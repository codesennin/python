import pyautogui, time
import tkinter as tk
root = tk.Tk()
root.title("spambot")

def spam():
    time.sleep(5)
    f = open(entry.get(), 'r')
    for word in f:
        pyautogui.typewrite(word)
        time.sleep(0.5)
        pyautogui.press("enter")

label = tk.Label(root, text = 'Podaj nazwe pliku:', width=40)
label.pack()

entry = tk.Entry(root, width=20)
entry.pack()

button = tk.Button(text = 'Spamuj!', command=spam)
button.pack()

root.mainloop()