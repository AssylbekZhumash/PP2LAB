import os

def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        print(f"🗑️ Файл {path} удален!")
    else:
        print("❌ Файл не существует или нельзя удалить")

delete_file("test_folder/copy_of_file1.txt")
