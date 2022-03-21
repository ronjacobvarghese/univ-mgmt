from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk


root = Tk()

root.title("University Management System")
canvas = Canvas(root, width=1000, height=500)
canvas.grid(columnspan=2, rowspan=3)

# Image
image = Image.open("images/download.jpeg")
image = image.resize((500, 500), Image.ANTIALIAS)
image = ImageTk.PhotoImage(image)
image_label = Label(image=image, width=500,  height=500)
image_label.image = image
image_label.grid(column=0, row=0, rowspan=3)

#header
header_font = font.Font(family="Comic Sans MS", size=20, weight="bold")
header_message = Message(root, text="Login System",
                         width=400, padx=200, pady=50, fg="white", bg="#ca0a4a")
header_message.configure(font=header_font)
header_message.grid(row=0, column=1)


#Form
space_Frame = Frame(root, width=500, height=370)
space_Frame.grid(row=1, column=1, rowspan=2)

#UserLabel
label_font = font.Font(family="Comic Sans MS", size=13, weight = "bold")
text_font = font.Font(family="Comic Sans MS", size=13)
rollNo_message = Message(root, text="Enter Roll No:",
                         width=200, font=label_font)
rollNo_message.place(relx=0.5, rely=0.4)
rollNo_text = Text(root,height = 1.3,width = 45, font = text_font, bg = "white", fg = "black")
rollNo_text.place(relx = 0.51, rely = 0.45 )

#PasswordLabel
rollNo_message = Message(root, text="Password:",
                         width=200, font=label_font)
rollNo_message.place(relx=0.5, rely=0.55)
rollNo_text = Text(root,height = 1.3,width = 45, font = text_font, bg = "white", fg = "black")
rollNo_text.place(relx = 0.51, rely = 0.6 )

#CancelButton
cancel_image = Image.open("images/Cancel_button.png")
cancel_image = ImageTk.PhotoImage(cancel_image)
cancel_button = Button(root, image = cancel_image)
cancel_button.place(relx = 0.75, rely = 0.85)

#LogInButton
login_image = Image.open("images/LogIn_button.png")
login_image = ImageTk.PhotoImage(login_image)
cancel_button = Button(root, image = login_image)
cancel_button.place(relx = 0.87, rely = 0.85)

root.mainloop()
