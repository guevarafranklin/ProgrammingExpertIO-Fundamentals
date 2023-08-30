class ContactInformation: 
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.country = None

person1 = ContactInformation("Franklin", "Roberto", "tec@gmail.com", "801-781-6601")
person2 = ContactInformation("Gabriela", "Monse", "gaby@gmail.com", "801-781-6601")

print(person1.last_name)
print(person2.email)