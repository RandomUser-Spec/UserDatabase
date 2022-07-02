from tkinter import *
root = Tk()
root.title("Inheritance")
root.geometry("600x600")

label_name = Label(root, text="User Name : ")
label_name.place(relx=0.3,rely=0.2, anchor=CENTER)
entry_name = Entry(root)
entry_name.place(relx=0.6,rely=0.2, anchor=CENTER)
label_email = Label(root, text="Email id : ")
label_email.place(relx=0.3,rely=0.3, anchor=CENTER)
entry_email = Entry(root)
entry_email.place(relx=0.6,rely=0.3, anchor=CENTER)
label = Label(root)

dictionary = {}
class Users: 

    def __init__(self):
        print("This is user class")
        
    def addUser(key, value): 
         #access the dictionary variable inside the class
         #pass parameter key as the index to the dictionary and inside it assign the parameter as value.
         #update the text parameter of the label with variable dictionary.
         global dictionary
         dictionary[key] = value
         label["text"] = dictionary

class GetUsers(Users): 
        
    def __init__(self):
        print("This is getUsers class")
        
    def getUser(self):
        #using get() function get the entry_name from the user and store it in variable username
        #using the get() function get the email_id from the user and store it in variable email_id
        #access the addUser function of the users class and inside it pass the parameters as username, email_id
        gottenName = entry_name.get()
        gottenEmail = entry_email.get()
        Users.addUser(gottenName, gottenEmail)

#Create a object of GetUsers class        
user = GetUsers()
btn = Button(root, text="Add user details", command=user.getUser)
btn.place(relx=0.5,rely=0.4, anchor=CENTER)
label.place(relx=0.5,rely=0.5, anchor=CENTER)
root.mainloop()