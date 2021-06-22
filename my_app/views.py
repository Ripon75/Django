from django import forms
from django.shortcuts import render
from .models import Student
from my_app import forms

def home(request):
    student_list = Student.objects.all()
    dictionary = {'students':student_list}
    return render(request,'my_app/index.html',context=dictionary)


def about(request):
    return render(request,'my_app/about.html')

def contact(request):
    return render(request,'my_app/contact.html')


# def form(request):
#     student_form = forms.Student_form()
#     diction = {
#         'student_form': student_form
#     } 
#     return render(request, 'my_app/form.html', context=diction)

def form(request):
    new_form = forms.Student_form()
    if request.method == "POST":
        new_form = forms.Student_form(request.POST)
        if new_form.is_valid():
            new_form.save(commit=True)
            return home(request)
        
    diction = {
        'student_form': new_form
    } 
    return render(request, 'my_app/form.html', context=diction)