from tkinter import *
from tkinter import messagebox
import os
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def GeneratePass():
    
    
    
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = ([random.choice(letters) for _ in range(nr_letters)] + [random.choice(symbols) for _ in range(nr_symbols)] + [random.choice(numbers) for _ in range(nr_numbers)])

    random.shuffle(password_list)
    password_str = "".join(password_list)


    input_password.insert(0 , string = password_str)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    try:
        Save_web = input_web.get()
        save_email = input_Email.get()
        save_password = input_password.get()

        new_data ={
            Save_web:{
                "email": save_email,
                "password": save_password
            }
        }

        if len(Save_web) == 0 or len(save_password) == 0:
            messagebox.showinfo(title="Warning", message="Please don't Leave any fields empty")
            
        else: 
        
            with open("Saved_data.json", "r") as saved_data:
                data = json.load(saved_data)
                data.update(new_data)

            with open("Saved_data.json", "w") as saved_data:
                json.dump(data, saved_data, indent=4)
    except FileNotFoundError:
        with open("Saved_data.json", "w") as saved_data:
            json.dump(new_data, saved_data, indent=4)



    input_web.delete(0,'end')
    input_password.delete(0,'end')
# ---------------------------- UI SETUP ------------------------------- #

def Search():
    Save_web = input_web.get()
    try:
        with open("Saved_data.json", "r") as saved_data:
            data = json.load(saved_data) #Convert the json to a python dictionary
            
            # print(data["facebook"]["email"])
        
        if Save_web in data:
            messagebox.showinfo(title = Save_web, message= f"Email: {data[Save_web]['email']}\nPasswoord: {data[Save_web]['password']}")

        else:
            messagebox.showinfo(title="error", message=f"No details for the {Save_web} exist.")
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="No Data File found")
       



window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)



canvas = Canvas(width=200, height=200)
logo_path = os.path.join("password generator","logo.png")
logo = PhotoImage(file=logo_path)
canvas.create_image(100, 100, image = logo)
canvas.grid(column=1,row=0)


Website_Label = Label(text="website:")
Website_Label.grid(column=0, row=1)
Email_Label = Label(text= "Email/Username:")
Email_Label.grid(column=0, row=2)
password_label = Label (text="Password:")
password_label.grid(column=0,row=3)

input_web = Entry(width=36)
input_web.grid(row=1,column=1) 
input_web.focus()

input_Email = Entry(width=55)
input_Email.grid(column=1,row=2, columnspan=2)
input_Email.insert(END, "andreimandapat09@gmail.com")
input_password = Entry(width=36)
input_password.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=GeneratePass)
generate_button.grid(column=2,row=3,columnspan=2)

search_button = Button(text="Search",width=14, command = Search)
search_button.grid(column=2, row=1)

add_button = Button(text="Add", width=46, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()