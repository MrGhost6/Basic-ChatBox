from nltk.chat.util import Chat, reflections

# Define the dialogue
pairs = [
    [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["No i can't go to chatGBT",]
    ],
     [
        r"(.*) your name ?",
        ["I don't have one, but you can just call me robot and I'm a chatbot .",]
    ],
    [
        r"can i call you (.*)",
        ["Noooo, i'ts a horrible name"]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*)created(.*)",
        ["Mr ghost created me using a forbiden magin from the 1878","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['f tabon mok',]
    ],
    [
        r"(.*)raining in (.*)",
        ["I don't give a shit about the rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health, how are yours",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of all kind of sports",]
    ],
    [
        r"who (.*) (Footballer|Middleman)?",
        ["Lionel Messi","me"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)","go do do somethig good"]
    ],
    [
        r"(.*)",
        ['ok goo away']
    ],
]
]
#default message at the start of chat
print("Hi, I'm a robot that is better than chatGBT i can help you but i want because i don't want to. Type quit to leave and leaving me in peace ")
chat = Chat(pairs, reflections)
chat.converse()