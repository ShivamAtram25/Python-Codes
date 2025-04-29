import tkinter as tk
from tkinter import scrolledtext

# Basic chatbot logic
def get_bot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello there! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing fine. Thanks for asking!"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I didn't understand that. Could you rephrase?"

# Send message to chat window
def send_message():
    user_input = entry_box.get()
    if user_input.strip() == "":
        return
    
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "You: " + user_input + "\n")
    
    bot_response = get_bot_response(user_input)
    chat_window.insert(tk.END, "Bot: " + bot_response + "\n\n")
    chat_window.config(state=tk.DISABLED)
    
    entry_box.delete(0, tk.END)
    chat_window.yview(tk.END)

# Main GUI setup
root = tk.Tk()
root.title("ChatBot")
root.geometry("500x600")
root.resizable(False, False)
root.config(bg="#f5f5f5")

# Chat window
chat_window = scrolledtext.ScrolledText(root, state='disabled', wrap=tk.WORD, font=("Arial", 12), bg="white", fg="black")
chat_window.place(x=10, y=10, width=480, height=500)

# Entry box
entry_box = tk.Entry(root, font=("Arial", 14))
entry_box.place(x=10, y=520, width=380, height=40)

# Send button
send_button = tk.Button(root, text="Send", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=send_message)
send_button.place(x=400, y=520, width=90, height=40)

# Run GUI loop
root.mainloop()
