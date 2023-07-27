def find_all_odds(lst):
    # Write your code here.
    new_lst = []
    for item in lst:
        if item % 2 != 0:
            new_lst.append(item)


    return new_lst


str = [1, 2, 3, 4, 5, 6, 5, 5, 3, 2]
print(find_all_odds(str))
