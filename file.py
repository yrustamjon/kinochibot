import os

structure = {
    "main.py": "",
    "config.py": "",
    "data": {
        "movies": {},
        "users": {},
        "channels": {}
    },
    'apps': {
        "handlers": {
        "user.py": "",
        "admin.py": ""
        },
        "keyboards": {
            "user_kb.py": "",
            "admin_kb.py": ""
        }
    }
}

def create(path, tree):
    for name, content in tree.items():
        full_path = os.path.join(path, name)

        if isinstance(content, dict):
            # Folder
            os.makedirs(full_path, exist_ok=True)
            create(full_path, content)
        else:
            # File
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content)

if __name__ == "__main__":
    project_root = os.getcwd()  # Current folder
    create(project_root, structure)
    print("✅ Project structure created successfully!")
