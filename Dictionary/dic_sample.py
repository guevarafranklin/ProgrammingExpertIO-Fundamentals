ages = {
    "Franklin": 33,
    "Gaby": 35,
    "Alex": 30,
}
print(f"Alex is, {ages['Franklin']} years old")


#Counting characters 

characters = {}

string = "Hello World"

for char in string: 
    characters[char] = characters.get(char, 0) + 1

print(characters)

# Welcome to our Python playground!

salaries = {
    "Brad": 10,
    "Lucy": 12,
    "John": 6.5,
}

for name in salaries:
    salary = salaries[name]
    print(f"{name} makes ${salary} an hour")


for name, salary in salaries.items():
    weekly_salary = salary * 40
    print(f"{name} makes ${weekly_salary} an week")