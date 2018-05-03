from tkinter import *

root = Tk()
root.title("Blood Management System")


lb_1 = Label(root, font=('arial', 40, 'bold'), text="Blood Management System", fg="Steel Blue",anchor=CENTER)
lb_1.grid(row=0, column=0)
def del1():
    flag = 1
    data = ""
    ln = "\n"

    try:
        file5 = open("D:/python/blood.txt", 'r+')
        data = ""
        while (flag != 0):
            str1 = file5.readline()
            k = str1.split()

            plate = str(text_50.get())

            if (plate == k[0]):

                flag = 0
                text_50.delete(0, END)



            else:

                data = data + str1

        str3 = file5.read()
        data = data + str3



    except:
        print("Error")
    file5.close()
    file2 = open("D:/python/blood.txt", 'w')
    file2.write(data)
    file2.close()

def search1():

    handle=Toplevel(root,width=1200)
    flag = 1
    data = ""
    ln = "\n"

    try:
        file1 = open("D:/python/blood.txt", 'r+')
        data = ""
        str1 = file1.readlines()
        str2=""



        plate = str(text_7.get())

        for i in str1:
            j=i.split()
            if(j[1]==plate):
                str2=str2+i
            print(str2)

            lab = Label(handle, text=str2)
            lab.grid(row=0, column=1)
            text_7.delete(0, END)






    except:
        print("Error")
    file1.close()
def next1():
    flag = 1
    data = ""
    ln = "\n"
    handle = Toplevel(root, width=1200)
    try:
        file1 = open("D:/python/blood.txt", 'r+')
        data = ""
        a=0
        while (flag != 0):
            str1 = file1.readline()
            k = str1.split()

            plate = str(text_6.get())
            if(a==1):
                lab = Label(handle, text=str1)
                lab.grid(row=0, column=1)
                text_6.delete(0, END)
                flag=0

            if (plate == k[0]):

                a=1








    except:
        print("Error")
    file1.close()
def prev1():
    flag = 1
    data = ""
    st=""
    ln = "\n"
    handle = Toplevel(root, width=1200)
    try:
        file1 = open("D:/python/blood.txt", 'r+')
        data = ""
        a=0
        prevstr=""
        while (flag != 0):
            str1 = file1.readline()
            k = str1.split()

            plate = str(text_6.get())




            print(st)
            if (plate == k[0]):

                prevstr=str1
                a=1
            if(a==0):
                st=str1

            if (prevstr != ""):
                flag = 0


                lab = Label(handle, text=st)
                lab.grid(row=0, column=1)
                text_6.delete(0, END)















    except:
        print("Error")
    file1.close()

def first():
    handle = Toplevel(root, width=1200)
    try:
        file1 = open("D:/python/blood.txt", 'r+')
        str1 = file1.readline()
        lab = Label(handle, text=str1)
        lab.grid(row=0, column=1)
        text_7.delete(0, END)



    except:
        print("Error")
    file1.close()
def last():
    handle = Toplevel(root, width=1200)
    try:
        file1 = open("D:/python/blood.txt", 'r+')
        str1 = file1.readlines()
        s=""
        for i in str1:
            s=i
        lab = Label(handle, text=s)
        lab.grid(row=0, column=1)
        text_7.delete(0, END)



    except:
        print("Error")
    file1.close()



lb_7 = Label(root, font=('arial', 16, 'bold'), text="Search By Blood", bd=16,anchor=E)
lb_7.grid(row=1, column=0,sticky=W)
text_7 = Entry(root, font=('arial', 16, 'bold'), bd=3, bg="Powder blue")
text_7.grid(row=1, column=0)

b5 = Button(root, text="Search", width=7, font="arial",bg="Green",command=search1).grid(row=2, column=0,padx=(0,0))

lb_50 = Label(root, font=('arial', 16, 'bold'), text="Delete Record", bd=16,anchor=E)
lb_50.grid(row=3, column=0,sticky=W)
text_50 = Entry(root, font=('arial', 16, 'bold'), bd=3, bg="Powder blue")
text_50.grid(row=3, column=0)
b4 = Button(root, text="Delete", width=10, font="arial",bg="red",command=del1)
b4.grid(row=4, column=0)


