from tkinter import *
from tkinter import ttk
from tkinter.messagebox import CANCEL
from PIL import Image, ImageTk
import numpy as np
import os
from os.path import isfile, join
from threading import Thread
from user_handler import UserData
from time import sleep

background, textColor = 'black', '#F6FAFB'
background, textColor = textColor, background

avatarChoosen = 0
choosedAvtrImage = None
user_name = ''
user_gender = ''
user_password = ''

###### ROOT1 ########
def startLogin():		
	try:
		result = True
		if result:
			user = UserData()
			user.extractData()
			userName = user.getName()
			welcLbl['text'] = 'Hi '+userName+',\nWelcome to the world of\nScience & Technology'
			loginStatus['text'] = 'UNLOCKED'
			loginStatus['fg'] = 'green'
			os.system('python modul/gui_ass.py')
		else:
			print('Error Occurred')

	except Exception as e:
		print(e)


if os.path.exists('userData')==False:
	os.mkdir('userData')


def SuccessfullyRegistered():
	if avatarChoosen != 0:
		gen = 'Male'
		if user_gender==2: gen = 'Female'
		u = UserData()
		u.updateData(user_name, gen, avatarChoosen)
		usernameLbl['text'] = user_name
		raise_frame(root4)
def selectAVATAR(avt=0):
	global avatarChoosen, choosedAvtrImage
	avatarChoosen = avt
	i=1
	for avtr in (avtb1,avtb2,avtb3,avtb4,avtb5,avtb6,avtb7,avtb8):
		if i==avt:
			avtr['state'] = 'disabled'
			userPIC['image'] = avtr['image']
		else: avtr['state'] = 'normal'
		i+=1

################# GUI ###################
def raise_frame(frame):
	frame.tkraise()


root = Tk()
root.title('J.A.R.V.I.S')
w_width, w_height = 350, 600
s_width, s_height = root.winfo_screenwidth(), root.winfo_screenheight()
x, y = (s_width/2)-(w_width/2), (s_height/2)-(w_height/2)
root.geometry('%dx%d+%d+%d' % (w_width,w_height,x,y-30)) #center location of the screen
root.configure(bg=background)
# root.attributes('-toolwindow', True)
root1 = Frame(root, bg=background)
root2 = Frame(root, bg=background)
root3 = Frame(root, bg=background)
root4 = Frame(root, bg=background)

for f in (root1, root2, root3, root4):
	f.grid(row=0, column=0, sticky='news')

########  MAIN SCREEN  #########
image1 = Image.open('assets/images/assistant.png')
image1 = image1.resize((300,250))
defaultImg1 = ImageTk.PhotoImage(image1)

dataFrame1 = Frame(root1, bd=10, bg=background)
dataFrame1.pack()
logo = Label(dataFrame1, width=300, height=250, image=defaultImg1)
logo.pack(padx=10, pady=10)

#welcome label
welcLbl = Label(root1, text='Hi there,\nWelcome to the world of\nScience & Technology', font=('Arial Bold', 15), fg='#303E54', bg=background)
welcLbl.pack(padx=10, pady=20)

#add login
loginStatus = Label(root1, text="Hi, I'm JARVIS", font=('Arial Bold', 15), bg=background, fg='red')
loginStatus.pack(pady=(40,20))	

if os.path.exists('userData/userData.pck')==False:
	Login = Button(root1, text='   Login   ', font=('Arial', 12), bg='#018384', fg='white', relief=FLAT, command=lambda:raise_frame(root2))
	Login.pack(ipadx=10)
else:
	Thread(target=startLogin).start()
########  Input INFO  #######

image2 = Image.open('assets/images/assistant.png')
image2 = image2.resize((300, 250))
defaultImg2 = ImageTk.PhotoImage(image2)

dataFrame2 = Frame(root2, bd=10, bg=background)
dataFrame2.pack(fill=X)
lmain = Label(dataFrame2, width=300, height=250, image=defaultImg2)
lmain.pack(padx=10, pady=10)

#Details
detailFrame2 = Frame(root2, bd=10, bg=background)
detailFrame2.pack(fill=X)
userFrame2 = Frame(detailFrame2, bd=10, width=300, height=250, relief=FLAT, bg=background)
userFrame2.pack(padx=10, pady=10)

#progress
progress_bar = ttk.Progressbar(root2, orient=HORIZONTAL, length=303, mode='determinate')
#name
nameLbl = Label(userFrame2, text='Name', font=('Arial Bold', 12), fg='#303E54', bg=background)
nameLbl.place(x=10,y=10)
nameField = Entry(userFrame2, bd=5, font=('Arial Bold', 10), width=25, relief=FLAT, bg='#D4D5D7')
nameField.focus()
nameField.place(x=80,y=10)

