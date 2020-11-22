from sys import argv, exit

def main():
    # check that the user provided 2 arguments
    if len(argv) != 2:
        print("Usage: python caesar_coder.py shift_number")
        exit(1)
    # check that the shift val provided by the user is an int
    try:
        shift = int(argv[1])
    except ValueError:
        print("Shift is not an integer")
        return exit(1)
    # change the shift to be between 0 and 25
    if shift < 0:
        shift = 25 + shift + 1
    if shift > 25:
        shift = shift % 26
    # get plaintext from user
    plaintext = input("Plaintext: ")
    try:
        i = int(plaintext)
    except ValueError:
        print("Good")
    # generate ciphertext with a shift of shift
    ciphertext = convert_to_cipher(plaintext, shift)
    # print out the cipher text
    print(f"Ciphertext: {ciphertext}")
    # exit
    exit(0)

def convert_to_cipher(plaintext, shift):
    ciphertext = []
    # repeat for every character in plaintext
    for char in plaintext:
        # Check if char is alphabetic
        if not char.isalpha():
            ciphertext.append(char)
            continue
        # Find the position of the letter in the alphabet
        pos = ord(char)
        if char.isupper():
            pos -= 65
        else:
            pos -= 97
        # Add the shift to the position of the char
        pos+=shift
        new_pos = pos % 26
        # Convert the new position back to a char. Call it new_char
        if char.islower():
            new_pos += 97
        else:
            new_pos += 65
        new_char = chr(new_pos)
        # Put this converted char into a ciphertext lst
        ciphertext.append(new_char)
        # print(char, new_char, sep=" | ")


    return "".join(ciphertext)

main()