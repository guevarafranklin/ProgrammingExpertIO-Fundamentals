def caesar_cipher(string, offset):
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
    encoded_string = ''
    for char in string: 
        position = alphabet.index(char)
        offset_pos = position - offset
        encoded_char = alphabet[offset_pos]
        encoded_string += encoded_char

    return encoded_string
            
string = input("Enter the string to cipher: ")
offset = int(input("Enter the offset: "))
print(caesar_cipher(string, offset))