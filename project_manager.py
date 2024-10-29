class ProjectManager:
    def __init__(self, storage):
        self.storage = storage
        
    def create_project(self, name, description, client_username):
        project = Project(name, description, client_username)
        self.storage.save_project(project)
        return project
        
    def get_client_projects(self, username):
        return self.storage.get_client_projects(username)
        
    def create_project_folder(self, project_name, client_username):
        base_path = Path("data/client_files") / client_username / project_name
        base_path.mkdir(parents=True, exist_ok=True)
        
        # Create standard project folders
        (base_path / "documents").mkdir(exist_ok=True)
        (base_path / "invoices").mkdir(exist_ok=True)
        (base_path / "deliverables").mkdir(exist_ok=True)
        
        return base_path