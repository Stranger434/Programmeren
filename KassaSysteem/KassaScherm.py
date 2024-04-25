from tkinter import *
 
# globally declare the expression variable 
CalculatorScreen = ""

 
 
# Function to update expression 
# in the text entry box 
def press(num): 
    global CalculatorScreen 
    CalculatorScreen = CalculatorScreen + str(num) 
    Uitkomst.set(CalculatorScreen) 
 
def equalpress(): 
    try: 
        global CalculatorScreen 
        global total
        total = str(eval(CalculatorScreen)) 
        Uitkomst.set(total)
        CalculatorScreen = "" 
    except:
        Uitkomst.set(" error ")
        CalculatorScreen = "" 
 

def clear(): 
    global CalculatorScreen 
    CalculatorScreen = "" 
    Uitkomst.set("") 

def ShowOnScreen():
    try:
        global CalculatorScreen 
        TeBetalen.set(total)
    except:
        TeBetalen.set('Berekening niet afgerond')

def WisselGeldfunc():
    try:
        te_betalen = float(TeBetalen.get())
        betaald = float(Betaald.get())
        wisselgeld = betaald - te_betalen
        if wisselgeld > 0:
            Wisselgeld.set("{:.2f}".format(wisselgeld))  # Zet het wisselgeld op twee decimalen
        elif wisselgeld == 0:
            Wisselgeld.set("Perfect")
        else:
            Wisselgeld.set("Krijg nog Geld van je")
    except ValueError:
        Wisselgeld.set("Ongeldige invoer")



