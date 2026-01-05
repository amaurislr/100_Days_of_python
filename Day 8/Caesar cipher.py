from itertools import repeat

alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]



def ceaser(original_text, shift_amount, encode_or_decode):
    chiper_text = ""

    if encode_or_decode == "decode":
            shift_amount *= -1

    for letter in original_text:
        shift_position = alfabeto.index(letter) + shift_amount
        shift_position %= len(alfabeto)
        chiper_text += alfabeto[shift_position]
    print(F"Here is the {encode_or_decode}d result: {chiper_text}")




finis_loop = False
while not finis_loop:
    direction = input("type 'enconde' to encrypt, type 'decode' to decrypt:").lower()
    text = input ("Type your message: ").lower()
    shift = int(input("Type the shift number:"))
    ceaser(original_text=text, shift_amount=shift, encode_or_decode=direction)
    repeat_1 = input("type 'Yes' is you want to go again. Otherwise type 'No' ").lower()

    if repeat_1 == "no":
        finis_loop = True
        print("GoodBye")