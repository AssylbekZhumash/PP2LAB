import json

with open("sample-data.json", "r") as file:
    data = json.load(file)


print("Interface Status")
print("=" * 80)
print(f"{'DN':50} {'Speed':10} {'MTU':10}")
print("-" * 80)


for item in data["imdata"]:
    dn = item["l1PhysIf"]["attributes"]["dn"]
    speed = item["l1PhysIf"]["attributes"].get("speed", "inherit")
    mtu = item["l1PhysIf"]["attributes"].get("mtu", "unknown")
    print(f"{dn:50} {speed:10} {mtu:10}")
