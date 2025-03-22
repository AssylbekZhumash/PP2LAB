import os

def path_info(path):
    if os.path.exists(path):
        print("✅ Путь существует")
        print("📂 Директория:", os.path.dirname(path))
        print("📄 Имя файла:", os.path.basename(path))
    else:
        print("❌ Путь не существует")

path_info("test_folder/file1.txt") 