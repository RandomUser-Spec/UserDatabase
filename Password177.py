from tkinter import *

root = Tk()
root.title("Login")
root.geometry("600x800")

labelname = Label(root, text = "Name : ")
labelname.place(relx = 0.2, rely = 0.1, anchor = CENTER)

inputname = Entry(root)
inputname.place(relx = 0.4, rely = 0.1, anchor = CENTER)

labelpassword = Label(root, text = "Password : ")
labelpassword.place(relx = 0.2, rely = 0.2,anchor = CENTER)

inputpassword = Entry(root)
inputpassword.place(relx = 0.4, rely = 0.2, anchor = CENTER)

labelcaptcha = Label(root, text = "Captcha : ")
labelcaptcha.place(relx = 0.2, rely = 0.3, anchor = CENTER)

inputcaptcha = Entry(root)
inputcaptcha.place(relx = 0.4, rely = 0.3, anchor = CENTER)

displayname = Label(root)
displayname.place(relx = 0.5, rely = 0.7, anchor = CENTER)

displaypassword = Label(root)
displaypassword.place(relx = 0.5, rely = 0.8, anchor = CENTER)

displaycaptcha = Label(root)
displaycaptcha.place(relx = 0.5, rely = 0.9, anchor = CENTER)

class userDB():
    def __init__(self):
        self.__username = "Wai"
        self.__password = "CodingRocks"
        self.__captcha = "Y7zJm0"
        
    def showUser(self):
        displayname["text"] = "Name :" + self.__username
        displaypassword['text'] = "Password :" + self.__password
        displaycaptcha['text'] = "Captcha :" + self.__captcha
        
        
obj1 = userDB()
def addUser():
    obj1.username = inputname.get()
    obj1.password = inputpassword.get()
    obj1.captcha = inputcaptcha.get()
    print("Details Updated")
    
btn = Button(root, text = "Update Login Details", command = addUser)
btn.place(relx = 0.3, rely = 0.4, anchor = CENTER)
btn1 = Button(root, text = "Show Profile", command = obj1.showUser)
btn1.place(relx = 0.6, rely = 0.4,anchor = CENTER)
root.mainloop()