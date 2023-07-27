def string_lengths(strings):
    # Write your code here.
    new_str = []
    for item in strings:
        new_str.append(len(item))
    return new_str

strings = ["hello", "this", "is", "a", "beard", "orange", "blue"]
print(string_lengths(strings))
