from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os

root = Tk()
root.title("File Transfer")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False,False) # cannot resize width and height

# set the background of the image
def set_background(window, image_path):
    image = PhotoImage(file=image_path)
    background_label = Label(window, image=image)
    background_label.place(relwidth=1, relheight=1)

# send file
def send_file():

    root.withdraw() # hide the main window

    window = Toplevel(root)
    window.title("Send")
    window.geometry('450x560+500+200') # width x height x horizontal x vertical
    window.configure(bg="#f4fdfe")
    window.resizable(False,False) # cannot resize width and height

    # function that help you select the file
    def select_file():
        return filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title='Select Your File',
        filetypes=(('file_type', '*.txt'), ('all files', '*.*'))
    )
        
    def send_file_window():
        s=socket.socket()
        host = socket.gethostname()
        port=8080
        s.bind((host,port))
        s.listen(1) # how many client
        print(host)
        print('Waiting for incoming connection...')
        conn,addr=s.accept()
        file = open(filename,'rb')
        file_data=file.read(1024)
        conn.send(file_data)
        print("Data has been transmitted successfully!")

    #icon
    image_icon1=PhotoImage(file="pics/send-icon.png")
    window.iconphoto(False,image_icon1)

    Sbackground=PhotoImage(file="pics/sender.png") 
    Label(window,image=Sbackground).place(x=-2,y=0)

    Mbackground=PhotoImage(file="pics/id.png")
    Label(window,image=Mbackground,bg="#f4fdfe").place(x=50,y=260)


    host=socket.gethostname()
    Label(window,text=f'ID: {host}', bg='white',fg='black').place(x=140,y=290)

    # stop here
    Button(window,text="+ select file",width=10,height=1,font='arial 14 bold',bg="#fff", fg="#000",command=select_file).place(x=120, y=150)
    Button(window,text="SEND",width=8,height=1,font='arial 14 bold',bg='#000',fg="#fff", command=send_file_window).place(x=260,y=150)

    window.mainloop()

# function that received the sent file
def receive_file():
    main = Toplevel(root)
    main.title("Receive")
    main.geometry('450x560+200+200') # width x height x horizontal x vertical
    set_background(main,"pics/receive.png")
    # main.configure(bg="#f4fdfe")
    main.resizable(False,False) # cannot resize width and height

    def receiver():
        ID=SenderID.get()
        filename1=file_name.get()

        s=socket.socket()
        port=8080
        s.connect((ID,port))
        file=open(filename1,'wb')
        file_data=s.recv(1024)
        file.write(file_data)
        file.close()
        print("File has been received successfully!")

    #icon
    image_icon1=PhotoImage(file="pics/receive-icon.png")
    main.iconphoto(False,image_icon1)

    # Hbackground = PhotoImage(file="pics/receive.png")
    # Label(main,image=Hbackground).place(x=-2,y=0)
    

    logo = PhotoImage(file="pics/profile.png")
    logo = logo.subsample(3,3)
    Label(main, image=logo,bg="#f4fdfe").place(x=100,y=250)
   
    Label(main,text="Receive",font=('arial',15),bg="#f4fdfe").place(x=100,y=280)

    Label(main,text="Input sender id",font=('arial',10,'bold'),bg="#f4fdfe").place(x=20,y=340)
    SenderID = Entry(main,width=25,fg="black",border=2,bg='white',font=('arial',15))
    SenderID.place(x=20,y=370)
    SenderID.focus()

    Label(main,text="Name of the incoming file",font=('arial',10,'bold'),bg="#f4fdfe").place(x=20,y=420)
    file_name = Entry(main,width=25,fg="black",border=2,bg='white',font=('arial',15))
    file_name.place(x=20,y=450)

    imageIcon = PhotoImage(file="pics/arrow.png")
    rr=Button(main,text="Receive",compound=LEFT,image=imageIcon,width=130,bg="#39c790",font='arial 14 bold',command=receiver)
    rr.place(x=20,y=500)

    main.mainloop()

#icon
image_icon = PhotoImage(file="pics/icon1.png")
root.iconphoto(False,image_icon)

Label(root,text="File Tranfer",font=('Acumin Variable Concept',20,'bold'),bg="#f4fdfe").place(x=20,y=30)
Frame(root,width=400,height=2,bg="#f3f5f6").place(x=25,y=80)

#send button
send_image=PhotoImage(file="pics/send-icon.png")
send_image = send_image.subsample(3, 3)
send=Button(root,image=send_image,bg="#f4fdfe",bd=0, command=send_file)
send.place(x=50,y=100)

#receive button
receive_image=PhotoImage(file="pics/receive-icon.png")
receive_image = receive_image.subsample(3, 3)
receive=Button(root,image=receive_image,bg="#f4fdfe",bd=0, command=receive_file)
receive.place(x=300,y=100)

#label
Label(root,text="Send",font=('Acumin Variable Concept',17,'bold'),bg="#f4fdfe").place(x=60,y=200)
Label(root,text="Receive",font=('Acumin Variable Concept',17,'bold'),bg="#f4fdfe").place(x=300,y=200)

background=PhotoImage(file="pics/background.png")
Label(root,image=background).place(x=-2,y=323)

root.mainloop()