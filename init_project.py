import os

folders = [
    "app",
    "app/api",
    "app/api/endpoints",
    "app/core",
    "app/models",
    "app/services",
]

files = [
    "app/__init__.py",
    "app/main.py",
    "app/api/__init__.py",
    "app/api/endpoints/__init__.py",
    "app/api/endpoints/chat.py",
    "app/core/__init__.py",
    "app/core/config.py",
    "app/models/__init__.py",
    "app/models/chat_schema.py",
    "app/services/__init__.py",
    "app/services/ai_service.py"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Created folder: {folder}")

for file in files:
    if not os.path.exists(file):
        with open(file, 'w') as f:
            pass
        print(f"Created file: {file}")