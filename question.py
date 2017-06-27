from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords
import random
import sqlite3


# Sentences we'll respond with if the user greeted us
GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up","yo")

GREETING_RESPONSES = ["'sup bro", "hey", "*nods*", ]

def check_for_greeting(sentence):
    """If any of the words in the user's input was a greeting, return a greeting response"""
    for word in sentence:
        if word in GREETING_KEYWORDS:
            return random.choice(GREETING_RESPONSES)
        else:
            return "I Dont know"

#qry = 'hi bot'    
def processing(qry):
    words = word_tokenize(qry) #words = ['hi', 'bot']
    tagged_query = pos_tag(words)#tagged_query = [('hi', 'NN'), ('bot', 'NN')]
    reply = check_for_greeting(words)
    return reply
