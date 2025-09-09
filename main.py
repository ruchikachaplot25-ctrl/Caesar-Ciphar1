
import string
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def command():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    l=''
    position=0
    encrypted_text =[]
    def encrypt():
        for i in range(len(text)):
            l = text[i]
            if l in alphabet:
                position=alphabet.index(l)
                #print(f"{position}")
                new_position = (position + shift) % len(alphabet)
                encrypted_text.append(alphabet[new_position])
            elif l in string.ascii_letters or l in string.digits or l in string.whitespace:
                encrypted_text.append(l)
        print(''.join(encrypted_text))

    decrypt_text=[]
    def decrypt():
        for i in range(len(text)):
            l = text[i]
            if l in alphabet:
                position=alphabet.index(l)
            #print(f"{position}")
                new_position = (position - shift) % len(alphabet)
                decrypt_text.append(alphabet[new_position])
            elif l in string.ascii_letters or l in string.digits or l in string.whitespace:
                decrypt_text.append(l)
        print(''.join(decrypt_text))

    if direction == "encode":
        encrypt()
    elif direction == "decode":
        decrypt()
    again=input("Wanna run again Y for yencodes N for no").upper()
    if again=="Y":
        command()
    else:
        print("Bye")

    # 👇 This line actually runs the program
command()






