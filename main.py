from models import User, Project
from storage import Storage
from auth import AuthManager
from project_manager import ProjectManager

def main():
    storage = Storage()
    auth_manager = AuthManager(storage)
    project_manager = ProjectManager(storage)
    
    while True:
        print("\n=== Project Management System ===")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            
            user = auth_manager.login(username, password)
            if user:
                handle_user_session(user, project_manager)
            else:
                print("Invalid credentials!")
                
        elif choice == "2":
            username = input("Choose username: ")
            password = input("Choose password: ")
            
            if auth_manager.register(username, password):
                print("Registration successful!")
            else:
                print("Username already exists!")
                
        elif choice == "3":
            break
            
def handle_user_session(user, project_manager):
    while True:
        print(f"\nWelcome, {user['username']}!")
        print("1. View My Projects")
        print("2. Create New Project")
        print("3. Logout")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            projects = project_manager.get_client_projects(user["username"])
            if projects:
                for idx, project in enumerate(projects, 1):
                    print(f"\n{idx}. {project['name']}")
                    print(f"   Description: {project['description']}")
                    print(f"   Status: {project['status']}")
            else:
                print("No projects found.")
                
        elif choice == "2":
            name = input("Project name: ")
            description = input("Project description: ")
            
            project = project_manager.create_project(name, description, user["username"])
            project_manager.create_project_folder(name, user["username"])
            print("Project created successfully!")
            
        elif choice == "3":
            break

if __name__ == "__main__":
    main()