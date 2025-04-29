import threading
import requests
import tkinter as tk
from tkinter import scrolledtext
from flask import Flask, request, jsonify

# === Flask API Setup ===
app = Flask(__name__)

def get_bot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi there! How can I help you?"
    elif "your name" in user_input:
        return "I'm your local Python chatbot!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand. Could you rephrase?"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_msg = data.get("message", "")
    bot_reply = get_bot_response(user_msg)
    return jsonify({"reply": bot_reply})

# Start Flask app in a background thread
def start_api():
    app.run(debug=False, use_reloader=False)

# === Chat GUI Setup ===
def call_chatbot_api(message):
    try:
        response = requests.post("http://localhost:5000/chat", json={"message": message})
        return response.json().get("reply", "No reply received.")
    except Exception as e:
        return f"API Error: {str(e)}"

def send_message():
    user_message = entry_box.get().strip()
    if not user_message:
        return

    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"You: {user_message}\n", "user")

    bot_response = call_chatbot_api(user_message)
    chat_window.insert(tk.END, f"Bot: {bot_response}\n\n", "bot")

    chat_window.config(state=tk.DISABLED)
    entry_box.delete(0, tk.END)
    chat_window.yview(tk.END)

def start_gui():
    global entry_box, chat_window

    root = tk.Tk()
    root.title("Local AI ChatBot")
    root.geometry("600x650")
    root.resizable(False, False)
    root.config(bg="#f0f0f0")

    chat_window = scrolledtext.ScrolledText(root, state='disabled', wrap=tk.WORD, font=("Arial", 13), bg="#ffffff", fg="#000000", padx=10, pady=10)
    chat_window.place(x=10, y=10, width=580, height=540)
    chat_window.tag_config("user", foreground="blue")
    chat_window.tag_config("bot", foreground="green")

    entry_box = tk.Entry(root, font=("Arial", 14))
    entry_box.place(x=10, y=570, width=470, height=40)
    entry_box.focus()

    send_button = tk.Button(root, text="Send", font=("Arial", 12, "bold"), bg="#007ACC", fg="white", command=send_message)
    send_button.place(x=490, y=570, width=90, height=40)

    root.bind('<Return>', lambda event: send_message())
    root.mainloop()

# === Start Everything ===
if __name__ == '__main__':
    api_thread = threading.Thread(target=start_api)
    api_thread.daemon = True
    api_thread.start()

    start_gui()