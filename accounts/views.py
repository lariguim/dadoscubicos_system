from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomerProfileForm
from .models import CustomerProfile
from projects.models import Project, ProjectFile

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        profile_form = CustomerProfileForm(request.POST)
        
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = UserCreationForm()
        profile_form = CustomerProfileForm()
    
    return render(request, 'accounts/register.html', {
        'form': form,
        'profile_form': profile_form
    })

@login_required
def dashboard(request):
    active_projects = Project.objects.filter(client=request.user, status='active')
    completed_projects = Project.objects.filter(client=request.user, status='completed')
    recent_projects = Project.objects.filter(client=request.user).order_by('-created_at')[:5]
    recent_files = ProjectFile.objects.filter(project__client=request.user).order_by('-uploaded_at')[:5]
    
    context = {
        'active_projects_count': active_projects.count(),
        'completed_projects_count': completed_projects.count(),
        'recent_projects': recent_projects,
        'recent_files': recent_files,
        'recent_files_count': ProjectFile.objects.filter(project__client=request.user).count()
    }
    
    return render(request, 'accounts/dashboard.html', context)