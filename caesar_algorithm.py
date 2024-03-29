def caesar_encode(text , shift):
    encoded_text = ""
    for c in text:
        if c.isupper():
            encoded_text += chr((ord(c)+shift-65)%26+65)
        else:
            encoded_text += chr((ord(c)+shift-97)%26+97)
    return encoded_text

def caesar_decode(text, shift):
    decoded_text = ""
    for c in text:
        if c.isupper():
            decoded_text += chr((ord(c)-shift-65)%26+65)
        else:
            decoded_text += chr((ord(c)-shift-97)%26+97)
    return decoded_text
     

print("\tWELCOME TO CAESAR ALGORITHM PROGRAM")
text = input("Enter a text : ")
shift = int(input("Enter a shift value : "))

print("\n1)Encode")
print("2)Decode")
choice = int(input("Select option (1-2) : "))
output = caesar_encode(text , shift) if choice == 1 else caesar_decode(text , shift)
print(output)