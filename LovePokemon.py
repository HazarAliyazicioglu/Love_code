from tkinter import *
from tkinter import messagebox

def click():
    messagebox.showinfo(title="I LOVE YOU", message="I LOVE YOU SOOOOO MUCH  💖💗💕❤️")


window = Tk()
window.geometry("720x720")
canvas = Canvas(window,height=600,width=600)
canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
canvas.create_arc(500,500,0,0,fill="white",extent=180,start=180,width=10)
oval = canvas.create_oval(190,190,310,310,fill="white",width=10)
Button(window,text="Click",command=click).place(x=360,y=370)
canvas.place(x=130,y=130)
window.mainloop()