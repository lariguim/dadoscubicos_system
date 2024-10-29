from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class ProjectFile(models.Model):
    FILE_TYPES = [
        ('document', 'Document'),
        ('invoice', 'Invoice'),
        ('deliverable', 'Deliverable'),
    ]
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=20, choices=FILE_TYPES)
    file = models.FileField(upload_to='project_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.project.name} - {self.file_type} - {self.description}"