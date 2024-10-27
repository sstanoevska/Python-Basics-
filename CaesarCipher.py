from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(encode_or_decode, original_text, shift_amount):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            original_position = alphabet.index(letter)
            shifted_position = (original_position + shift_amount) % len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter

    print(f"Here is the {encode_or_decode}d result: {output_text}")


caesar(encode_or_decode=direction, original_text=text, shift_amount=shift)

should_continue=True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(encode_or_decode=direction, original_text=text, shift_amount=shift)
    restart=input("Type yes if you want to go again. Otherwise, type no.\n").lower()
    if restart=="no":
        should_continue=False
        print("Hope you had fun!")





