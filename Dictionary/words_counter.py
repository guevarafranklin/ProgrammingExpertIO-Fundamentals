string = input("Enter your paragraph: ")

words_counter = string.split(" ")
counter = 0

for w in words_counter:
    counter += 1

print(f"The number of words on this paragraph is: {counter}")