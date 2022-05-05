'''
Subway Order Process
Caitlin Moenich
v3.0
4/14/22
'''

#getattr()




import tkinter as tk
from tkinter import *
from tkinter import ttk 
root = Tk()

meatList = []
veggieList = []
sauceList = []

size = StringVar()
bread = StringVar()
meat = StringVar()
cheese = StringVar()
toast = StringVar()
veggie = StringVar()
saucy = StringVar()



#first window construction
root.geometry('700x500')
root.resizable(0,0)
root.title("Subway Order")
begin = Label(text = "Hello! Would you like to order from Subway?").grid()
subway = PhotoImage(file="Subway.png")
logo = Label(root, image=subway).grid()
altLogo = Label(root, text= "Subway logo").grid(row = 2)
start = Button(root,#button lets user begin to enter their order
                text = "Start",
                bg = 'light green',
                fg= 'black',
                command = lambda:[orderWindow(), disableStart()])
start.grid()
cancel = Button(root, 
                text = 'Cancel Order',
                bg= 'red',
                fg= 'white',
                command =root.destroy).grid()

#disables start button as soon as user clicks it
def disableStart():
    if start["state"] == "normal":
        start["state"] = "disabled"
#group of functions add selections to list to print on second window
def sandySize():
    sandy = size.get()
    meatList.append(sandy)
    return meatList
def breadType():
    sandy = bread.get()
    meatList.append(sandy)
    return meatList
def valueToast():
    sandy = toast.get()
    meatList.append(sandy)
    return meatList
def valueMeat():
    sandy = meat.get()
    meatList.append(sandy)
    return meatList
def valueCheese():
    sandy = cheese.get()
    meatList.append(sandy)
    return meatList
def valueVeggie():
    sandy = veggie.get()
    veggieList.append(sandy)
    veggieList.append(',')
    return veggieList
def valueSauce():
    sandy = saucy.get()
    sauceList.append(sandy)
    sauceList.append(',')
    return sauceList



