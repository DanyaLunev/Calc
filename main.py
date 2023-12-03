from tkinter import *
from tkinter import ttk

calc = Tk()
calc.title("Калькулятор")
calc.iconbitmap(default="icon.ico")
calc.geometry("450x450")
calc.minsize(450, 450)
calc.maxsize(450, 450)

# Logic
def removeAll():
    answ.set("0")

def findRes(val):
    if "." not in val:
        if "+" in val:
            temp = val.split("+")
            return(str(int(temp[0]) + int(temp[1])))
        if "-" in val:
            temp = val.split("-")
            return(str(int(temp[0]) - int(temp[1])))
        if "*" in val:
            temp = val.split("*")
            return(str(int(temp[0]) * int(temp[1])))
        if "/" in val:
            temp = val.split("/")
            return(str(int(temp[0]) / int(temp[1])))
            print(temp)
    else:
        if "+" in val:
            temp = val.split("+")
            return(str(float(temp[0]) + float(temp[1])))
        if "-" in val:
            temp = val.split("-")
            return(str(float(temp[0]) - float(temp[1])))
        if "*" in val:
            temp = val.split("*")
            return(str(float(temp[0]) * float(temp[1])))
        if "/" in val:
            temp = val.split("/")
            return(str(float(temp[0]) / float(temp[1])))
            print(temp)

def clickOnBtn(event):
    button_text = event.widget.cget('text')
    if button_text != "=":
        if answ.get() == "0":
            answ.set(button_text)
        else:
            answ.set(answ.get() + button_text)
    else:
        answ.set(findRes(answ.get()))

# Title
frameTitle = ttk.Frame(padding=10)

label = ttk.Label(frameTitle, text="Калькулятор", font=("Arial", 20))
label.pack()

frameTitle.pack(anchor="n", fill=X, padx=25, pady=35)


# Answer
answ = StringVar()
answ.set("0")

frameAnsw = ttk.Frame(borderwidth=1, relief=SOLID, padding=8)

# Grid
for c in range(4): frameAnsw.columnconfigure(index=c, weight=1)
for r in range(1): frameAnsw.rowconfigure(index=r, weight=1)

# Delete Button
c = ttk.Button(frameAnsw, text="C", command=removeAll)
c.grid(row=0, column=0, ipadx=6, ipady=6, padx=4, pady=4)

# Answer field
labelAnsw = ttk.Label(frameAnsw, textvariable=answ, font=("Arial", 14))
labelAnsw.grid(row=0, column=1, columnspan=3, ipadx=6, ipady=6, padx=4, pady=4)

frameAnsw.pack(anchor="e", fill=X, padx=25, pady=15)


# Buttons
btncount = 1
btndo = ["/", "*", "-"]
btnlast = [".", "0", "=", "+"]

frameCalc = ttk.Frame(borderwidth=1, relief=SOLID, padding=8)

for c in range(4): frameCalc.columnconfigure(index=c, weight=1)
for r in range(4): frameCalc.rowconfigure(index=r, weight=1)

for r in range(4):
    for c in range(4):
        if r != 3:
            if c != 3:
                btn = ttk.Button(frameCalc, text=f"{btncount}")
                btn.bind('<Button>', clickOnBtn)
                btn.grid(row=r, column=c, ipadx=6, ipady=6, padx=4, pady=4)
                btncount += 1
            else:
                btn = ttk.Button(frameCalc, text=f"{btndo[0]}")
                btn.bind('<Button>', clickOnBtn)
                btn.grid(row=r, column=c, ipadx=6, ipady=6, padx=4, pady=4)
                btndo.pop(0)
        else:
            btn = ttk.Button(frameCalc, text=f"{btnlast[0]}")
            btn.bind('<Button>', clickOnBtn)
            btn.grid(row=r, column=c, ipadx=6, ipady=6, padx=4, pady=4)
            btnlast.pop(0)

frameCalc.pack(anchor="s", fill=X, padx=25, pady=15)

calc.mainloop()