import random
import pickle
import json
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer


from tensorflow.keras.models import load_model


lemmatizer = WordNetLemmatizer()
model = load_model('/home/cifope/Bureau/chatbot/chatbot/chats/chatbot1.h5')
intens = json.loads(open('/home/cifope/Bureau/chatbot/chatbot/chats/data.json').read())


words = pickle.load(open('/home/cifope/Bureau/chatbot/chatbot/chats/word.pkl','rb'))

classes = pickle.load(open('/home/cifope/Bureau/chatbot/chatbot/chats/classes.pkl','rb'))




def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]* len(words)
    for w in sentence_words:
        for i,word in enumerate(words):
            if word==w:
                bag[i] = 1

    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    result = [[i,r] for i,r in enumerate(res) if r > ERROR_THRESHOLD]
    result.sort(key=lambda x: x[1],reverse=True)
    return_list = []
    for r in result:
        return_list.append({'intens':classes[r[0]],"probability": str(r[1]) })
    return return_list
def get_reponse(intents_list,instents_json):
    tag = intents_list[0]['intens']
    list_of_intents = instents_json['intens']
    for i in list_of_intents:
        if i["tag"]==tag:
            result = random.choice(i['reponses'])
            break
    return result
def rps(message):
    ints = predict_class(message)
    res = get_reponse(ints,intens)
    return res