genLbl = Label(userFrame2, text='Gender', font=('Arial Bold', 12), fg='#303E54', bg=background)
genLbl.place(x=10,y=50)
r = IntVar()
s = ttk.Style()
s.configure('Wild.TRadiobutton', background=background, foreground=textColor, font=('Arial Bold', 10), focuscolor=s.configure(".")["background"])
genMale = ttk.Radiobutton(userFrame2, text='Male', value=1, variable=r, style='Wild.TRadiobutton', takefocus=False)
genMale.place(x=80,y=52)
genFemale = ttk.Radiobutton(userFrame2, text='Female', value=2, variable=r, style='Wild.TRadiobutton', takefocus=False)
genFemale.place(x=150,y=52)
addBtn = Button(userFrame2, text="    Let's go    ", font=('Arial Bold', 12), bg='#01933B', fg='white', command=lambda:raise_frame(root3), relief=FLAT)
addBtn.place(x=90, y=150)

#### AVATAR SELECTION ####
Label(root3, text="Choose Your Avatar", font=('arial', 15), bg=background, fg='#303E54').pack()

avatarContainer = Frame(root3, bg=background, width=300, height=500)
avatarContainer.pack(pady=10)
size = 100

avtr1 = Image.open('assets/images/avatars/a1.png')
avtr1 = avtr1.resize((size, size))
avtr1 = ImageTk.PhotoImage(avtr1)
avtr2 = Image.open('assets/images/avatars/a2.png')
avtr2 = avtr2.resize((size, size))
avtr2 = ImageTk.PhotoImage(avtr2)
avtr3 = Image.open('assets/images/avatars/a3.png')
avtr3 = avtr3.resize((size, size))
avtr3 = ImageTk.PhotoImage(avtr3)
avtr4 = Image.open('assets/images/avatars/a4.png')
avtr4 = avtr4.resize((size, size))
avtr4 = ImageTk.PhotoImage(avtr4)
avtr5 = Image.open('assets/images/avatars/a5.png')
avtr5 = avtr5.resize((size, size))
avtr5 = ImageTk.PhotoImage(avtr5)
avtr6 = Image.open('assets/images/avatars/a6.png')
avtr6 = avtr6.resize((size, size))
avtr6 = ImageTk.PhotoImage(avtr6)
avtr7 = Image.open('assets/images/avatars/a7.png')
avtr7 = avtr7.resize((size, size))
avtr7 = ImageTk.PhotoImage(avtr7)
avtr8 = Image.open('assets/images/avatars/a8.png')
avtr8 = avtr8.resize((size, size))
avtr8 = ImageTk.PhotoImage(avtr8)

	
avtb1 = Button(avatarContainer, image=avtr1, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(1))
avtb1.grid(row=0, column=0, ipadx=25, ipady=10)

avtb2 = Button(avatarContainer, image=avtr2, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(2))
avtb2.grid(row=0, column=1, ipadx=25, ipady=10)

avtb3 = Button(avatarContainer, image=avtr3, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(3))
avtb3.grid(row=1, column=0, ipadx=25, ipady=10)

avtb4 = Button(avatarContainer, image=avtr4, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(4))
avtb4.grid(row=1, column=1, ipadx=25, ipady=10)

avtb5 = Button(avatarContainer, image=avtr5, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(5))
avtb5.grid(row=2, column=0, ipadx=25, ipady=10)

avtb6 = Button(avatarContainer, image=avtr6, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(6))
avtb6.grid(row=2, column=1, ipadx=25, ipady=10)

avtb7 = Button(avatarContainer, image=avtr7, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(7))
avtb7.grid(row=3, column=0, ipadx=25, ipady=10)

avtb8 = Button(avatarContainer, image=avtr8, bg=background, activebackground=background, relief=FLAT, bd=0, command=lambda:selectAVATAR(8))
avtb8.grid(row=3, column=1, ipadx=25, ipady=10)


Button(root3, text='         Submit         ', font=('Arial Bold', 15), bg='#01933B', fg='white', bd=0, relief=FLAT, command=SuccessfullyRegistered).pack()
userPIC = Label(root4, bg=background, image=avtr1)
userPIC.pack(pady=(40, 10))
usernameLbl = Label(root4, text="Jarvis", font=('Arial Bold',15), bg=background, fg='#85AD4F')
usernameLbl.pack(pady=(0, 70))
def destroyButton():
    root4.destroy()
Label(root4, text="Your account has been successfully activated!", font=('Arial Bold',15), bg=background, fg='#303E54', wraplength=300).pack(pady=10)
button = Button(root4, text='     OK     ', bg='#0475BB', fg='white',font=('Arial Bold', 18), bd=0, relief=FLAT,command=lambda: quit()).pack(pady=50)
root.iconbitmap('assets/images/assistant2.ico')
raise_frame(root1)
root.mainloop()

