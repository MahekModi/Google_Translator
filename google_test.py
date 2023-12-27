from tkinter import *
from tkinter import ttk  #ttk calls combobox
import googletrans
from googletrans import Translator, LANGUAGES

def change(text="type", src = "English", dest = "Gujarati"):
    text2 = text
    src2 = src
    dest2 = dest
    trans = Translator()
    # print("hey")
    trans2 = trans.translate(text, src = src2, dest = dest2)
    return trans2.text

def data():
    s = combo_src.get()
    d = combo_dest.get()
    msg = source_txt.get(1.0, END)
    textget = change(text = msg, src = s, dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END, textget)

screen = Tk()
screen.title("Translator")
screen.geometry("500x700")
screen.config(bg='lavender')

label_txt = Label(screen, text = "TRANSLATOR", font = ("Calibri", 40, "bold"), bg="Lavender")
label_txt.place(x=100, y=40, height=50, width=300)

frame = Frame(screen).pack(side=BOTTOM)

label_txt = Label(screen, text = "Source Text", font = ("Calibri", 30, "bold"), bg="Lavender", fg= "dark blue")
label_txt.place(x=100, y=105, height=30, width=300)

source_txt = Text(frame, font = ("Times New Roman", 20, "bold"), wrap = WORD)
source_txt.place(x=20, y=150, height=150, width=460)

list_text = list(LANGUAGES.values())

combo_src = ttk.Combobox(frame, value=list_text)
combo_src.place(x=20, y=315, height=40, width=140)
combo_src.set("English")

button = Button(frame, text = "Translate", relief=RAISED, command=data)
button.place(x=180, y=315, height=40, width=140)

combo_dest = ttk.Combobox(frame, value=list_text)
combo_dest.place(x=340, y=315, height=40, width=140)
combo_dest.set("English")

label_txt = Label(screen, text = "Destination Text", font = ("Calibri", 30, "bold"), bg="Lavender", fg= "dark Blue")
label_txt.place(x=100, y=370, height=30, width=300)

dest_txt = Text(frame, font = ("Times New Roman", 20, "bold"), wrap = WORD)
dest_txt.place(x=20, y=420, height=150, width=460)

screen.mainloop()