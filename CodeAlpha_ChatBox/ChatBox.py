def get_bot_response(user_input):
    # Normalize input by lowercasing and stripping whitespace
    user_input = user_input.lower().strip()
    
    if user_input in ["hello", "hi", "hey"]:
        return "Hi!"
    elif user_input in ["how are you", "how are you?", "how's it going"]:
        return "I'm fine, thanks!"
    elif user_input in ["bye", "goodbye", "exit"]:
        return "Goodbye!"
    elif user_input in ["what is your name", "what's your name?"]:
        return "I am a simple rule-based chatbot."
    else:
        return "I'm sorry, I don't understand that. Try saying 'hello', 'how are you', or 'bye'."

def main():
    print("Chatbot: Hello! Type 'bye' to exit the conversation.")
    while True:
        user_input = input("You: ")
        response = get_bot_response(user_input)
        print(f"Chatbot: {response}")
        
        if user_input.lower().strip() in ["bye", "goodbye", "exit"]:
            break

if __name__ == "__main__":
    main()
