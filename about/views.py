from django.shortcuts import render

# Create your views here.

def classes(request):
    return render(request, 'classes.html')

def student(request):
    return render(request, 'student.html')

def teacher(request):
    return render(request, 'teacher.html')
