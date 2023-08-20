people = {"Tim": 21, "Joe": 18, "Sarah": 25, "Jennie": 26, "Bill": 34}

result = sorted(people, key=people.get)
print(result)

# Explanation

# In Python, the sorted() function takes in an iterable object and returns a new list containing the object's elements in sorted order. It also takes in two optional parameters: reverse (a boolean) and key (a function).

# By default, passing a dictionary to the sorted() function returns a list of the dictionary's keys sorted according to their actual value (i.e., the value "Tim" in the provided code). However, if the key argument is passed to sorted(), the function will sort the dictonary's keys by the result of each dictionary key passed to the passed key function (the key function must return a comparable object).

# In the provided code, we use people.get as the key function. This means that the keys in the dictionary will be sorted based on their values, which are integers. Therefore, result will be equal to ["Joe", "Tim", "Sarah", "Jennie", "Bill"], and that will be printed by the program.
