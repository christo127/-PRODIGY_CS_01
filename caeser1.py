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
