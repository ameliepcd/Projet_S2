from textblob import *

def translate(tweet):
    #tweet est un texte str
    #traduis n'importe quel tweet en anglais
    tweet_initial = TextBlob(tweet)
    langue = tweet_initial.detect_language()
    tweet_traduit = tweet_initial.translate(from_lang=langue, to='en')
    return(tweet_traduit)


tweet='Je suis content'
#print(translate(tweet))

en_blob = TextBlob(u'Simple is better than complex.')
#print(en_blob.translate(from_lang='en', to='es'))

