# importing files
from tkinter import *
from tkinter import messagebox
from sorts import sorting_visualizer


root = Tk()
root.title("Gunjan Raj Tiwari")
root.geometry("500x360")

# calling sorting part
def visualize():
    try:
        N = int(entry1.get())
        method = var1.get()[0]
        data = var2.get()[0]
        speed = (11-entry4.get())**3
        sorting_visualizer(N, method, data, speed)

    except:
        messagebox.showwarning("Error!","Please fill valid data!")
    
# creating tkinter variables
var1 = StringVar(root)
var2 = StringVar(root)
var1.set('bubble')
var2.set('random')

# options
sorts = {'bubble','insertion','selection','merge','quick','heap'}
choices = {'random','sorted(nearly)','descending'}


# WIDGETS
# head
h1 = Label(root, 
    bg="#dd6666", 
    fg = "white", 
    padx=20, 
    pady=5, 
    font=("bold",20), 
    text="SORTING ALGORITHM VISUALIZER")

# input number of data
l1 = Label(root, text="Number of Values: ", font=12)

entry1 = Entry(root, font=10) 

# input sorting algorithm
l2 = Label(root, text="Sorting Algorithm: ", font=12)

entry2 = OptionMenu(root, var1, *sorts)
entry2.config(font=10)
root.nametowidget(entry2.menuname).config(font=10)

# input type of data
l3 = Label(root, text="Type of Data ", font=12)

entry3 = OptionMenu(root, var2, *choices)
entry3.config(font=10)
root.nametowidget(entry3.menuname).config(font=10)

# input speed of animation
l4 = Label(root, text="Speed of Animation: ", font=12)

entry4 = Scale(root, from_=1, to=10, orient=HORIZONTAL)

# visualizing button
btn = Button(root, 
    text="Visualize", 
    highlightbackground="#dd6666", 
    activebackground="#dd6666", 
    activeforeground="white",
    bg="#dd6666", 
    fg="white", 
    font=("bold",12), 
    relief=GROOVE, 
    command=visualize)

# Position of all widget

h1.grid(row=1,columnspan=4)

l1.grid(row=2,column=1)
l2.grid(row=3,column=1)
l3.grid(row=4,column=1)
l4.grid(row=5,column=1)

entry1.grid(row=2,column=2,pady=5, ipadx=4, ipady=4)
entry2.grid(row=3,column=2,pady=5, ipadx=4, ipady=4)
entry3.grid(row=4,column=2,pady=5, ipadx=4, ipady=4)
entry4.grid(row=5,column=2,pady=5, ipadx=4, ipady=4)

btn.grid(row=6,column=1, pady=10, ipadx=3, ipady=3)

root.mainloop()