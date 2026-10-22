#Вариант 1
import tkinter as tk
import pygame
from keyGen import keyGeneration

def close():
    window.destroy()


def generate():
    key_field.configure(state='normal')
    key_field.delete(0, tk.END)
    key_field.insert(0, keyGeneration())
    key_field.configure(state='readonly')


colors = ['blue', 'red', 'green', 'orange', 'purple']
color_index = 0


def animate():
    global color_index
    lbl_title.configure(bg=colors[color_index])
    color_index = (color_index + 1) % len(colors)
    window.after(500, animate)


window = tk.Tk()
window.title('KeyGen')
window.geometry('500x500')
bg_img = tk.PhotoImage(file='bg_pic.png')
pygame.mixer.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')

lbl_title = tk.Label(frame, text='KEYGEN', font=('Arial', 30), bg='blue', fg='white')
lbl_title.grid(column=0, row=0, columnspan=2, padx=10, pady=15)

lbl_key = tk.Label(frame, text='Key:', font=('Arial', 14))
lbl_key.grid(column=0, row=1, padx=10, pady=15)
key_field = tk.Entry(frame, width=17, font=('Consolas', 16), state='readonly')
key_field.grid(column=1, row=1, padx=10, pady=15)

btn_generate = tk.Button(frame, text='Generate', command=generate)
btn_generate.grid(column=0, row=2, padx=10, pady=15)
btn_close = tk.Button(frame, text='Close', command=close)
btn_close.grid(column=1, row=2, padx=10, pady=15)

animate()
window.mainloop()