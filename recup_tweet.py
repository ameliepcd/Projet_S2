import connexion_api
from traduction_tweet_english import *
from textblob import *

### permet de récupérer des listes de tweets traduits en anglais

def collect_by_user(user_id):
    #Récupère les textes des derniers tweets d'un utilisateur donné et les renvoie dans une liste
    connexion = connexion_api.twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 100)
    liste_tweet=[]
    for status in statuses:
        liste_tweet.append(status.text)
    return(liste_tweet)

user_id='EmmanuelMacron'
print(collect_by_user('EmmanuelMacron'))

def traduction_liste_tweet(liste):
    #prend en entrée une liste de tweet et la traduit en anglais
    liste_traduite=[]
    for tweet in liste :
        nouv_tweet=TextBlob(tweet)
        #on traduit le tweet que si il n'est pas en anglais
        if nouv_tweet.detect_language()!='en':
            new_tweet = translate(tweet)
            liste_traduite.append(new_tweet)
        else:
            liste_traduite.append(tweet)
    return(liste_traduite)

#a=collect_by_user('EmmanuelMacron')
#print(a)
#print(traduction_liste_tweet(a))


