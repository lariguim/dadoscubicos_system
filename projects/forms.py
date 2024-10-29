from django import forms
from .models import Project, ProjectFile

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']

class ProjectFileForm(forms.ModelForm):
    class Meta:
        model = ProjectFile
        fields = ['file_type', 'file', 'description']