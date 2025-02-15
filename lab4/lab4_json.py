import json
import os


file_path = "lab4/sample-data.json"



if not os.path.exists(file_path):
    print(f"Ошибка: Файл {file_path} не найден!")
    exit()


with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)


print("Interface Status")
print("=" * 80)
print(f"{'DN':50} {'Speed':10} {'MTU':10}")
print("-" * 80)


for item in data.get("imdata", []):
    attributes = item.get("l1PhysIf", {}).get("attributes", {})
    dn = attributes.get("dn", "N/A")
    speed = attributes.get("speed", "inherit")
    mtu = attributes.get("mtu", "unknown")
    print(f"{dn:50} {speed:10} {mtu:10}")
