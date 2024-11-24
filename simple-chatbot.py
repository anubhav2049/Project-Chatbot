responses = {"hi" : "Hello there, how may I assist you!", "how are you?": "I'm fine! Ask me some simple basic questions", 
             "help" : "I can assist with basic questions. Try asking something!"}

def chatbot():
    print("Hi, I'm a simple chatbot. Ask me something!")
    while True:
        user_input = input("You: ").lower()
        if user_input in responses:
            print(responses[user_input])
        elif "how old are you" in user_input or "your age" in user_input:
            print("I'm 20 years old.")
        elif "what's your name" in user_input or "your name" in user_input:
            print("I'm a simple chatbot.")
        elif "bye" in user_input:
            print("Goodbye! See you soon!")
            break
        else:
            print("I'm not sure how to answer that. Ask me a simple question!")
    
    
if __name__ == "__main__":
    chatbot()