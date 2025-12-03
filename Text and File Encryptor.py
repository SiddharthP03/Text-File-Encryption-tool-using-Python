import os

def encrypt_text(text, key):
    result = ""
    for char in text:
        result += chr((ord(char) + key) % 256)
    return result

def decrypt_text(text, key):
    result = ""
    for char in text:
        result += chr((ord(char) - key) % 256)
    return result

def encrypt_file(input_file, output_file, key):
    with open(input_file, "rb") as f:
        data = f.read()

    encrypted = bytes([(byte + key) % 256 for byte in data])

    with open(output_file, "wb") as f:
        f.write(encrypted)

def decrypt_file(input_file, output_file, key):
    with open(input_file, "rb") as f:
        data = f.read()

    decrypted = bytes([(byte - key) % 256 for byte in data])

    with open(output_file, "wb") as f:
        f.write(decrypted)

while True:
    print("\n1. Encrypt Text")
    print("2. Decrypt Text")
    print("3. Encrypt File")
    print("4. Decrypt File")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        message = input("Enter text to encrypt: ")
        key = int(input("Enter key (number): "))
        print("Encrypted:", encrypt_text(message, key))

    elif choice == "2":
        message = input("Enter text to decrypt: ")
        key = int(input("Enter key (number): "))
        print("Decrypted:", decrypt_text(message, key))

    elif choice == "3":
        infile = input("Enter file path to encrypt: ")
        outfile = input("Enter output file path: ")
        key = int(input("Enter key (number): "))
        encrypt_file(infile, outfile, key)
        print("File encrypted successfully!")

    elif choice == "4":
        infile = input("Enter file path to decrypt: ")
        outfile = input("Enter output file path: ")
        key = int(input("Enter key (number): "))
        decrypt_file(infile, outfile, key)
        print("File decrypted successfully!")

    elif choice == "5":
        break

    else:
        print("Invalid option, try again.")
