string = input("Enter a string: ")
frequency = {}

for word in string:
    frequency[word] = frequency.get(word, 0) + 1


for key, items in frequency.items():
    print(f"{key}: {items}")