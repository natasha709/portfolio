def cv(request):
    return render(request, 'cv.html')
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

def home(request):
    return render(request, 'index.html')

def projects(request):
    return render(request, 'projects.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = f'Portfolio Contact Form: {name}'
        body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
        try:
            send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, ['natashawinnie20@gmail.com'])
            messages.success(request, 'Thank you for reaching out! Your message has been sent.')
        except Exception as e:
            messages.error(request, 'Sorry, there was a problem sending your message. Please try again later.')
        return redirect('contact')
    return render(request, 'contact.html')

def project_detail(request, project_id):
    # For now, just show details for the inventory system
    project = {
        'id': 1,
        'title': 'Inventory Management System',
        'description': 'A comprehensive inventory management system designed to help businesses track their products, manage stock levels, and monitor sales.',
        'features': [
            'Real-time stock tracking',
            'Product categorization',
            'Low stock alerts',
            'Sales reporting',
        ],
        'github': 'https://github.com/Natasha-Justine/karibu',
        'tech': ['Python', 'Flask', 'SQLite'],
    }
    return render(request, 'project_detail.html', {'project': project})
