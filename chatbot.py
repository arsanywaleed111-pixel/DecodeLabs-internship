print("Welcome to AI Chatbot!")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! Nice to meet you.")

    elif user_input == "how are you":
        print("Bot: I am fine, thank you!")

    elif user_input == "your name":
        print("Bot: My name is AI Bot.")

    elif user_input == "what can you do":
        print("Bot: I can answer simple questions.")

    elif user_input == "bye" or user_input == "exit":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")