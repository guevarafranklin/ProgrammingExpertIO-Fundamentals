w = -2  # <- Change this
x = 3  # <- Change this
y = 8  # <- Change this
z = 1  # <- Change this

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first_slice = lst[::z]
#print(first_slice)
second_slice = first_slice[:y]
# print(second_slice)
third_slice = second_slice[x:]
# print(third_slice)
last_slice = third_slice[::w]

print(last_slice)