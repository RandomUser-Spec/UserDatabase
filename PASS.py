from tkinter import *
import random

root=Tk()
root.title("Testing Random Function")
root.geometry("400x400")

expected_word = Label(root)
expected_word['text'] = "coding languages + vowels + numbers from 1-10"
entry = Entry(root)
guessed_password = Label(root)
generated_password = Label(root)
result = Label(root)

array_3d = [[[1,2,3,4,5,6,7,8,9,10],["HTML","CSS","C++","Lua","Javascript","C","Python"],["A","E","I","O","U"]]]
print(array_3d[0][2][3])

def check_password():
    random_no_1 = random.randint(0,9)
    random_no_2 = random.randint(0,6)
    random_no_3 = random.randint(0,4)
    
    letter1 = str(array_3d[0][0][random_no_1])
    letter2 = (array_3d[0][1][random_no_2])
    letter3 = (array_3d[0][2][random_no_3])
    generated_password['text']= "Generated Password = " + letter1 + "" + letter2 + "" + letter3
    gotten_password = entry.get()
    guessed_password['text'] = "Guessed Password = " + gotten_password
    if(generated_password == gotten_password):
       result['text'] = "the password was correct!" 
    else:
        result['text'] = "wrong! 😢"

expected_word.place(relx = 0.5, rely = 0.3, anchor = CENTER)
entry.place(relx = 0.5, rely = 0.4, anchor = CENTER)
guessed_password.place(relx = 0.5, rely = 0.5, anchor = CENTER)
btn = Button(root, text = "show password", command = check_password)
btn.place(relx = 0.5, rely = 0.6, anchor = CENTER)
generated_password.place(relx = 0.5, rely = 0.7, anchor = CENTER)
result.place(relx = 0.5, rely = 0.8, anchor = CENTER)

root.mainloop()