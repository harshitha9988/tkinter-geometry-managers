from tkinter import*

root=Tk()
root.title('Login App')
root.geometry('400x400')

frame=Frame(master=root, height=200, width=360,bg="#90ba97")

lbl1=Label(frame,text="Full Name",bg="#4F8B46", fg="#D8F1D9", width=12)
lbl2=Label(frame,text="Email Id",bg="#4F8B46", fg="#D8F1D9", width=12)
lbl3=Label(frame,text="Enter Password",bg="#4F8B46", fg="#D8F1D9", width=12)

nameEntry=Entry(frame)
emailEntry=Entry(frame)
passEntry=Entry(frame,show="*")

def display():
        name=nameEntry.get()
        greet="Hey "+name
        message="\nCongratulations for your new account!"
        textbox.insert(END,greet)
        textbox.insert(END,message)

textbox=Text(bg="#7C8B82",fg="#FFFFFF")
btn=Button(text="Create Account", command=display, bg="#2E5B3C")

frame.place(x=20,y=0)
lbl1.place(x=20,y=20)
nameEntry.place(x=150,y=20)
lbl2.place(x=20,y=80)
emailEntry.place(x=150,y=80)
lbl3.place(x=20,y=140)
passEntry.place(x=150,y=140)
btn.place(x=130,y=210)
textbox.place(y=250)

root.mainloop()