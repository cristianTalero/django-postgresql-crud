from django import forms
from .models import Task


class NewTask(forms.Form):

    title = forms.CharField(
        label='Title',
        max_length=40,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    description = forms.CharField(
        label='Description',
        max_length=80,
        widget=forms.Textarea(
            attrs={
                'rows': 7,
                'cols': 25,
                'class': 'form-control'
            }
        )
    )


class EditTask(forms.Form):
    title = forms.CharField(
        label='Title',
        max_length=40,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    description = forms.CharField(
        label='Description',
        max_length=80,
        widget=forms.Textarea(
            attrs={
                'rows': 7,
                'cols': 25,
                'class': 'form-control',
            }
        )
    )
    status = forms.BooleanField(
        label='Done',
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input'
            }
        )
    )

