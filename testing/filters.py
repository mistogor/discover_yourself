import django_filters
from django import forms
from .models import PsyTest, TestCategory


class TestFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input test title', 'row': 3}))
    category = django_filters.ModelChoiceFilter(queryset=TestCategory.objects.all(), widget = forms.Select(attrs={'class': 'form-control'}))
    author = django_filters.CharFilter(lookup_expr='icontains', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input test author'}))

    class Meta:
        model = PsyTest
        fields = ['title', 'category', 'author']
