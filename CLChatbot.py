import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name?",
        ["You can call me a chatbot", "My name is Chatbot", "I am a chatbot"]
    ],
    [
        r"how are you?",
        ["I'm doing good", "I'm fine", "Pretty good, how about You?"]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind"]
    ],
    [
        r"I am fine",
        ["Great to hear that!"]
    ],
    [
        r"quit",
        ["BBye take care. It was nice talking to you :) "]
    ],
]

chatbot = Chat(pairs, reflections)
chatbot.converse()
