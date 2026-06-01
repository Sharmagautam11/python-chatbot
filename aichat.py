import datetime
import random
from colorama import Fore, init

# Start colorama
init()

# Load memory
try:
    with open("memory.txt", "r") as file:
        name = file.read().strip()
except:
    name = ""

print(Fore.YELLOW + "=== AI Chatbot Started ===")

while True:
    user = input(Fore.CYAN + "You: ").lower()

    if user == "hello":
        replies = [
            "Hello Gautam!",
            "Hi! Nice to see you.",
            "Hey Gautam, how are you?"
        ]
        print(Fore.GREEN + "Bot:", random.choice(replies))

    elif user == "how are you":
        print(Fore.GREEN + "Bot: I am fine and ready to help you.")

    elif user == "what is your name":
        print(Fore.GREEN + "Bot: I am your AI chatbot.")

    elif user == "what is my name":
        if name != "":
            print(Fore.GREEN + f"Bot: Your name is {name}")
        else:
            print(Fore.GREEN + "Bot: I don't know your name yet.")

    elif user.startswith("my name is"):
        name = user.replace("my name is", "").strip()

        with open("memory.txt", "w") as file:
            file.write(name)

        print(Fore.GREEN + f"Bot: Nice to meet you, {name}! I will remember you.")

    elif user == "time":
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(Fore.GREEN + "Bot: Current time is", current_time)

    elif user == "joke":
        jokes = [
            "Why do programmers hate bugs? Because they take too much debugging!",
            "Python is my favorite snake.",
            "Why did the computer sleep? Because it was tired."
        ]

        print(Fore.GREEN + "Bot:", random.choice(jokes))

    elif user == "motivate me":
        motivation = [
            "Success comes from consistency.",
            "Keep learning every day.",
            "Small progress is still progress."
        ]

        print(Fore.GREEN + "Bot:", random.choice(motivation))

    elif user.startswith("calculate"):
        try:
            expression = user.replace("calculate", "")
            result = eval(expression)
            print(Fore.GREEN + f"Bot: Answer = {result}")
        except:
            print(Fore.GREEN + "Bot: Invalid calculation.")

    elif user == "help":
        print(Fore.GREEN + "Bot Commands:")
        print(Fore.GREEN + "- hello")
        print(Fore.GREEN + "- my name is ___")
        print(Fore.GREEN + "- what is my name")
        print(Fore.GREEN + "- time")
        print(Fore.GREEN + "- joke")
        print(Fore.GREEN + "- motivate me")
        print(Fore.GREEN + "- calculate 5+5")
        print(Fore.GREEN + "- bye")

    elif user == "bye":
        print(Fore.RED + "Bot: Goodbye Gautam!")
        break

    else:
        print(Fore.GREEN + "Bot: Sorry, I don't understand.")