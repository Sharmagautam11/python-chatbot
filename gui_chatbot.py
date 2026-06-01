import tkinter as tk
import random
import datetime

# Main window
window = tk.Tk()
window.title("AI Chatbot")
window.geometry("550x650")
window.config(bg="#1e1e1e")

# Chat area
chat_area = tk.Text(
    window,
    height=25,
    width=60,
    bg="#2d2d2d",
    fg="white",
    font=("Arial", 12)
)

chat_area.pack(pady=10)

# User input
user_input = tk.Entry(
    window,
    width=40,
    font=("Arial", 14),
    bg="#3c3c3c",
    fg="white",
    insertbackground="white"
)

user_input.pack(pady=5)

# Save chat history
def save_chat(message):

    with open("chat_history.txt", "a") as file:
        file.write(message + "\n")

# Bot reply function
def send_message(event=None):

    user = user_input.get().lower()

    if user == "":
        return

    user_message = "You: " + user
    chat_area.insert(tk.END, user_message + "\n")
    save_chat(user_message)

    # Typing effect
    chat_area.insert(tk.END, "Bot is typing...\n")
    chat_area.update()

    if user == "hello":
        replies = [
            "Hello Gautam!",
            "Hi! Nice to see you.",
            "Hey Gautam!"
        ]
        bot_reply = random.choice(replies)

    elif user == "time":
        bot_reply = datetime.datetime.now().strftime("%H:%M:%S")

    elif user == "joke":
        jokes = [
            "Python is my favorite snake.",
            "Programmers love coffee.",
            "Debugging is like detective work."
        ]
        bot_reply = random.choice(jokes)

    elif user == "motivate me":
        motivation = [
            "Keep learning every day.",
            "Consistency beats talent.",
            "Never stop improving."
        ]
        bot_reply = random.choice(motivation)

    elif user == "bye":
        bot_reply = "Goodbye Gautam!"

    else:
        bot_reply = "Sorry, I don't understand."

    # Remove typing text
    chat_area.delete("end-2l", "end-1l")

    bot_message = "Bot: " + bot_reply

    chat_area.insert(tk.END, bot_message + "\n\n")
    save_chat(bot_message)

    # Auto-scroll
    chat_area.see(tk.END)

    user_input.delete(0, tk.END)

# Clear chat
def clear_chat():
    chat_area.delete("1.0", tk.END)

# Send button
send_button = tk.Button(
    window,
    text="Send",
    command=send_message,
    bg="#4CAF50",
    fg="white",
    width=15
)

send_button.pack(pady=5)

# Clear button
clear_button = tk.Button(
    window,
    text="Clear Chat",
    command=clear_chat,
    bg="#f44336",
    fg="white",
    width=15
)

clear_button.pack(pady=5)

# Enter key support
window.bind("<Return>", send_message)

# Run app
window.mainloop()