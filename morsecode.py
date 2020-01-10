from tkinter import *
from tkinter import ttk
import tkinter as tk
from ttkthemes import themed_tk as tk

root=tk.ThemedTk()
root.get_themes()
root.set_theme("plastik")
root.title("Morse code encrypter and decryptor")
root.geometry("200x200")
tkvar=StringVar(root)
mode=["encrypt","decrypt"]
tkvar.set('Choose One')
popupMenu= OptionMenu(root,tkvar,*mode)
Label(root,text="choose a mode").grid(row=4,column=0)
popupMenu.grid(row=5,column =0)
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '
    return cipher
#
# # Function to decrypt the string
# # from morse to english
def decrypt(message):

    # extra space added at the end to access the
    # last morse code
    message += ' '

    decipher = ''
    citext = ''
    for letter in message:

        # checks for space
        if (letter != ' '):

            # counter to keep track of space
            i = 0

            # storing morse code of a single character
            citext += letter

        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2 :

                 # adding space to separate words
                decipher += ' '
            else:

                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''

    return decipher
def type():
    message=entry.get()
    if tkvar.get()=='encrypt':
        result = encrypt(message.upper())
        label1=ttk.Label(root, text=f"{result}")
        label1.grid(row=10,column=0)
        button2 = ttk.Button(root, text="Clear",command=lambda : clear_widget_text(label1))
        button2.grid(row=10,column=2)
    elif tkvar.get()=='decrypt':
        result = decrypt(message)
        label1=ttk.Label(root, text=f"{result}")
        label1.grid(row=10,column=0)
        button2 = ttk.Button(root, text="Clear",command=lambda : clear_widget_text(label1))
        button2.grid(row=10,column=2)
def clear_widget_text(widget):
    widget['text'] = ""
label=ttk.Label(root,text="Enter word:")
label.grid(row=0,column=0, sticky="W")
entry=ttk.Entry(root)
entry.grid(row=1,column=0)
button=ttk.Button(root,text="Perform",command=type)
button.grid(row=1,column=2)

root.mainloop()
# Executes the main function
