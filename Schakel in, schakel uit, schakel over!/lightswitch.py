import tkinter as tk

# schijf hier tussen je code
def knop():
    if button['text'] == 'Switch light ON':
        window.config(bg='yellow')
        print('Light is On')
        button['text'] = 'Switch light OFF'
    else:
        window.config(bg='black')
        print('Light is Off')
        button['text'] = 'Switch light ON'

window = tk.Tk()
window.config(bg='black')
button = tk.Button(text='Switch light ON', bg="white", fg="black", command=knop)
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code

window.mainloop()