#first part of the order window
def orderWindow():  #First window. User puts in the size, meat, cheese, and if they want it toasted part of the order
    #Bread Choice
    sizeLabel = Label(text = "What size sandwich would you like?").grid()
    R1 = Radiobutton(root, text="6-inch", value = "6-inch", variable = size, command = sandySize)  #User selects one of two size options
    R1.grid(row=6, sticky=W)
    R2 = Radiobutton(root, text="Footlong", value="Footlong", variable = size, command = sandySize)
    R2.grid(row=6, sticky=E)

    breadLabel = Label(text = "What type of bread would you like?").grid()
    brd1 = Radiobutton(root, text="Italian", value="Italian", variable = bread, command = breadType)
    brd1.grid(row=8, sticky=E)
    brd2 = Radiobutton(root, text="Monterey Cheddar", value="Monterey Cheddar", variable = bread, command = breadType)
    brd2.grid(row=8, sticky=N)
    brd3 = Radiobutton(root, text="9-Grain Wheat", value="9-Grain Wheat", variable = bread, command = breadType)
    brd3.grid(row=8, sticky=W)
    brd4 = Radiobutton(root, text="Flatbread", value="Flatbread", variable = bread, command = breadType)
    brd4.grid(row=9, sticky=E)
    brd5 = Radiobutton(root, text="Herbs and Cheese", value="Herbs and Cheese", variable = bread, command = breadType)
    brd5.grid(row=9, sticky=N)
    brd6 = Radiobutton(root, text="Honey Oat", value="Honey Oat", variable = bread, command = breadType)
    brd6.grid(row=9, sticky=W)

    #Meat Choice
    whichMeat =Label(text= "What meat choice would you like on your sandwich?").grid()
    mt1 = Radiobutton(root, text="No Meat", value="No Meat", variable = meat, command = valueMeat)
    mt1.grid(row=11, sticky=E)
    mt2 = Radiobutton(root, text="Ham", value="Ham", variable = meat, command = valueMeat)
    mt2.grid(row=11, sticky=N)
    mt3 = Radiobutton(root, text="Turkey", value="Turkey", variable = meat, command = valueMeat)
    mt3.grid(row=11, sticky=W)
    mt4 = Radiobutton(root, text="Chicken Breast", value="Chicken Breast", variable = meat, command = valueMeat)
    mt4.grid(row=12, sticky=E)
    mt5 = Radiobutton(root, text="Roast Beef", value="Roast Beef", variable = meat, command = valueMeat)
    mt5.grid(row=12, sticky=N)
    mt6 = Radiobutton(root, text="Tuna", value="Tuna", variable = meat, command = valueMeat)
    mt6.grid(row=12, sticky=W)
    mt7 = Radiobutton(root, text="Salami", value="Salami", variable = meat, command = valueMeat)
    mt7.grid(row=13, sticky=E)
    mt8 = Radiobutton(root, text="Shaved Steak", value="Shaved Steak", variable = meat, command = valueMeat)
    mt8.grid(row=13, sticky=N)
    mt9 = Radiobutton(root, text="Bacon", value="Bacon", variable = meat, command = valueMeat)
    mt9.grid(row=13, sticky=W)
    mt10 = Radiobutton(root, text="Meatballs", value="Meatballs", variable = meat, command = valueMeat)
    mt10.grid(row=14, sticky=E)
    mt11 = Radiobutton(root, text="Pepperoni", value="Pepperoni", variable = meat, command = valueMeat)
    mt11.grid(row=14, sticky=N)
    mt12 = Radiobutton(root, text="Bologna", value="Bologna", variable = meat, command = valueMeat)
    mt12.grid(row=14, sticky=W)


    #Cheese Choice
    whatCheese = tk.Label(text= "What kind of cheese would you like?").grid(column = 2, row =1)
    chs1 = Radiobutton(root, text="No Cheese", value="No Cheese", variable = cheese, command = valueCheese)
    chs1.grid(column = 2, row=2, sticky=E)
    chs2 = Radiobutton(root, text="American", value="American", variable = cheese, command = valueCheese)
    chs2.grid(column = 2, row=2, sticky=N)
    chs3 = Radiobutton(root, text="Provolone", value="Provolone", variable = cheese, command = valueCheese)
    chs3.grid(column=2, row=2, sticky=W)
    chs4 = Radiobutton(root, text="Pepper Jack", value="Pepper Jack", variable = cheese, command = valueCheese)
    chs4.grid(column = 2, row=3, sticky=E)
    chs5 = Radiobutton(root, text="Shredded", value="Shredded", variable = cheese, command = valueCheese)
    chs5.grid(column= 2, row=3, sticky=W)
    
    #Toasted?
    willToast =Label(text = "Would you like it toasted?").grid(column = 2, row = 4)
    toast1 = Radiobutton(root, text="Yes", value = "Toasted", variable = toast, command = valueToast)
    toast1.grid(column = 2, row = 5, sticky=NW)
    toast2 = Radiobutton(root, text="No", value="Not Toasted", variable =toast, command = valueToast)
    toast2.grid(column =2, row= 5, sticky=NE)

    #vegetables
    vegetablesOrder = Label(text = "What vegetables would you like on your sandwich?").grid(row=6, column=2)#checkboxes of different ingredients for user to select
    vege1 = Checkbutton(root, text = 'Lettuce', variable = veggie, onvalue = 'Lettuce',offvalue=1, command=valueVeggie).grid(row=7, column=2, sticky=W) 
    vege2 = Checkbutton(root, text = 'Cucumber',variable = veggie, onvalue = 'Cucumber',offvalue=1, command=valueVeggie).grid(row=7, column=2, sticky=N)
    vege3 = Checkbutton(root, text = 'Tomato',variable = veggie, onvalue = 'Tomato',offvalue=0, command=valueVeggie).grid(row=7, column=2, sticky=E)
    vege4 = Checkbutton(root, text = 'Black Olive',variable = veggie, onvalue = 'Black Olive',offvalue=0, command=valueVeggie).grid(row=8, column=2, sticky=W)
    vege5 = Checkbutton(root, text = 'Onion',variable = veggie, onvalue = 'Onion',offvalue=0, command=valueVeggie).grid(row=8, column=2, sticky=N)
    vege6 = Checkbutton(root, text = 'Banana Pepper',variable = veggie, onvalue = 'Banana Pepper',offvalue=0, command=valueVeggie).grid(row=8, column=2, sticky=E)
    vege7 = Checkbutton(root, text = 'Green Pepper',variable = veggie, onvalue = 'Green Pepper',offvalue=0, command=valueVeggie).grid(row=9, column=2, sticky=W)
    vege8 = Checkbutton(root, text = 'Jalapeno',variable = veggie, onvalue = 'Jalapeno',offvalue=0, command=valueVeggie).grid(row=9, column=2, sticky=N)
    vege9 = Checkbutton(root, text = 'Pickle', variable = veggie, onvalue = 'Pickle',offvalue=0, command=valueVeggie).grid(row=9, column=2, sticky=E)
    saucesOrder = Label(text = "What sauce would you like on your sandwich?").grid(row=10, column=2)  #Sauce selection start
    sauce1 = Checkbutton(root, text = 'Mayo', variable = saucy, onvalue = 'Mayo',offvalue=0, command=valueSauce).grid(row=11, column=2, sticky=W)
    sauce2 = Checkbutton(root, text = 'Lite Mayo',variable = saucy, onvalue = 'Lite Mayo',offvalue=0, command=valueSauce).grid(row=11, column=2, sticky=E)
    sauce3 = Checkbutton(root, text = 'Mustard',variable = saucy, onvalue = 'Mustard',offvalue=0, command=valueSauce).grid(row=12, column=2, sticky=W)
    sauce4 = Checkbutton(root, text = 'Brown Mustard',variable = saucy, onvalue = 'Brown Mustard',offvalue=0, command=valueSauce).grid(row=12, column=2, sticky=E)
    sauce5 = Checkbutton(root, text = 'Olive Oil', variable = saucy, onvalue = 'Olive Oil',offvalue=0, command=valueSauce).grid(row=13, column=2, sticky=W)
    sauce6 = Checkbutton(root, text = 'Vinegar',variable = saucy, onvalue = 'Vinegar',offvalue=0, command=valueSauce).grid(row=13, column=2, sticky=E)
    sauce7 = Checkbutton(root, text = 'Honey Mustard',variable = saucy, onvalue = 'Honey Mustard',offvalue=0, command=valueSauce).grid(row=14, column=2, sticky=W)
    sauce8 = Checkbutton(root, text = 'Ranch',variable = saucy, onvalue = 'Ranch',offvalue=0, command=valueSauce).grid(row=14, column=2, sticky=E)
    sauce9 = Checkbutton(root, text = 'Sweet Onion Sauce',variable = saucy, onvalue = 'Sweet Onion Sauce',offvalue=0, command=valueSauce).grid(row=15, column=2, sticky=W)
    sauce10 = Checkbutton(root, text = 'Chipotle Sauce',variable = saucy, onvalue = 'Chipotle Sauce',offvalue=0, command=valueSauce).grid(row=15, column=2, sticky=E)
    finishOrder= Button(root,     #button takes user to the order confirmation window
                text = "Go to Confirmation",
                bg= 'light green',
                fg= 'black',
                command =lambda:[root.withdraw(), printSelection(meatList,veggieList,sauceList)]) #hides order window and opens the new window
    finishOrder.grid(row=16, column= 2)