if __name__ == "__main__":
    # Create the app's main window
    window = Tk()
    window.title("Kassa")

    # Gets screen size
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.geometry(f"{screen_width}x{screen_height}")
    # print(f"{screen_width}x{screen_height}")


    # Sets background color
    window.configure(background='gray')

    # Removes the window's title bar
    window.overrideredirect(True)

    Uitkomst = StringVar()
    TeBetalen = StringVar()
    Betaald = StringVar()
    Wisselgeld = StringVar()


    # Widgets
    stop = Button(window, text = 'Turn Screen Off!',command = window.destroy)
    Uitkomst_veld = Entry(window, textvariable=Uitkomst, state='disabled')
    Tebetalen_text = Label(window, text=' Te betalen ', relief=FLAT)
    Tebetalen_veld = Entry(window, textvariable=TeBetalen, state='disabled')
    Betaald_text = Label(window, text=' Hoeveel heeft de klant betaald ', relief=FLAT)
    Betaald_veld = Entry(window, textvariable=Betaald)
    Wisselgeld_text = Label(window, text=' Wisselgeld ', relief=FLAT)
    Wisselgeld_veld = Entry(window, textvariable=Wisselgeld, state='disabled')
    Wisselgeld_button = Button(window, text=' Calculate ', fg='black', bg='white', command=WisselGeldfunc)

    button1 = Button(window, text=' 1 ', fg='black', bg='white', 
                    command=lambda: press(1))
    button2 = Button(window, text=' 2 ', fg='black', bg='white', 
                    command=lambda: press(2))
    button3 = Button(window, text=' 3 ', fg='black', bg='white', 
                    command=lambda: press(3))
    button4 = Button(window, text=' 4 ', fg='black', bg='white', 
                    command=lambda: press(4))
    button5 = Button(window, text=' 5 ', fg='black', bg='white', 
                    command=lambda: press(5)) 
    button6 = Button(window, text=' 6 ', fg='black', bg='white', 
                    command=lambda: press(6))
    button7 = Button(window, text=' 7 ', fg='black', bg='white', 
                    command=lambda: press(7)) 
    button8 = Button(window, text=' 8 ', fg='black', bg='white', 
                    command=lambda: press(8)) 
    button9 = Button(window, text=' 9 ', fg='black', bg='white', 
                    command=lambda: press(9))
    button0 = Button(window, text=' 0 ', fg='black', bg='white', 
                    command=lambda: press(0))
    Clear = Button(window, text=' Clear ', fg='black', bg='Red', 
                   command=clear)
    Ok = Button(window, text=' Ok ', fg='black', bg='Green',
                command=ShowOnScreen
                    )
    equal = Button(window, text=' = ', fg='black', bg='light sky blue',
                command=equalpress,
                width=9, height=4)
    
    plus = Button(window, text=' + ', fg='black', bg='light sky blue',
                  command=lambda: press(" + "),
                  width=9, height=4
                    )
    Min = Button(window, text=' - ', fg='black', bg='light sky blue',
                   command=lambda: press(" - "),
                   width=9, height=4
                     )
    delen = Button(window, text=' : ', fg='black', bg='light sky blue',
                   command=lambda: press(" / "),
                   width=9, height=4
                     )
    Keer = Button(window, text=' x ', fg='black', bg='light sky blue',
                   command=lambda: press(" * "),
                   width=9, height=4
                     )
    komma = Button(window, text=' , ', fg='black', bg='light sky blue',
                   command=lambda: press("."),
                   width=9, height=4
                     )

    # Makes the Grid
    window.columnconfigure((0,1,2,3,4,5,6,7,8), weight = 1)
    window.rowconfigure((0,1,2,3,4,5,6,7,8), weight = 1)


    # Place Widgets
    stop.grid(row=8, column=8, ipadx=15, ipady=10)
    Uitkomst_veld.grid(row=1, column=5, columnspan=3, sticky=NSEW, padx=3, pady=5)
    Tebetalen_text.grid(row=0, column=1, sticky=SW, padx=3, pady=5)
    Tebetalen_veld.grid(row=1, column=1, columnspan=3, sticky=NSEW, padx=3, pady=2)
    Betaald_text.grid(row=2, column=1, sticky=SW, padx=3, pady=5)
    Betaald_veld.grid(row=3, column=1, columnspan=3, sticky=NSEW, padx=3, pady=2)
    Wisselgeld_text.grid(row=4, column=1, sticky=SW, padx=3, pady=5)
    Wisselgeld_veld.grid(row=5, column=1, columnspan=3, sticky=NSEW, padx=3, pady=2)
    Wisselgeld_button.grid(row=4, column=1, sticky=NW, padx=3, pady=5)

    button1.grid(row=2, column=5, sticky=NSEW, padx=2, pady=2)
    button2.grid(row=2, column=6, sticky=NSEW, padx=2, pady=2)
    button3.grid(row=2, column=7, sticky=NSEW, padx=2, pady=2)
    button4.grid(row=3, column=5, sticky=NSEW, padx=2, pady=2)
    button5.grid(row=3, column=6, sticky=NSEW, padx=2, pady=2)
    button6.grid(row=3, column=7, sticky=NSEW, padx=2, pady=2)
    button7.grid(row=4, column=5, sticky=NSEW, padx=2, pady=2)
    button8.grid(row=4, column=6, sticky=NSEW, padx=2, pady=2)
    button9.grid(row=4, column=7, sticky=NSEW, padx=2, pady=2)
    button0.grid(row=5, column=6, sticky=NSEW, padx=2, pady=2)
    Clear.grid(row=5, column=5, sticky=NSEW, padx=2, pady=2)
    Ok.grid(row=5, column=7, sticky=NSEW, padx=2, pady=2)
    plus.grid(row=2, column=8, sticky=NW, padx=2, pady=2)
    Min.grid(row=2, column=8, sticky=SW, padx=2, pady=2)
    delen.grid(row=3, column=8, sticky=NW, padx=2, pady=2)
    Keer.grid(row=3, column=8, sticky=SW, padx=2, pady=2)
    equal.grid(row=4, column=8, sticky=SW, padx=2, pady=2)
    komma.grid(row=4, column=8, sticky=NW, padx=2, pady=2)

    # Run the app's main loop    
    window.mainloop()


