from django.shortcuts import render, redirect
from .models import About, Certificate, Project, Feedback  # Import all relevant models
from .forms import FeedbackForm

def home(request):
    about_obj = About.objects.first()  # Corrected variable name to avoid conflict
    return render(request, 'home.html', {'about': about_obj})

def about(request):
    about_obj = About.objects.first()  # Corrected variable name to avoid conflict
    return render(request, 'about.html', {'about': about_obj})

def certificates(request):
    certificates = Certificate.objects.all()
    return render(request, 'certificates.html', {'certificates': certificates})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})



from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback  # Import your Feedback model

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to success page after submission
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to success page after submission
    else:
        form = FeedbackForm()

    return redirect('feedback')  # Redirect to feedback page after submission


def success_page(request):
    return render(request, 'success.html') 
