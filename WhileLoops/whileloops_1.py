array_lst = []
while True:
    num = int(input("Enter a number: "))
    array_lst.append(num)
    if num == 5:
        print(f"You entered {len(array_lst)} numbers.") 
        break