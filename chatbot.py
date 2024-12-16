from preprocessing import preprocess_hybrid

responses = {"greet" : "Hello there! How may I assist you?", 
             "age": "I'm an AI, so I don't have any human concept of age!", 
             "help" : "I can assist with basic questions. Try asking something!", 
             "bye": "Goodbye! See you again soon!", 
             "name":"I'm a simple Chatbot that can answer simple questions",
             "feelings" : "I'm okay! How can I help you?"
             }

intent_keywords = {
    "greet":["hello","hi","hey"],
    "help":["help","assist","support", "what"],
    "age":["old","age"],
    "name":["name"],
    "bye":["goodbye","bye","later"],
    "feelings" : ["how", "are", "you", "how's", "it", "going", "feel"]
}

def get_intent(user_input):
    words = preprocess_hybrid(user_input)
    print("Debug: Tokenized words: ", words)
    for intent, keywords in intent_keywords.items():
        print(f"Checking intent '{intent}' with keywords {keywords}")
        for keyword in keywords:
            if " " in keyword and keyword in user_input:
                return intent
            if any(word in words for word in keywords):
                print(f"Match found: {intent}")
                return intent
    return None

def chatbot():
    print("Hi, I'm a simple chatbot. Ask me something!")
    while True:
        user_input = input("You: ").lower()
        if user_input.lower() in ["bye", "exit", "goodbye"]:
            print("Chatbot:", responses["bye"])
            break

        intent = get_intent(user_input)
        print("Chatbot:", intent)      #Debug line; uncomment to see how intent gets tokenized
        if intent:
            print("Chatbot:", responses[intent])
        else:
            print("Chatbot: I'm sorry, but I don't understand. Please rephrase!")
    
    
if __name__ == "__main__":
    chatbot()