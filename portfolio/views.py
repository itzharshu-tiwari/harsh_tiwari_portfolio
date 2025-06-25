from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Resume, HeroSection, Skill
from .models import Certificate
from .models import Project

# Home Page (Hero + Skills)
def index(request):
    hero = HeroSection.objects.first()
    skills = Skill.objects.all()
    return render(request, 'home.html', {
        'hero': hero,
        'skills': skills
    })

# About Page
def about(request):
    certificates = Certificate.objects.all()
    return render(request, 'about.html', {'certificates': certificates})

# Projects Page
def project(request):
    projects = Project.objects.all()
    return render(request, 'project.html', {'projects': projects})

# Contact Page with Form
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Message sent successfully! I’ll get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# Resume Page
def resume_list(request):
    resumes = Resume.objects.all()
    return render(request, 'resume.html', {'resumes': resumes})

 