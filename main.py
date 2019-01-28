import tkinter as tk

window=tk.Tk()
window.title("Tk Converter")
        
#choice_dict = {conversion type : (from unit, to unit, multiplier)}
#add more conversion options by just expanding the dictionary
choice_dict = {' km --> mi ' : ('km', 'mi', 0.621371),
               '  m --> ft ' : ('m ', 'ft', 3.28084),
               ' cm --> in ' : ('cm', 'in', 0.393701)}
clear_choice = 'select type'

def clear():
    # clear conversion type dropdown
    choice = clear_choice
    from_unit = to_unit = mult = '   '
    tkvar.set(choice)

    # clear entry box and label
    e2_label = tk.Label(window, text=from_unit)
    e2_label.grid(row=0, column=0, padx=10)
    e2.delete(0, tk.END)

    # clear output box and label
    t1_label = tk.Label(window, text=to_unit)
    t1_label.grid(row=0, column=4, padx=10, pady=5)
    t1.delete("1.0", tk.END)
 
def change_dropdown(*args):
    choice = tkvar.get()
    if choice != clear_choice:
        from_unit, to_unit, mult = choice_dict[choice]

        # update entry units per new choice
        e2_label = tk.Label(window, text=from_unit)
        e2_label.grid(row=0, column=0, padx=5)

        # update output units per new choice
        t1_label = tk.Label(window, text=to_unit)
        t1_label.grid(row=0, column=4, padx=10, pady=5)

        convert()

def convert():
    choice = tkvar.get()
    if choice != clear_choice:
        from_unit, to_unit, mult = choice_dict[choice]
        from_value = e2_value.get()
        
        if from_value != '':
                t1.delete("1.0", tk.END)
                to_value = float(from_value) * mult
                t1.insert(tk.END, to_value)

if __name__ == "__main__":
    choices = choice_dict.keys()

    # entry box for value to be converted
    e2_value = tk.StringVar()
    e2 = tk.Entry(window, font=("Calibri",10), textvariable=e2_value)
    e2.grid(row=0, column=1)

    # text output of converted results
    t1 = tk.Text(window, font=("Calibri",10), height=1, width=20)
    t1.grid(row=0, column=3)
    
    # pulldown menu to select conversion type
    tkvar = tk.StringVar(window)
    clear()
    popupMenu = tk.OptionMenu(window, tkvar, *choices)
    popupMenu.grid(row=0, column=2, padx=10, pady=5)    
    tkvar.trace('w', change_dropdown)

    # button to convert (if entry added after conversion type selected)
    b1 = tk.Button(window, text="Convert", command=convert)
    b1.grid(row=2, column=3, padx=10, pady=5)

    # button to clear everything
    b2 = tk.Button(window, text="Clear", command=clear)
    b2.grid(row=2, column=1, padx=10, pady=5)

    window.mainloop()
