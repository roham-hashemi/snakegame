from tkinter import *

def save():
    f=open(f"{e_name.get()}.txt", 'w')
    f.write(f"{e_name.get()}\n{e_surname.get()}\n{e_age.get()}")
    f.close()    
root = Tk()
root.geometry("600x300")
root.resizable(1,1) # کم کاربرد
root.title("preject 1")
root.config(bg='sky blue')
l_name=Label(root, text="Enter your name: ")
l_name.pack()
e_name = Entry(root)
e_name.pack()
l_surname=Label(root, text="Enter your surname: ")
l_surname.pack()
e_surname = Entry(root)
e_surname.pack()
l_age=Label(root, text="Enter your age: ")
l_age.pack()
e_age = Entry(root)
e_age.pack()
btn_exit = Button(root, text='Exit', command=exit)
btn_exit.pack()
btn_save = Button(root, text='Save', command=save)
btn_save.pack()
mainloop()


rajsldkajfl;jksadf
sdjfkllksajdflk
sdajflkjlsadjfljsaldkfj
dsajflkjlksdajf
