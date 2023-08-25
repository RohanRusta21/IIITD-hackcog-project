import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import nltk
import pandas as pd

from deep_translator import GoogleTranslator
import pandas as pd

def main2():
    text = open('read.txt', encoding='utf-8').read()
    lower_case = text.lower()
    global cleaned_text
    cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# Using word_tokenize because it's faster than split()
    tokenized_words = word_tokenize(cleaned_text)  # Removed "english"

# Removing Stop Words
    final_words = []
    for word in tokenized_words:
     if word not in stopwords.words('english'):
        final_words.append(word)

# Lemmatization - From plural to single + Base form of a word (example better -> good)
    lemma_words = []
    for word in final_words:
       word = WordNetLemmatizer().lemmatize(word)
       lemma_words.append(word)

    emotion_list = []
    with open('emotions.txt', 'r') as file:
      for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in lemma_words:
            emotion_list.append(emotion)

    print(emotion_list)
    global count
    count = Counter(emotion_list)
    print(count)
    return emotion_list
def callcount():
   return count


def sentiment_analyze():  # Renamed from sentiment_analyse to sentiment_analyze
    score = SentimentIntensityAnalyzer().polarity_scores(cleaned_text)
    if score['neg'] > score['pos']:
        senti="Negative Sentiment"
    elif score['neg'] < score['pos']:
        senti="Positive Sentiment"
    else:
        senti="Neutral Sentiment"
    print(senti)
    return(senti)





