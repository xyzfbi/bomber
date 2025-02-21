from tkinter import simpledialog
import tkinter as tk
import time
import keyboard
import pyperclip

root = tk.Tk()
root.withdraw()

x = simpledialog.askstring("Input", "Enter text to spam:")
f = int(simpledialog.askstring("Input", "Enter number of repetitions:"))

def spam(text: str, amount: int):
    pyperclip.copy(text)
    time.sleep(1)
    for _ in range(amount):
        time.sleep(0.1)
        keyboard.press_and_release("ctrl+v")
        keyboard.press_and_release("enter")

spam(x  , f)

print("Spamming completed!")
root.destroy()
