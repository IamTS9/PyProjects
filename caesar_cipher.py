alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encode(text, shift):
    new_text = ""
    i = 0
    for letter in text:
        if letter in alphabet:
            index_no = alphabet.index(letter)
            if index_no+shift > 25:
                n = int((index_no + shift) / 26) + 1
                new_text += alphabet[index_no + shift-(26*n)]
            else:
                new_text += alphabet[index_no+shift]
        else:
            new_text += letter
    print(new_text)


def decode(text, shift):
        new_text = ""
        i = 0
        for letter in text:
            if letter in alphabet:
                index_no = alphabet.index(letter)
                if index_no + shift > 25:
                    n = int(((index_no + shift )/26))+1
                    new_text += alphabet[index_no - shift - (26*n)]
                else:
                    new_text += alphabet[index_no - shift]
            else:
                new_text += letter

        print(new_text)


if direction == 'encode':
    print(encode(text, shift))
elif direction == 'decode':
    print(decode(text, shift))
else:
    print('Pls type encode or decode')

