from tkinter import *

root = Tk()
root.title("Calculator?")
root.resizable(False, False)


field = Entry(root, width=20, font=("Segoe UI", 18), justify="right")
field.grid(row=0, column=0, columnspan=5, padx=8, pady=8)
field.focus_set()

def back_key():
    length = len(field.get())
    if length > 0:
        field.delete(length - 1, END)

def clear_key():
    field.delete(0,END)


def click(x):
    field.insert("end",x)
    field.icursor(END)
    field.xview_moveto(1)



button1 = Button(padx=20, pady=20, text="1",            command=lambda: click("1")); button1.grid(row=4, column=1)
button2 = Button(padx=20, pady=20, text="2",            command=lambda: click("2")); button2.grid(row=4, column=2)
button3 = Button(padx=20, pady=20, text="3",            command=lambda: click("3")); button3.grid(row=4, column=3)
button4 = Button(padx=20, pady=20, text="4",            command=lambda: click("4")); button4.grid(row=3, column=1)
button5 = Button(padx=20, pady=20, text="5",            command=lambda: click("5")); button5.grid(row=3, column=2)
button6 = Button(padx=20, pady=20, text="6",            command=lambda: click("6")); button6.grid(row=3, column=3)
button7 = Button(padx=20, pady=20, text="7",            command=lambda: click("7")); button7.grid(row=2, column=1)
button8 = Button(padx=20, pady=20, text="8",            command=lambda: click("8")); button8.grid(row=2, column=2)
button9 = Button(padx=20, pady=20, text="9",            command=lambda: click("9")); button9.grid(row=2, column=3)
button0 = Button(padx=50, pady=20, text="0",            command=lambda: click("0")); button0.grid(row=5, column=0, columnspan=3)
button_decimal = Button(padx=20, pady=20, text=".",     command=lambda: click(".")); button_decimal.grid(row=5, column=3)
button_divide = Button(padx=20, pady=20, text="/",      command=lambda: click("/")); button_divide.grid(row=1, column=3)
button_multiply = Button(padx=20, pady=20, text="x",    command=lambda: click("x")); button_multiply.grid(row=1, column=2)
button_minus = Button(padx=20, pady=20, text="-",       command=lambda: click("-")); button_minus.grid(row=2, column=4)
button_add = Button(padx=20, pady=20, text="+",         command=lambda: click("+")); button_add.grid(row=3, column=4)
button_equal = Button(padx=20, pady=50, text="=",       command=lambda: click("=")); button_equal.grid(row=4, column=4, rowspan=2)
button_clear = Button(padx=20, pady=20, text="C",       command=clear_key); button_clear.grid(row=1, column=1)
button_back = Button(padx=20, pady=20, text="<-",       command=back_key); button_back.grid(row=1, column=4)

root.bind("<BackSpace>", lambda event: back_key())

#KEYBINDS
def handle(d):
    click(d)
    return "break"   # prevent Entry’s default insert

# Digits (top row + numpad)
for i in range(10):
    field.bind(str(i),      lambda e, d=str(i): handle(d))
    field.bind(f"<KP_{i}>", lambda e, d=str(i): handle(d))

# Operators (top row + numpad)
field.bind("+",             lambda e: handle("+"))
field.bind("-",             lambda e: handle("-"))
field.bind("*",             lambda e: handle("x"))
field.bind("/",             lambda e: handle("/"))
field.bind("<KP_Add>",      lambda e: handle("+"))
field.bind("<KP_Subtract>", lambda e: handle("-"))
field.bind("<KP_Multiply>", lambda e: handle("x"))
field.bind("<KP_Divide>",   lambda e: handle("/"))

# Backspace: also stop default delete
field.bind("<BackSpace>",   lambda e: (back_key(), "break")[1])
root.bind("<Escape>",       lambda event: clear_key())


root.mainloop()


    