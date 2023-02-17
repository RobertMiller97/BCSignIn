# Breast Cancer Sign In Project

import tkinter
from tkinter import*
from tkinter import messagebox

# Window
root = Tk()
root.title("Login")
root.geometry('800x700+20+0')
root.resizable(False,False)
root.configure(bg='#F7F7F7')

# Breast Cancer Photo
img = PhotoImage(file='bc7.png',height=800,width=800)
Label(root, image=img).place(x=0,y=-100)

# Sign In Bakcground
frame=Frame(root,width=250,height=500,bg='#FFABD1')
frame.place(x=10,y=180)

# Sign In
heading=Label(frame,text='Sign In',bg='#FFABD1',fg='#fff',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=60,y=5)

# username & password
user=Label(frame,text='Username',fg='#CCCCCC', bg='#fff',font=('Microsoft YaHei UI Light',12,'bold'))
user.place(x=10,y=60,width=200)
password=Label(frame,text='Password',fg='#CCCCCC', bg='#fff',font=('Microsoft YaHei UI Light',12,'bold'))
password.place(x=10,y=100,width=200)

# Create a Button
btn = tkinter.Button(root, text='Sign In' , bg='#B00159', fg='#fff')
btn.place(x=20,y=320,width=100)


# Donations
user=Label(frame,text='Donations',fg='#CCCCCC', bg='#fff',font=('Microsoft YaHei UI Light',12,'bold',))
user.place(x=10,y=200,width=200)


btn = tkinter.Button(root, text='Donate',bg='#B00159',fg='#fff')
btn.place(x=20,y=420,width=100)




# Window Execution
root.mainloop()