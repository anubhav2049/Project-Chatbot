from preprocessing import preprocess

responses = {"greet" : "Hello there! How may I assist you?", "age": "I'm an AI, so I don't have any human concept of age!", 
             "help" : "I can assist with basic questions. Try asking something!", "goodbye": "Goodbye! See you again soon!", "name":"I'm a simple Chatbot that can answer simple questions"}

intent_keywords = {
    "greet":["hello","hi","hey"],
    "help":["help","assist","support"],
    "age":["how old are you","your age"],
    "name":["what's your name","your name"],
    "bye":["goodbye","bye bye","see you later"]
}

def get_intent(user_input):
    words = preprocess(user_input)
    for intent, keywords in intent_keywords.items():
        for keyword in keywords:
            if keyword in user_input or all(word in words for word in keyword.split()):
                return intent
    return None

def chatbot():
    print("Hi, I'm a simple chatbot. Ask me something!")
    while True:
        user_input = input("You: ").lower()
        if user_input.lower() in ["bye", "exit", "goodbye"]:
            print("Chatbot:", responses["goodbye"])
            break

        intent = get_intent(user_input)
        #print("Chatbot:", intent)      #Debug line; uncomment to see how intent gets tokenized
        if intent:
            print("Chatbot:", responses[intent])
        else:
            print("Chatbot: I'm sorry, but I don't understand. Please rephrase!")
    
    
if __name__ == "__main__":
    chatbot()