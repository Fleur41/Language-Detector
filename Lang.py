'''
Language Detector
-------------------------------------------------------------
pip install langdetect
'''

from langdetect import detect
import tkinter as tkinter

def detect_lang():
    window = tk.Tk()
    window.geometry('600x400')
    head = tk.Label(window, text='Language Detector', font=('Calibri 15'))
    head.pack(pady=20)

    def check_language():