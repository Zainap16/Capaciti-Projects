import tkinter as tk

top = tk.Tk()
top.geometry('1100x600')

C = tk.Canvas(top, bg="blue", height=250, width=300)

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")

C.place(x=56, y=56)
top.mainloop()
