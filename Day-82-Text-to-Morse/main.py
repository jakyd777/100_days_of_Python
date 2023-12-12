# import necessary libraries
import decode_morse as morse

valid_answer = ['c', 'C', 'd', 'D']

# coding function
def code(text):
    coded_text = ""
    for letter in text:
        if letter != " ":
            if letter not in morse.MORSE_CODE_DICT:
                pass
            else:
                coded_letter = morse.MORSE_CODE_DICT[letter]
                coded_text += coded_letter
                coded_text += " "
        if letter == " ":
            coded_text += " "
        else:
            pass
    return coded_text


# decoding function
def decode(text):
    text += " "
    decoded_text = ""
    letter_to_decode = ""
    space = 0
    for char in text:
        if char not in [' ', '.', '-']:
            pass
        elif char != " ":
            letter_to_decode += char
            space = 0
        elif char == " ":
            if space == 1:
                decoded_text += " "
                space = 0
            else:
                decoded_letter = morse.DECODE_MORSE_DICT[letter_to_decode]
                decoded_text += decoded_letter
                letter_to_decode = ""
                space = 1
    return decoded_text


# start main program
def main():
    # Ask for input string
    ask_if_code = input('\nDo you want code text to morse code (press "C") or decode morse code to text (press"D"): ')
    if ask_if_code not in valid_answer:
        main()

    text_to_code = input("Please enter text for converting: ")
    if text_to_code == "":
        main()
    else:
        text_to_code = text_to_code.upper()

    if ask_if_code.upper() == "C":
        coded_text = code(text_to_code)
        print(coded_text)
    elif ask_if_code.upper() == "D":
        decoded_text = decode(text_to_code)
        print(decoded_text)

    wish_continue = input('Do you want continue press "Y" otherwise program will end: ')
    if wish_continue == "Y":
        main()


# run program
if __name__ == '__main__':
    main()