lb_2 = Label(root, font=('arial', 16, 'bold'), text="Donar Name", bd=16, anchor=E)
lb_2.grid(row=5, column=0, sticky=W)
text_2 = Entry(root, font=('arial', 16, 'bold'), bd=3, bg="Powder blue")
text_2.grid(row=5, column=0)
var = IntVar()
var1 = IntVar()
lb_3 = Label(root, font=('arial', 16, 'bold'), text="Blood Group", bd=16, anchor="w")
lb_3.grid(row=6, column=0, sticky=W)
choices = {'A+', 'A-', 'AB+', 'AB-', 'O+', 'O-', 'B+', 'B-'}
tkvar = StringVar(root)
tkvar.set('A+')  # set the default option

popupMenu = OptionMenu(root, tkvar, *choices)
Label(root).grid(row=6, column=0,padx=(10,0))
popupMenu.grid(row=6, column=0,padx=(0,10))

lb_4 = Label(root, font=('arial', 16, 'bold'), text="Date", bd=16, anchor=E)
lb_4.grid(row=13, column=0, sticky=W)
text_4 = Entry(root, font=('arial', 16, 'bold'), bd=3, bg="Powder blue")
text_4.grid(row=13, column=0)


lb_5 = Label(root, font=('arial', 16, 'bold'), text="No of Units", bd=16)
lb_5.grid(row=10, column=0, sticky=W)
text_5 = Entry(root, font=('arial', 16, 'bold'), bd=3, bg="Powder blue")
text_5.grid(row=10, column=0)

lb_6 = Label(root, font=('arial', 16, 'bold'), text="Phone No", bd=16)
lb_6.grid(row=11, column=0, sticky=W)
text_6 = Entry(root, font=('arial', 16, 'bold'), bd=3, bg="Powder blue")
text_6.grid(row=11, column=0)

lb_10= Label(root, font=('arial', 16, 'bold'), text="City Name", bd=16)
lb_10.grid(row=13, column=0, sticky=W)
text_10 = Entry(root, font=('arial', 16, 'bold'), bd=3, bg="Powder blue")
text_10.grid(row=13, column=0)
def Add1():
    file=open("D:/python/blood.txt",'a+')
    file.write(str(text_6.get()))
    text_6.delete(0,END)
    file.write("\t")
    file.write(str(tkvar.get()))
    tkvar.set('A+')
    file.write("\t")
    file.write(str(text_2.get()))
    text_2.delete(0,END)
    file.write("\t")
    file.write(str(text_10.get()))
    text_10.delete(0, END)
    file.write("\t")
    file.write(str(text_5.get()))
    text_5.delete(0, END)
    file.write("\t")
    file.write(str(text_4.get()))
    text_4.delete(0, END)
    file.write("\n")
    file.close()





b1 = Button(root, text="Quit", width=10, font="arial" ,bg="grey", command=root.destroy)
b1.grid(row=18, column=0 ,padx=(0,0),pady=(10,0))
b2 = Button(root, text="Add",bg="green", width=10, font="arial",command=Add1)
b2.grid(row=16, column=0,padx=(0,0))

lb_70 = Label(root, font=('arial', 16, 'bold'), text="", bd=16, anchor=E)
lb_70.grid(row=19, column=0, sticky=W)
b5 = Button(root, text="Previous", width=10, font="arial",bg="grey",command=prev1)
b5.grid(row=12, column=0,padx=(0,130))
b6 = Button(root, text="Next", width=10, font="arial",bg="grey",command=next1)
b6.grid(row=12, column=0,padx=(100,0))
b7 = Button(root, text="First Record", width=15, font="arial",bg="orange",command=first)
b7.grid(row=17, column=0,padx=(0,150),pady=(10,0))
b8 = Button(root, text="Last Record", width=15, font="arial",bg="orange",command=last)
b8.grid(row=17, column=0,padx=(150,0),pady=(10,0))
root.mainloop()