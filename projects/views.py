from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project, ProjectFile
from .forms import ProjectForm, ProjectFileForm

@login_required
def project_list(request):
    projects = Project.objects.filter(client=request.user)
    return render(request, 'projects/project_list.html', {'projects': projects})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, client=request.user)
    files = ProjectFile.objects.filter(project=project)
    
    if request.method == 'POST':
        file_form = ProjectFileForm(request.POST, request.FILES)
        if file_form.is_valid():
            project_file = file_form.save(commit=False)
            project_file.project = project
            project_file.save()
            messages.success(request, 'File uploaded successfully!')
            return redirect('project_detail', pk=pk)
    else:
        file_form = ProjectFileForm()
    
    return render(request, 'projects/project_detail.html', {
        'project': project,
        'files': files,
        'file_form': file_form,
    })

@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.client = request.user
            project.save()
            messages.success(request, 'Project created successfully!')
            return redirect('project_list')
    else:
        form = ProjectForm()
    
    return render(request, 'projects/project_form.html', {'form': form})