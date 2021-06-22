from django import forms
from my_app import models

# class Student_form(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()

class Student_form(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = "__all__"