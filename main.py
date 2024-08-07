# printing the logo
from art import logo

print(logo)

# adding the letters twice in alphabet variable for the letters with high shift number
# for e.g word = zack , shift number = 10
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# creating while loop to repeat the program accoridng to the user's choice
should_continue = True  # creating a variable to stop while loop
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Combining the decrpyt and encrypt function into one function
    def caesar(start_text, shift_amount, cipher_direction):
        end_text = ""  # creating a variable to store the text after the shift
        # placing the if statement outside of for loop to prevent the bug created by for loop
        # if the user wants to decode the text
        if cipher_direction == "decode":
            shift_amount *= -1  # multiplying the shift number by -1 to get the negative shift number
        for char in start_text:
            if char in alphabet:  # checking if the character is in the alphabet list
                # finding the position(index) of the each letter in the alphabet list
                position = alphabet.index(char)
                # adding the shift number to the position of the letter to get the new position of the letter
                new_position = position + shift_amount
                end_text += alphabet[
                    new_position]  # adding the new letter to the end_text variable
            else:  # otherwise it'll just print the symbols and numbers as it is
                end_text += char
        # setting the print statement dynamically according to the direction choosed by the user
        print(f"The {cipher_direction}d text is: {end_text}")

    # using modulus to get the remainder of the shift number even if the enter user enters a large shift number
    shift = shift % 26
    # Calling the caesar function with the arguments
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # asking the user if they want to continue or not
    result = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    # ending the while loop if the user enters "no"
    if result == "no":
        should_continue = False
        print("Thankyou for using Caesar Cipher program. \nGoodbye!")
