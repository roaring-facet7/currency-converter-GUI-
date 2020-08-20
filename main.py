from tkinter import *
from currency_converter import *

def foreign_to_INR():
    screen1 = Tk()
    screen1.geometry("400x180")
    screen1.title("Convert a foreign currency to INR")
    
    Label(screen1, text = "Country Code: ").place(x=15, y=40)
    Label(screen1, text = "Value in that currency: ").place(x=15, y=80)

    code = StringVar(screen1)
    curr = StringVar(screen1)
    
    code_entry = Entry(screen1, textvariable = code, width = 30)
    curr_entry = Entry(screen1, textvariable = curr, width = 30)
    
    code_entry.place(x=100, y=40)
    curr_entry.place(x=140, y=80)

    submit = Button(screen1, text="Submit", width=10, height=1, command=lambda: foreign_to_INR_back(screen1, code, curr))
    submit.place(x = 100, y = 120)


def foreign_to_INR_back(screen1, code, curr):
    code_info = code.get()
    curr_info = float(curr.get())
    res = f_to_INR(code_info, curr_info)
    Label(screen1, text=str(res)).place(x=200, y=140)


def INR_to_foreign():
    screen2 = Tk()
    screen2.geometry("500x500")
    screen2.title("Convert INR to a foreign currency")

    Label(screen2, text = "Country Code: ").place(x=15, y=40)
    Label(screen2, text = "Value in INR currency: ").place(x=15, y=80)

    code = StringVar(screen2)
    curr = StringVar(screen2)
    
    code_entry = Entry(screen2, textvariable = code, width = 30)
    curr_entry = Entry(screen2, textvariable = curr, width = 30)
    
    code_entry.place(x=100, y=40)
    curr_entry.place(x=140, y=80)

    submit = Button(screen2, text="Submit", width=10, height=1, command=lambda: INR_to_foreign_back(screen2, code, curr))
    submit.place(x = 100, y = 120)


def INR_to_foreign_back(screen2, code, curr):
    code_info = code.get()
    curr_info = float(curr.get())
    res = INR_to_f(code_info, curr_info)
    Label(screen2, text=str(res)).place(x=200, y=140)    
   

def main():
    screen_main = Tk()
    screen_main.geometry("400x200")
    screen_main.title("Currency Converter")

    mssg = Label(text = "Choose one of the options")
    mssg.place(x = 100, y = 20)

    option1 = Button(screen_main, text="Convert INR to foreign Currency", width=50, height=2, bg="blue", command=INR_to_foreign)
    option2 = Button(screen_main, text="Convert foreign Currency to INR", width=50, height=2, bg="red", command=foreign_to_INR)

    option1.place(x = 20, y = 70)
    option2.place(x = 20, y = 120)

    screen_main.mainloop()

main()
