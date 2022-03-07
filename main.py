from tkinter import * 
root = Tk()
score = 0
canvas = Canvas(root, height=600, width=600, relief=RAISED, bg='brown')
canvas.grid() 
canvas.grid(row=0, column=1)
img = PhotoImage(file='C:/Users/15614/Desktop/swole_peep_simulator/Bench-press-1.png')
img2 = PhotoImage(file='C:/Users/15614/Desktop/swole_peep_simulator/Bench-press-2.png')
canvas.create_image(75, -50, image=img)
canvas.create_text(300, 50, text='SWOLE PEEP SIMULATOR!', font=0)
from tkinter import ttk


def key(event):
    global score
    canvas.create_image(300, 300, image=img2)
    score += 1
    canvas.itemconfig(score_text, text = score)


def callback(event):
    canvas.focus_set()


canvas.bind("a", key)
canvas.bind("<Button-1>", callback)
canvas.pack()


def key(event):
    canvas.create_image(300, 300, image=img)

canvas.bind("b", key)

score_text = canvas.create_text(50, 50, text= 'Score: ')  

root.mainloop()
