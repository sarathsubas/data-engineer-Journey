with open("sample_file.txt", "r") as file:
    list = file.readlines()
    print(list)
    word_counts = {}
    for line in list:
        line = line.strip().lower()
        words = line.split()
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

print(word_counts)