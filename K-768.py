from tkinter import *
import openai

root = Tk()
root.geometry("600x600")
root.config(bg="Black")
root.title("Chat-Bot")

#################################################################################################
api_label = Label(root, text="Enter APIKEY:", bg="Black", fg="White")
api_label.place(x=200,y=40)

get_apikey = Entry(root)
get_apikey.place(x=200,y=60)

entry1 = Entry(root, width=20)
entry1.place(x=12, y=60)

openai.api_key = get_apikey.get()

def chat_with_gpt():
    user_input = entry1.get()  # Get the user's input from the entry box
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        # Update bot_answer label with the response
        bot_answer.config(text=response['choices'][0]['message']['content'])
    except Exception as e:
        bot_answer.config(text=f"Error: {e}")


#################################################################################################


title_label = Label(root, text="Buisness A-Bot", bg="Black", fg="White",font=("Cascadia Code", 16, "bold"))
title_label.pack()

title_label = Label(root, text="You:", bg="Black", fg="White",font=("Arial", 10, "bold"))
title_label.place(x=12, y=38)

button1 = Button(root, text="Enter🔎", command=chat_with_gpt)
button1.place(x=140, y=60)

Labelcredit = Label(root, text="Credit: Cheez_dev", bg="black", foreground="RED")
Labelcredit.place(x=200, y=280)

title_labe2l = Label(root, text="Bot:", bg="Black", fg="White",font=("Arial", 10, "bold"))
title_labe2l.place(x=12, y=100)

bot_answer = Label(root, text="", bg="Black", fg="White")
bot_answer.place(x=12,y=120)


root.mainloop()