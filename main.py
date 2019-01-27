import tkinter as tk

window=tk.Tk()
    
def from_kg():
    miles = float(e2_value.get()) * 0.621371
    t1.delete("1.0", tk.END)
    t1.insert(tk.END, miles)

    feet = float(e2_value.get()) * 3280.84
    t2.delete("1.0", tk.END)
    t2.insert(tk.END, feet)

    inches = float(e2_value.get()) * 39370.1
    t3.delete("1.0", tk.END)
    t3.insert(tk.END, inches)

def clear():
    e2.delete(0, tk.END)
    t1.delete("1.0", tk.END)
    t2.delete("1.0", tk.END)
    t3.delete("1.0", tk.END)
    
e2_label = tk.Label(window, text="km")
e2_value = tk.StringVar()
e2 = tk.Entry(window, textvariable=e2_value)
e2_label.grid(row=0, column=0, padx=10)
e2.grid(row=0, column=1)

b1 = tk.Button(window, text="-->", command=from_kg)
b1.grid(row=0, column=2, padx=10)

b2 = tk.Button(window, text="Clear", command=clear)
b2.grid(row=2, column=0, padx=10)

t1 = tk.Text(window, height=1, width=20)
t1_label = tk.Label(window, text="miles")
t1.grid(row=0, column=3)
t1_label.grid(row=0, column=4, padx=10, pady=10)

t2=tk.Text(window, height=1, width=20)
t2_label = tk.Label(window, text="feet")
t2.grid(row=1,column=3)
t2_label.grid(row=1, column=4, padx=10)

t3 = tk.Text(window, height=1, width=20)
t3_label = tk.Label(window, text="inches")
t3.grid(row=2, column=3)
t3_label.grid(row=2, column=4, padx=10, pady=10)

window.mainloop()