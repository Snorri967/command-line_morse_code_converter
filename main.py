import pyperclip
import winsound
import time

print('''
                                ___          _          ___                          _             
  /\/\   ___  _ __ ___  ___    / __\___   __| | ___    / _ \___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 /    \ / _ \| '__/ __|/ _ \  / /  / _ \ / _` |/ _ \  / /_\/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
/ /\/\ \ (_) | |  \__ \  __/ / /__| (_) | (_| |  __/ / /_\\  __/ | | |  __/ | | (_| | || (_) | |   
\/    \/\___/|_|  |___/\___| \____/\___/ \__,_|\___| \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                                   
''')

coding = True
while coding:

    text_to_morse_dict = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
        'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
        's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
        '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
        '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    }

    unit = 100  # ms
    frequency = 3000  # Hz

    def play_dot():
        winsound.Beep(600, 100)

    def play_dash():
        winsound.Beep(500, 200)


    morse_to_text_dict = {value: key for key, value in text_to_morse_dict.items()}

    choice = input("Do you want to 'encode' your text to morse code or 'decode' your morse code back into text?\n")


    def coding():
        if choice == 'encode':
            message_encyption = input("Your message can only include a-z, 0-9, periods, commas, question marks,"
                                      " apostrophes, exclamation marks, foward-slashes, open and close parenthesis,"
                                      " ambersands, colons, semi-colons, equals operators, plus operators,"
                                      " subtract operators, underscores, quotation marks, dollar signs,"
                                      " and at signs.\n")

            """ retrieves the morse code values from the letter keys in the message encryption input and splits 
            the code word for word. """

            morse_code = '  '.join([' '.join(text_to_morse_dict[character] for character in word) for word in
                                    message_encyption.lower().split(' ')])
            print(morse_code)
            pyperclip.copy(morse_code)
            print("Code added to clipboard")

            """ takes the morse code a and plays a sound at a different frequencey depending on if the code contains
            either a dot, a dash """
            morse_value = morse_code
            for x in morse_value:
                if x == '.':
                    play_dot()
                    time.sleep(1*unit/1000)
                elif x == '-':
                    play_dash()
                    time.sleep(1*unit/1000)
                else:
                    time.sleep(3*unit/1000)
            return morse_value

        elif choice == 'decode':
            message_decryption = input('Enter your morse code to be decrypted back into text.\n')

            """ retrieves the letter keys from the values in the message decryption input and splits the text
            word for word. """

            text = ' '.join([''.join([morse_to_text_dict[character] for character in word.split(' ')]) for word in
                             message_decryption.split('  ')])
            print(text)
            pyperclip.copy(text)
            print("Text added to clipboard")

    coding()

    run_again = input("Do you want to run the program again? Enter 'yes' or 'no'\n")
    if run_again == 'yes':
        coding = True
    else:
        print('Goodbye!')
        coding = False
