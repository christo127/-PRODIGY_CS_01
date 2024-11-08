Caesar Cipher 🔐
The Caesar Cipher is one of the earliest encryption techniques, named after Julius Caesar, who used it to secure his messages. This cipher shifts each letter in the alphabet by a set number of positions. For instance, with a shift of 3, ‘A’ becomes ‘D’, ‘B’ becomes ‘E’, and so forth. While simple, it laid the foundation for modern cryptography.

Table of Contents
Introduction
Algorithm
Rules
How to Run
Code
Example
Introduction
The Caesar Cipher involves shifting each letter in a message by a set amount. This method can be used for encryption and decryption. Though not suitable for modern security needs, it serves as a foundational exercise in cryptography.

Algorithm
Input:
Choose a shift value between 1 and 25.
Write down the alphabet in order from A to Z.
Shift the Alphabet:
Create a shifted alphabet by moving each letter in the original alphabet forward by the chosen shift value. For example, with a shift of 3:
mathematica
Copy code
Original alphabet: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Shifted alphabet:  D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
Encrypt or Decrypt:
Encryption: Replace each letter in the original message with its corresponding letter in the shifted alphabet.
Decryption: Shift each letter in the encrypted message backward by the same shift value.
Rules
Choose a shift value between 1 and 25.
To encrypt a message, shift each letter forward by the chosen value.
To decrypt, shift each letter back by the same value.
How to Run
Save the code in a file named caesar.py.
Open a command prompt or terminal and navigate to the directory where you saved the file.
Run the script by typing:
bash
Copy code
python caesar.py
Follow the prompts to enter the text, shift value, and select to either encrypt or decrypt.
Code
Here’s the Python code for the Caesar Cipher:

python
def caesar_cipher(message, shift_value, action='encrypt'):
    result_text = ""
    shift_value = shift_value if action == 'encrypt' else -shift_value

    for letter in message:
        if letter.isalpha():
            ascii_base = ord('A') if letter.isupper() else ord('a')
            shifted_char = chr((ord(letter) - ascii_base + shift_value) % 26 + ascii_base)
            result_text += shifted_char
        else:
            result_text += letter

    return result_text


    def main():
    print("Welcome to the Caesar Cipher Program!")
    action = input("Select action: (e)ncrypt or (d)ecrypt: ").lower()
    text = input("Enter the text: ")
    shift_value = int(input("Enter shift amount: "))

    if action == 'e':
        result = caesar_cipher(text, shift_value, 'encrypt')
    elif action == 'd':
        result = caesar_cipher(text, shift_value, 'decrypt')
    else:
        print("Invalid action selected.")
        return

    print(f"Output: {result}")


if __name__ == "__main__":
    main()
Example
With a shift value of 3:

Encryption: "hello" becomes "khoor"
Decryption: "khoor" reverts to "hello"
Try experimenting with different messages and shift values!
