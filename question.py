from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords
import random
import sqlite3

#flags



# Sentences we'll respond with if the user greeted us
GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up","yo")

GREETING_RESPONSES = ["'sup", "hey", "*nods*", ]

RESPONSES = ["What can I do for you?","How can I help?","What can I help you with?"]

WEATHER_KEYWORDS = ["climate","weather","forecast"]

def check_for_greeting(sentence):
    """If any of the words in the user's input was a greeting, return a greeting response"""
    for word in sentence:
        g_flag = 0
        w_flag = 0
        d_flag = 0
        if g_flag == 0:
            if word in GREETING_KEYWORDS:
                g_flag = 1
                return random.choice(GREETING_RESPONSES),random.choice(RESPONSES)
##            elif word in WEATHER_KEYWORDS:
##                w_flag = 1
##                return
##            elif word in

            
##            
##    for word in sentence:
##        if word in WEATHER_KEYWORDS:
##            
##
##
##
##
##        else:
##            return 1
##
##def weather_api(location):
##    
    


#qry = 'hi bot'    
def processing(qry):
    words = word_tokenize(qry) #words = ['hi', 'bot']
    tagged_query = pos_tag(words)#tagged_query = [('hi', 'NN'), ('bot', 'NN')]
    reply = check_for_greeting(tagged_query)
##    temperature = check_for_temperature()
##    dictionary = check_for_meaning()
    return reply
    
        
