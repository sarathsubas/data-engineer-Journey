from pathlib import Path

file_path = Path("datasets\\sales_data.csv")
folder = Path("datasets")
print(file_path)
print(file_path.exists())
lis_dir = []
csv_lis =[]
for file in folder.iterdir():
    lis_dir.append(file.name)
    print(file.name)
print(len(lis_dir))

for file in folder.glob("*.json"):
    csv_lis.append(file.name)
    print(file.name)

print(csv_lis)
print(file_path.suffix)
print(file_path.stem)
print(file_path.absolute())