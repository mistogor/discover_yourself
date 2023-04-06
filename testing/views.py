from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse_lazy
from django.urls import reverse
from django import forms
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms.models import inlineformset_factory
from django.http import HttpResponseNotAllowed, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.forms import modelformset_factory


from testing.filters import TestFilter
from .models import TestCategory, Question, PsyTest, TestResult, PersonalResult, Option
from .forms import PsyTestForm, QuestionForm, OptionForm, TestResultForm, UserForm, UserEditForm, OptionFormSet

def index(request):
    return render(request, 'testing/index.html')


def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            return redirect('/home')
    else:
        user_form = UserForm()
    return render(request, 'testing/auth/register.html', {'user_form': user_form})


def auth(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome, {user}! ')
            return redirect('/home')
        else:
            messages.info(request, 'Something went wrong. Please try again!')
            return redirect('/login')
    else:
        return render(request, 'testing/auth/login.html')
    

@login_required
def log_out(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")


def create_test(request):
    if request.user.is_superuser:
        user = request.user
        if request.method == 'POST':
            test_form = PsyTestForm(request.POST)
            if test_form.is_valid():
                user = user
                test = test_form.save(commit=False)
                test.added_by = user
                test.save()
                            
                messages.success(request, 'Test created')
                return redirect('create_questions', test_id = test.id)
        else:
            test_form = PsyTestForm(initial= {'added_by': request.user,
                                              })
        return render(request, 'testing/creating/create_test.html', {
            'test_form': test_form,
        })
    else:
        return HttpResponse(request, 'You have no rights')

def create_questions(request, test_id):
    if request.user.is_superuser:
        test = PsyTest.objects.get(id=test_id)
        if request.method == 'POST':
            question_form = QuestionForm(request.POST)
            OptionFormSet = inlineformset_factory(Question, Option, form=OptionForm, can_delete=True, extra=6)
            option_formset = OptionFormSet(request.POST)

            if question_form.is_valid() and option_formset.is_valid():
                question = question_form.save(commit=False)
                question.test = test
                question.save()

                options = option_formset.save(commit=False)
                for option in options:
                    option.question = question
                    option.save()

                action = request.POST.get('action', 'back')
                question_number = int(request.POST.get('question_number', 1))

                if action == 'add':
                    question_number += 1
                    question_form = QuestionForm(initial={'test': test, 'number': question_number})
                    option_formset = OptionFormSet(queryset=Option.objects.none())
                if action == 'results':
                    return redirect('create_results', test_id)
                elif action == 'finish':
                    return redirect('tests-list')
            else:
                question_number = int(request.POST.get('question_number', 1))
        else:
            question_number = 1
            question_form = QuestionForm(initial={'test': test, 'number': question_number})
            OptionFormSet = inlineformset_factory(Question, Option, form=OptionForm,can_delete=True, extra=6)
            option_formset = OptionFormSet(queryset=Option.objects.none())

        return render(request, 'testing/creating/create_questions.html', context={'test': test, 'question_form': question_form, 'option_formset': option_formset, 'question_number': question_number})
    else:
        return HttpResponse(request, 'You have no rights')


def create_test_results(request, test_id):
    if request.user.is_superuser:
        test = PsyTest.objects.get(id=test_id)
        test_result_form = TestResultForm()
        if request.method == 'POST':
            test_result_form = TestResultForm(request.POST)
            if test_result_form.is_valid():
                result = test_result_form.save(commit=False)
                result.test = test
                result.save()
                messages.success(request, 'Result created')
            return redirect('create_results', test_id=test_id)
        
        result_number = test.testresult_set.count() + 1
        test_result_form = TestResultForm(initial={'test': test})
        
        return render(request, 'testing/creating/create_results.html', {
            'test': test,
            'test_result_form': test_result_form,
            'result_number': result_number
        })
    else:
        return HttpResponse(request, 'You have no rights')
    

class EditTest(UpdateView):
    model = PsyTest
    fields = ['title', 'description', 'author', 'category']
    template_name = 'testing/editing/edit_test.html'

    def get_success_url(self):
        return reverse_lazy('test_info', kwargs={'test_id': self.object.pk})


class EditResult(UpdateView):
    model = TestResult
    fields = ['description', 'condition_min', 'condition_max']
    template_name = 'testing/editing/edit_result.html'

    def get_success_url(self):
        return reverse('test_info', kwargs={'test_id': self.object.test.id})


class DeleteTest(DeleteView):
    model = PsyTest
    success_url = '/tests_list'
    template_name = 'testing/editing/delete_test.html'

@login_required
def tests_list(request):
    f = TestFilter(request.GET, queryset=PsyTest.objects.all())
    return render(request, 'testing/psytesting/tests_list.html', {'filter': f})


@login_required
def test_info (request, test_id):
    test = PsyTest.objects.get(id = test_id)
    questions = Question.objects.filter(test = test)
    options = Option.objects.filter(question__in=questions)  # Получаем все связанные объекты Option
    results = TestResult.objects.filter(test=test)
    if request.method == 'GET':
        return render (request, 'testing/psytesting/test_info.html', {
            'test': test,
            'title': test.title,
            'category': test.category,
            'author': test.author,
            'description': test.description,
            'questions': questions,
            'options': options, 
            'results': results
            })
    
def edit_question(request, test_id, question_id):
    if request.user.is_superuser:
        test = PsyTest.objects.get(id = test_id)
        question = Question.objects.get(id = question_id)
        if request.method == 'POST':
            question_form = QuestionForm(request.POST, instance=question)
            OptionFormSet = inlineformset_factory(Question, Option, form=OptionForm, extra = 0, widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Input description', 'rows': 2}),
            'points': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Input points for option', 'rows': 2, 'style': 'width: 100%'})
            })
            option_formset = OptionFormSet(request.POST or None, instance=question)

            if question_form.is_valid() and option_formset.is_valid():
                question = question_form.save(commit=False)
                question.test = test
                question.save()

                options = option_formset.save(commit=False)
                for option in options:
                    option.question = question
                    option.save()
            
            return HttpResponseRedirect(reverse('test_info', args=[test.pk]))

        else:
            question_form = QuestionForm(initial={'test': test, 'question': question, 'description': question.description})
            OptionFormSet = inlineformset_factory(Question, Option, form=OptionForm, extra = 0)
            option_formset = OptionFormSet(instance=question, initial= {'id': question.pk,})

        return render(request, 'testing/editing/edit_question.html', context={'test': test, 'question': question, 'question_form': question_form, 'option_formset': option_formset,})
    else:
        return HttpResponse(request, 'You have no rights')


class DeleteQuestion(DeleteView):
    model = Question
    template_name = 'testing/editing/delete_question.html'
    def get_success_url(self):
        return reverse_lazy('test_info', kwargs={'test_id': self.object.pk})



@login_required
def take_test(request, test_id):
    test = PsyTest.objects.get(id=test_id)
    questions = test.question_set.all()
    options = Option.objects.filter(question__in=questions)
    user = request.user

    if request.method == 'POST':
        score = 0
        for question in questions:
            option_id = request.POST.get(f'question_{question.id}')
            if option_id is not None:
                option = Option.objects.get(pk=option_id)
                score += option.points
        personal_result = TestResult.objects.filter(test=test, condition_max__gte=score, condition_min__lte=score).first()
        messages.success(request, 'Test passed. Data saved in your profile!')
        final_result = PersonalResult(user=user, test=test, score=score, result = personal_result)
        final_result.save()
        return redirect('get_results', result_id=final_result.id)

    context = {
        'test': test,
        'questions': questions,
        'options': options
    }
    return render(request, 'testing/psytesting/take_test.html', context)


@login_required
def get_results(request, result_id):
    result = get_object_or_404(PersonalResult, pk=result_id, user=request.user)
    context = {
        'test': result.test,
        'score': result.score,
        'resume': result.result,
    }
    return render(request, 'testing/psytesting/get_results.html', context)

@login_required
def your_results(request):
    results = PersonalResult.objects.filter(user=request.user)

    return render(request, 'testing/psytesting/your_results.html', {'results': results})

@login_required
def your_results_details(request, result_id):
    result = get_object_or_404(PersonalResult, pk=result_id, user=request.user)
    context = {
        'test': result.test,
        'score': result.score,
        'resume': result.result,
    }
    return render(request, 'testing/psytesting/your_results_details.html', context)

@login_required
def create_test_panel(request):
        tests = PsyTest.objects.all()
        return render(request,'testing/psytesting/your_results.html')


