"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from app import cv_data

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def cv2(request):
    """Renders the cv page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/cv2.html',
        {
            'title':'CV',
            'message':'Your CV page.',
            'year':datetime.now().year,
            'formations': cv_data.formations,
            'competences': cv_data.competences,
            'vie_associatives': cv_data.vie_associatives,
            'loisirs': cv_data.loisirs,
        }
    )

def projects(request):
    """Renders the projects page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/projects.html',
        {
            'title':'Projects',
            'message':'Your projects page.',
            'year':datetime.now().year,
        }
    )
