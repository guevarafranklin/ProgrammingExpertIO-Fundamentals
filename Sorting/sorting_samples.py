def sort_second_index(item):
    return item[0]

lst = [[1, -2], [3, -4], [5,-6], [-1, -2], [0, 0]]
lst.sort(reverse=True, key=sort_second_index)
print(lst)