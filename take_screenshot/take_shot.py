import pyautogui as auto
import tkinter as tk

from tkinter import filedialog
root=tk.Tk()
can=tk.Canvas(root,width=200,height=100)
can.pack()
screen=auto.screenshot()
def screenshort():
     
     file_path=filedialog.asksaveasfilename(defaultextension=".png")
     screen.save(file_path)

button=tk.Button(text="teke a shot",command=screenshort,bg='black',fg='white',font=10)
can.create_window(100,50,window=button)

root.mainloop()
