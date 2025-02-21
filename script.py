from tkinter import simpledialog
import tkinter as tk
import time
import pyperclip
from pynput.keyboard import Controller

root = tk.Tk()
root.withdraw()

x = simpledialog.askstring("Input", "Enter text to spam:")
f = int(simpledialog.askstring("Input", "Enter number of repetitions:"))

keyboard = Controller()

def spam(text: str, amount: int):
    pyperclip.copy(text)
    time.sleep(1)
    for _ in range(amount):
        time.sleep(0.2)
        keyboard.press('v')
        keyboard.release('v')
        keyboard.press('\n')
        keyboard.release('\n')

spam(x, f)

print("Spamming completed!")

keyboard._controller.stop()
root.destroy()vv