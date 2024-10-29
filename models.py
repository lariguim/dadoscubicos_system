import json
from datetime import datetime
from pathlib import Path

class User:
    def __init__(self, username, password, role="customer"):
        self.username = username
        self.password = password  # In production, use proper password hashing
        self.role = role
        
    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "role": self.role
        }

class Project:
    def __init__(self, name, description, client_username, status="active"):
        self.name = name
        self.description = description
        self.client_username = client_username
        self.status = status
        self.created_at = datetime.now().isoformat()
        
    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "client_username": self.client_username,
            "status": self.status,
            "created_at": self.created_at
        }