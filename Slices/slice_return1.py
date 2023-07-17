lst =  [1, 3, 4, 4, 3, 1, 2, 3, 2]
lst_2 = lst[:6:2] 
print(lst_2)

""" 
Explanation

Since there's no integer to the left of the first colon, 
that means the slice starts at the beginning of the list. 
With a 6 to the right of the first colon, the slice ends at but does not include index 6. 
Finally, we see a 2 to the right of the second colon, which means the slice steps by 2, 
effectively skipping every other element.
 """