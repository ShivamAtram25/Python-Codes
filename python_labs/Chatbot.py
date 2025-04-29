import tkinter as tk
from tkinter import scrolledtext
import cohere
import pyttsx3
import speech_recognition as sr

# === API Setup ===
co = cohere.Client("dN61vXT6r2I12JpoyYZnAA7Um6O9LhYuafNMIPxS")  # Replace with your real API key

# === Speech Engine Setup ===
engine = pyttsx3.init()
engine.setProperty('rate', 150)
is_speaking = False  # GLOBAL VARIABLE

# === Speech Recognition Setup ===
recognizer = sr.Recognizer()

def toggle_speak(text_to_speak, button):
    global is_speaking
    if not is_speaking:
        is_speaking = True
        button.config(text="⏹ Stop")
        engine.say(text_to_speak)
        engine.runAndWait()
        button.config(text="🔊 Speak")
        is_speaking = False
    else:
        engine.stop()
        button.config(text="🔊 Speak")
        is_speaking = False

def listen_to_user():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source, timeout=5)
            user_text = recognizer.recognize_google(audio)
            entry_box.delete(0, tk.END)
            entry_box.insert(0, user_text)
    except Exception as e:
        print("Error:", str(e))

def call_chatbot_api(message):
    try:
        response = co.chat(message=message)
        return response.text
    except Exception as e:
        return f"API Error: {str(e)}"

def send_message():
    user_message = entry_box.get().strip()
    if not user_message:
        return

    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"You: {user_message}\n", "user")

    bot_response = call_chatbot_api(user_message)
    chat_window.insert(tk.END, f"Bot: {bot_response}\n", "bot")
    
    add_speak_button(bot_response)

    chat_window.config(state=tk.DISABLED)
    entry_box.delete(0, tk.END)
    chat_window.yview(tk.END)

def add_speak_button(text_to_speak):
    speak_btn = tk.Button(chat_window, text="🔊 Speak", font=("Arial", 8))
    speak_btn.config(command=lambda: toggle_speak(text_to_speak, speak_btn))
    chat_window.window_create(tk.END, window=speak_btn)
    chat_window.insert(tk.END, "\n\n")

# === GUI Setup ===
root = tk.Tk()
root.title("AI ChatBot with Voice Input/Output")
root.geometry("650x700")
root.resizable(False, False)
root.config(bg="#f0f0f0")

chat_window = scrolledtext.ScrolledText(root, state='disabled', wrap=tk.WORD, font=("Arial", 13), bg="#ffffff", fg="#000000", padx=10, pady=10)
chat_window.place(x=10, y=10, width=630, height=580)
chat_window.tag_config("user", foreground="blue")
chat_window.tag_config("bot", foreground="green")

entry_box = tk.Entry(root, font=("Arial", 14))
entry_box.place(x=10, y=610, width=440, height=40)
entry_box.focus()

send_button = tk.Button(root, text="Send", font=("Arial", 12, "bold"), bg="#007ACC", fg="white", command=send_message)
send_button.place(x=460, y=610, width=80, height=40)

mic_button = tk.Button(root, text="🎤 Speak", font=("Arial", 12), bg="#28a745", fg="white", command=listen_to_user)
mic_button.place(x=550, y=610, width=80, height=40)

root.bind('<Return>', lambda event: send_message())
root.mainloop()
