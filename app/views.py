from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from app.form import SignUpForm
from .form import StudentSignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # do any additional processing or redirect to a new page
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def student_signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = StudentSignUpForm()
    return render(request, 'student_signup.html', {'form': form})