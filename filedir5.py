def write_list_to_file(filename, lst):
    with open(filename, 'w') as f:
        f.writelines(f"{item}\n" for item in lst)
    print(f"✅ Список записан в {filename}")

data = ["Python", "Java", "C++", "JavaScript"]
write_list_to_file("test_folder/programming_languages.txt", data)
