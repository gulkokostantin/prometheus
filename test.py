import os


def create_structure():
    # Перевірка наявності папок перед їх створенням
    folders_to_create = [
        "config",
        "modules/common",
        "modules/ui/page_objects",
        "modules/api/clients",
        "tests/ui",
        "tests/api"
    ]

    for folder in folders_to_create:
        if not os.path.exists(folder):
            os.makedirs(folder)
        else:
            print(f"Папка '{folder}' вже існує.")

    # Створення файлів
    files_to_create = [
        "config/config.py",
        "modules/common/__init__.py",
        "modules/ui/__init__.py",
        "modules/ui/page_objects/__init__.py",
        "modules/api/__init__.py",
        "modules/api/clients/__init__.py",
        "tests/ui/test_ui.py",
        "tests/api/test_api.py"
    ]

    for file in files_to_create:
        if not os.path.exists(file):
            with open(file, "w") as f:
                pass
        else:
            print(f"Файл '{file}' вже існує.")


if __name__ == "__main__":
    create_structure()
