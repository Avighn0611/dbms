# forms.py
from django import forms

class DataForm(forms.Form):
    new_question = forms.CharField(label='new_question', max_length=500)
    correct_option = forms.CharField(label='Field 2', max_length=100)
    option1 = forms.CharField(label='Field 2', max_length=100)
    option2 = forms.CharField(label='Field 2', max_length=100)
    option3 = forms.CharField(label='Field 2', max_length=100)
    option4 = forms.CharField(label='Field 2', max_length=100)

    # Add more fields as needed