#function opens new window to print reciept
def printSelection(meatList,veggieList,sauceList):  
    newWindow = Toplevel(root)  #creates new window
    newWindow.title("Order Confirmation")
    newWindow.geometry('550x400')
    newWindow.resizable(0,0)
    Label(newWindow,
            text = "Here is your order: ").grid(column=2)
    Label(newWindow, text = meatList).grid(column = 2)
    Label(newWindow, text = veggieList).grid(column = 2)
    Label(newWindow, text = sauceList).grid(column = 2)
    submitOrder= Button(newWindow,     #button ends program as if user submitted the order
                text = "Submit!",
                bg = 'light green',
                fg = 'black',
                command = root.destroy)
    submitOrder.grid(column = 2, row = 5, sticky = W)
    fixOrder = Button(newWindow,
                text = "Return to Order Screen",   #button brings back order window and kills the top level window for editing the order
                bg = 'yellow',
                fg = 'black',
                command = lambda:[root.deiconify(), newWindow.destroy()]).grid(column = 2, row = 5, sticky = E)
    sandwich = PhotoImage(file="sandwich.jpeg") 
    yum=Label(newWindow,image=sandwich).grid(column = 2)
    altYum = Label(newWindow, text= "Sandwich Examples").grid(column = 2)
    newWindow.mainloop()

root.mainloop()
