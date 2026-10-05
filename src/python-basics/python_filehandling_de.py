from pathlib import Path
import csv

print("========== FILE INVENTORY ==========")
lisfil =[]
csvlis =[]
jlis=[]
path_file = Path("datasets/sales_data.csv")
directory = Path("datasets")
print(path_file)
print(directory)
for file in directory.iterdir():
    print(file.name)
    lisfil.append(file.name)
print(f"Total files: {len(lisfil)}")
print("---------- CSV FILES ----------")

for file in directory.glob("*.csv"):
    print(file.name)
    csvlis.append(file.name)

print(f"CSV files: {len(csvlis)}")

for file in directory.glob("*.json"):
    print(file.name)
    jlis.append(file.name)

print(f"JSON files: {len(jlis)}")

print(path_file.exists())
path_file1 = Path("datasets//test.csv")
print(path_file1.exists())
try:
    content = path_file1.read_text()
except:
    print("ERROR: File not found")
else:
    print(content)

print("---------------Mini Data Engineering challenge----------")
print("---------========== INPUT FILE REPORT ==========--------")

listcsv =[]
councsv = []
for file in directory.glob("*.csv"):
    listcsv.append(file.name)
    with open(file) as f:
        header = next(f)
        dataset = f.readlines()
        councsv.append(len(dataset))

print(listcsv,councsv)

for x,y in zip(listcsv,councsv):
    print(f"{x} --> {y}")

print(f"Total CSV files: {len(listcsv)}")
print(f"Total records: {sum(councsv)}")