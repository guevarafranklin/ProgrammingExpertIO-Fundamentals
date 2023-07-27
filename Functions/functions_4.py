def compare_lists(lst1=[], lst2=[]):
    lst1_set = set(lst1)
    lst2_set = set(lst2)
    counter = 0
    for i in lst1_set:
        if i in lst2_set:
            counter += 1
    return counter

lst = [1, 2, 3]
lst_2 = [1, 2, 4]

print(compare_lists(lst2=[1, 2, 3]))