import csv

with open('iris-tabs.csv', 'r', newline='') as iris_file:
    reader = csv.reader(
        iris_file, delimiter='\t', quoting=csv.QUOTE_NONNUMERIC
    )
    headers = next(reader, None)
    irises = list(reader)

print("Spaltentitel:", headers)
print(f"{len(irises)} Datensätze importiert.")
print(irises[0])
print(irises[50])
print(irises[100])
