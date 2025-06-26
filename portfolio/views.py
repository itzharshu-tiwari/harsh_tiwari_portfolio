from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def project(request):
    return render(request, 'project.html')

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

def resume_list(request):
    return render(request, 'resume.html')
