from django.shortcuts import render, get_object_or_404
from .models import Profile, Experience, Skill, Education, Certification, Project, Recommendation

def home(request):
    """Main portfolio page"""
    profile = Profile.objects.first()
    experiences = Experience.objects.all()[:3]  # Show only recent 3
    skills = Skill.objects.all()
    educations = Education.objects.all()
    certifications = Certification.objects.all()
    recommendations = Recommendation.objects.all()[:2]  # Show only 2 recommendations
    
    context = {
        'profile': profile,
        'experiences': experiences,
        'skills': skills,
        'educations': educations,
        'certifications': certifications,
        'recommendations': recommendations,
    }
    return render(request, 'portfolio/home.html', context)

def projects(request):
    """Projects page"""
    projects = Project.objects.all()
    context = {
        'projects': projects,
        'profile': Profile.objects.first(),
    }
    return render(request, 'portfolio/projects.html', context)
