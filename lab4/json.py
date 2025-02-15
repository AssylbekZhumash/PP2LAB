import json

# Определяем путь к файлу вручную
file_path = r"C:\Users\Асыл\Desktop\lab4\sample-data.json"

# Открываем JSON-файл и загружаем данные
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Заголовок таблицы
print("Interface Status")
print("=" * 80)
print(f"{'DN':50} {'Speed':10} {'MTU':10}")
print("-" * 80)

# Извлекаем интерфейсы и их параметры
for item in data["imdata"]:
    dn = item["l1PhysIf"]["attributes"]["dn"]
    speed = item["l1PhysIf"]["attributes"].get("speed", "inherit")
    mtu = item["l1PhysIf"]["attributes"].get("mtu", "unknown")
    print(f"{dn:50} {speed:10} {mtu:10}")