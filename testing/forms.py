from datetime import date
from django.forms import formset_factory
from django import forms
from .models import PersonalResult, PsyTest, Question, Option, TestResult
from django.contrib.auth.models  import User 
from customuser.models import CustomUser
from psy_test import settings


class PsyTestForm(forms.ModelForm):

    class Meta:
        model = PsyTest
        fields = '__all__'
        exclude = ['addition_date', 'is_passed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input test title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Input test description'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input test author'}),
            'added_by': forms.HiddenInput()
        }


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = '__all__'
        widgets = {
            'test': forms.HiddenInput(),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Input description', 'rows': 5}),
        }

class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['description', 'points']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Input description', 'rows': 2}),
            'points': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Input points for option', 'rows': 2, 'style': 'width: 100%'})
        }

OptionFormSet = forms.modelformset_factory(Option, form=OptionForm, extra=5, min_num=6)

class TestResultForm(forms.ModelForm):

    class Meta:
        model = TestResult
        fields = '__all__'
        widgets = {
            'test': forms.HiddenInput(),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Input description', 'rows': 5}),
            'condition_min': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Input points for option', 'rows': 2}),
            'condition_max': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Input points for option', 'rows': 2})
        }

class TakeTestForm(forms.ModelForm):

    class Meta:
        model = PersonalResult
        fields = ['user','test', 'score']


class UserForm(forms.ModelForm):
    date_of_birth = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'password', 'date_of_birth', 'phone_number', 'gender')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Input your email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Input your password'}),
            'date_of_birth': forms.DateInput(format='%d.%m.%Y', attrs={'class': 'form-control', 'placeholder': 'Input your date of birth', 'type': date}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input your phone number'}),
            'gender': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Choouse your gender'})

        }

class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'password', 'date_of_birth', 'phone_number', 'gender')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Input your email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Input your password'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Input your date of birth'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input your phone number'}),
            'gender': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Choouse your gender'})

        }
