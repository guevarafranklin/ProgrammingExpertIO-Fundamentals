lst = [3, 4, 5, 0.1, 2]

sorted(lst, reverse=True)
print(lst)

# Explanation

# In Python, the sorted() function takes in an iterable object and returns a new list containing the object's elements in sorted order. It doesn't sort in place and therefore doesn't mutate the iterable object that's passed to it.

# In the provided code, sorted(lst) doesn't change the value of lst; it creates and returns a new list that's sorted. Thus, printing lst at the end of the program just outputs the original value of lst, which is [3, 4, 5, 0.1, 2].
