import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pairs = [
    (r"Hi|Hello|Hey", ["Hello! How can I help you today?"]),
    (r"What's your name?", ["I'm a chatbot created using NLTK."]),
    (r"How are you?", ["I'm just a program, but I'm doing well!"]),
    (r"(.*) (your|you) name?", ["My name is ChatBot."]),
    (r"quit", ["Goodbye! Have a great day!"]),
]

chatbot = Chat(pairs, reflections)

def main():
    print("Hello! I am your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")

        if user_input.lower() == 'quit':
            print("ChatBot: Goodbye!")
            break
        response = get_response(user_input)
        print("ChatBot:", response)
def get_response(user_input):
    response = chatbot.respond(user_input)
    return response

if __name__ == "__main__":
    main()