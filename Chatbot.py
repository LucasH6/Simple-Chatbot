#Ketan Kumawat :-"Simple chatbot Task 1"

def simple_chatbot(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Define predefined rules and responses
    greetings = ["hello", "hi", "hey", "greetings"]
    farewells = ["bye", "goodbye", "see you", "take care"]
    asking_name = ["what's your name?", "who are you?", "your name?"]
    default_response = "I'm sorry, I didn't understand that."

    # Check user input against predefined rules
    if any(word in user_input for word in greetings):
        return "Hello! How can I help you today?"

    elif any(word in user_input for word in farewells):
        return "Goodbye! Have a great day!"

    elif any(word in user_input for word in asking_name):
        return "I am a simple chatbot."

    else:
        return default_response


# Main loop for user interaction
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break

    response = simple_chatbot(user_input)
    print("Chatbot:", response)
