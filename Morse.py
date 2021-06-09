from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)


def dot():
    time.sleep(0.5)
    GPIO.output(4, True)
    time.sleep(0.5)
    GPIO.output(4, False)


def dash():
    time.sleep(0.5)
    GPIO.output(4, True)
    time.sleep(1.5)
    GPIO.output(4, False)


def charbreak():
    time.sleep(1.0)

def wordbreak():
    time.sleep(3.0)


MORSE_CODE_DICT = { 'A':'.-',
                    'B':'-...',
                    'C':'-.-.',
                    'D':'-..',
                    'E':'.',
                    'F':'..-.',
                    'G':'--.',
                    'H':'....',
                    'I':'..',
                    'J':'.---',
                    'K':'-.-',
                    'L':'.-..',
                    'M':'--',
                    'N':'-.',
                    'O':'---',
                    'P':'.--.',
                    'Q':'--.-',
                    'R':'.-.',
                    'S':'...',
                    'T':'-',
                    'U':'..-',
                    'V':'...-',
                    'W':'.--',
                    'X':'-..-',
                    'Y':'-.--',
                    'Z':'--..',
                    '1':'.----',
                    '2':'..---',
                    '3':'...--',
                    '4':'....-',
                    '5':'.....',
                    '6':'-....',
                    '7':'--...',
                    '8':'---..',
                    '9':'----.',
                    '0':'-----',
                    ', ':'--..--',
                    '.':'.-.-.-',
                    '?':'..--..',
                    '/':'-..-.',
                    '-':'-....-',
                    '(':'-.--.',
                    ')':'-.--.-'}


MORSE_TO_GPIO_DICT= {'.': 'dot(), ', '-': 'dash(), ', ' ': 'charbreak(), '}



def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '

    return cipher

def morse(cipher):
    morse = ''
    for symbol in cipher:
        morse += MORSE_TO_GPIO_DICT[symbol]
    morse = morse.replace(' charbreak(), charbreak(),', ' wordbreak(),')
    eval(morse)
    return morse



win = Tk()
win.title("Text To Morse")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")


def close(window):
    window.destroy()
    GPIO.cleanup()
    print("close")

def convert():
    global inputTxt
    Text = inputTxt.get()
    asMorse = encrypt(Text.upper())
    blink = morse(asMorse)


inputTxt = Entry(win, width=100)
inputTxt.pack()
inputTxt.focus_set()

sendButton = Button(win, text = 'Convert', font = myFont, command = convert, bg = 'white', height = 1, width = 24)
sendButton.pack(side= 'top')
closeButton = Button(win, text = 'Close', font = myFont, command = lambda: close(win), bg = 'white', height = 1, width = 24)
closeButton.pack(side = 'bottom')
