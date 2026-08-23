str = "data engineering is fun and data engineering is useful"
count = 0
x = str.split()
word_frequency = set()
for i in x:
    if i not in word_frequency:
        print(f"{i}:{x.count(i)}")
        word_frequency.add(i)
