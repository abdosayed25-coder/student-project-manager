import json
import os

FILE_NAME = "projects.json"

def load_projects():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_projects(projects):
    with open(FILE_NAME, "w") as file:
        json.dump(projects, file, indent=4)

def add_project(projects):
    name = input("Project name: ")
    deadline = input("Deadline: ")
    projects.append({
        "name": name,
        "deadline": deadline,
        "completed": False
    })
    save_projects(projects)
    print("Project added successfully.")

def view_projects(projects):
    if not projects:
        print("No projects found.")
        return
    for i, project in enumerate(projects):
        status = "Done" if project["completed"] else "Pending"
        print(f"{i + 1}. {project['name']} - {project['deadline']} - {status}")

def mark_completed(projects):
    view_projects(projects)
    choice = int(input("Select project number to mark as completed: ")) - 1
    if 0 <= choice < len(projects):
        projects[choice]["completed"] = True
        save_projects(projects)
        print("Project marked as completed.")
    else:
        print("Invalid choice.")

def main():
    projects = load_projects()
    while True:
        print("\n1. Add Project")
        print("2. View Projects")
        print("3. Mark Project as Completed")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_project(projects)
        elif choice == "2":
            view_projects(projects)
        elif choice == "3":
            mark_completed(projects)
        elif choice == "4":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
