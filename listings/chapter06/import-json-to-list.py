import json

with open('iris.json', 'r', newline='') as json_file:
    irises = json.load(
        json_file,
        object_hook = lambda obj: list(obj.values())
    )

print(f"{len(irises)} Datensätze importiert.")
print(irises[0])
print(irises[50])
print(irises[100])
