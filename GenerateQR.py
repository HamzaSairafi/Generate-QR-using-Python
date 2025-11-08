import qrcode
from tkinter import *


def genrateQR():
    inpt = link.get()
    qr = qrcode.QRCode(version = 1, box_size = 5, border = 5, )

    qr.add_data(inpt)
    qr.make()

    img = qr.make_image(fill_color = 'black' , back_color = 'white')
    img.save('your_qr.png')


# window setting 
window = Tk()
window.geometry('360x400')
window.title("Genrate QR code")


lable = Label(window ,
                text="Generate a QR code using Python", 
                font=('Arial' , 15 , 'bold'), 
                fg='black', 
                bg='white', 
                border=10, 
                relief = RAISED , 
                padx=3,
                pady=5,)

lable.pack()

link = Entry(window,
             font=('Arial' , 15 ),
             border=10, 
             relief = RAISED , 
             )
link.place(x=60 , y= 58)


submit = Button(window,
                text="Submit",
                command=genrateQR,
                font=('Arial' , 10 , 'bold'),
                fg='black', 
                bg='white', 
                border=5, 
                relief=RAISED, 
                bd= 5,
                padx=3,
                pady=1,
                activeforeground="green",
                activebackground="black")

submit.place(x=5, y=150)


window.mainloop()

