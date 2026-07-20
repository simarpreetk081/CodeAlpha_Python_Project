print("Simple Chatbot")

while True:

    a = input("You : ")

    if a == "hello":
        print("Bot : Hello")
    elif a == "hi":
        print("Bot : Hi")
    elif a == "how are you":
        print("Bot : I am fine")
    elif a == "bye":
        print("Bot : Bye")
        break
    else:
        print("Bot : I don't know this")