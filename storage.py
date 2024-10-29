import json
import os
from pathlib import Path

class Storage:
    def __init__(self):
        self.base_path = Path("data")
        self.users_file = self.base_path / "users.json"
        self.projects_file = self.base_path / "projects.json"
        self._init_storage()
    
    def _init_storage(self):
        self.base_path.mkdir(exist_ok=True)
        if not self.users_file.exists():
            self._save_json(self.users_file, [])
        if not self.projects_file.exists():
            self._save_json(self.projects_file, [])
            
    def _load_json(self, file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
            
    def _save_json(self, file_path, data):
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
            
    def save_user(self, user):
        users = self._load_json(self.users_file)
        users.append(user.to_dict())
        self._save_json(self.users_file, users)
        
    def get_user(self, username):
        users = self._load_json(self.users_file)
        return next((u for u in users if u["username"] == username), None)
        
    def save_project(self, project):
        projects = self._load_json(self.projects_file)
        projects.append(project.to_dict())
        self._save_json(self.projects_file, projects)
        
    def get_client_projects(self, username):
        projects = self._load_json(self.projects_file)
        return [p for p in projects if p["client_username"] == username]