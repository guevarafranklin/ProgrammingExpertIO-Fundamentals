import random

while True:
    counter = 0
    number_1 = input("Enter the start of the range: ")
    number_2 = input("Enter the end of the range: ")
    
    try:
        number_1 = int(number_1)
    except Exception as e:
        print("Please enter a valid number")

    try:
        number_2 = int(number_2)
    except Exception as e:
        print("Please enter a valid number")
    
    random_number = random.randint(int(number_1), int(number_2))

    while True:
        guess_number = input("Guess a number:")

        try:
            guess_number = int(guess_number)
        except Exception as e:
            print("Please enter a valid number")

    
        print(random_number)
        if random_number == guess_number:
            counter += 1 
            print(f"You guessed the number in {counter} attempt")
            break
        else:
            counter += 1
            continue

    
