from tkinter import *
import base64


bg = Tk()

bg.geometry('700x500')
bg.resizable(0,0)
bg.configure(bg ="black")
bg.title("Data Defender")

Label(bg, text ='Encode and Decode your texts', font = 'arial 20 bold').pack()

mail = StringVar()
safe_key = StringVar()
mode = StringVar()
product = StringVar()


def Encode(key,message):
    encrypted=[]


    for i in range(len[message]):
        key_s = key[i % len(key)]
        encrypted.append(chr((ord(message[i]) + ord(key_s)) % 256))
        return base64.urlsafe_b64encode("".join(encrypted).encode()).decode()


def Decode(key,message):
    decrypted=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        decrypted.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return "".join(decrypted)
def Mode():
    if(mode.get() == 'encryption'):
        product.set(Encode(safe_key.get(), Text.get()))
    elif(mode.get() == 'decryption'):
        product.set(Decode(safe_key.get(), Text.get()))
    else:
        product.set('Invalid Mode')
def Exit():
    bg.destroy()

def Reset():
    Text.set("")
    safe_key.set("")
    mode.set("")
    product.set("")




Label(bg, font= 'arial 12 bold', text='MESSAGE').place(x= 60,y=60)
Entry(bg, font = 'arial 10', textvariable = Text, bg = 'white').place(x=290, y = 60)
Label(bg, font = 'arial 12 bold', text ='KEY').place(x=60, y = 90)
Entry(bg, font = 'arial 10', textvariable = safe_key , bg ='white').place(x=290, y = 90)
Label(bg, font = 'arial 12 bold', text ='MODE(e-encode, d-decode)').place(x=60, y = 120)
Entry(bg, font = 'arial 10', textvariable = mode , bg= 'white').place(x=290, y = 120)
Entry(bg, font = 'arial 10 bold', textvariable = product, bg ='ghost white').place(x=290, y = 150)
Button(bg, font = 'arial 10 bold', text = 'RESULT'  ,padx =2,bg ='LightGray' ,command = Mode).place(x=60, y = 150)
Button(bg, font = 'arial 10 bold' ,text ='RESET' ,width =6, command = Reset,bg = 'cyan', padx=2).place(x=80, y = 190)
Button(bg, font = 'arial 10 bold',text= 'EXIT' , width = 6, command = Exit,bg = 'firebrick2', padx=2, pady=2).place(x=180, y = 190)
image = PhotoImage(file ="")
bg.mainloop()