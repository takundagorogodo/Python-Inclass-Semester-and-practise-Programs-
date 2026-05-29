alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char

    print(f"Here's the text after encryption: {cipher_text}")


def decrypt(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_key) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text += char

    print(f"Here's the text after decryption: {plain_text}")


program_running = True

while program_running:
    action = input("Type 'encrypt' to encrypt, type 'decrypt' to decrypt:\n")
    message = input("Type your message:\n")
    shift = int(input("Enter shift key:\n"))

    if action == "encrypt":
        encrypt(plain_text=message, shift_key=shift)
    elif action == "decrypt":
        decrypt(cipher_text=message, shift_key=shift)
    
    restart = input("Type 'yes' to continue or 'no' to exit:\n").lower()
    if restart == "no":
        program_running = False
