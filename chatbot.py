#import the regular expression module to handle pattern matching
import re

# a directory that maps keyboard  to predefined respponces
responses = {
    "hi": "Hello! How can I assist you today?",
    "how are you": "I'm just a computer program, but thanks for asking! How can I help you?",
    "bye": "Goodbye! Have a great day!",
    "help": "Sure! What do you need help with?",
    "thank you": "You're welcome! If you have any more questions, feel free to ask.",
    "what is your name": "I am a simple chatbot created to assist you.",
    "default": "I'm sorry, I didn't understand that. Can you please rephrase?",
}

# Function to find the appropriate response based on the user's input
def chatbot_response(user_input):
    #convert the user input to lowercase to make matching case-insensitive
    user_input = user_input.lower()
    
    for keyword in responses:
        if re.search(keyword,user_input):
            return responses[keyword]
    
    return responses["default"]


# Main function to run the chatbot
def chatbot():
    print("Chatbot: Hello! I'm here to assist you. Type 'bye' to exit.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Check if the user wants to exit the chat
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        # Get the chatbot's response based on user input
        response = chatbot_response(user_input)

        # Print the chatbot's response
        print(f"Chatbot: {response}")
# Run the chatbot
chatbot()