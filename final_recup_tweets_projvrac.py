from analyse_tweets_proj import *
from analyse_tweet_vrac import *
from traduction_tweet_english import *

def traduction_liste(liste):
    ###Traduit la liste des mots récupérés en anglais pour portwiture
    liste_traduite=[]
    for word in liste:
        word_initial = TextBlob(word)
        langue = word_initial.detect_language()
        if langue != 'en':
            word_traduit = word_initial.translate(from_lang=langue, to='en')
            liste_traduite.append(word_traduit)
        else:
            liste_traduite.append(word)
    return(liste_traduite)

def final_recup_projvrac(user_id,nombre ,listes_domaines):
    #prend en entrée un nom d'utilisateur à analyser et un nombre de mot à récupérer
    #ainsi que les listes de domaines de départ (pour récupérer les mots dans les thèmes choisis

    ###récupère la liste de mots par domaines, disons n mots
    liste_mots=recup_tous_domaines(user_id,listes_domaines)

    n=len(liste_mots)
    a_recup = nombre
    ###le pb c'est qu'on peut ne pas avoir récupérer suffisamment de mot voulu, on retombe donc sur la déf de portwiture initial
    ### on récupère seulement les mots les + fréquents
    if n < a_recup :
        ###avec les mots par thème, on peut ne pas récupérer suffisamment de mots
        ### on bascule donc sur la recherche par fréquence de mots:
        a_rajouter = a_recup - n
        liste_vrac=final_word_vrac(user_id, a_rajouter)
        liste_mots += liste_vrac
        return (liste_mots)
    if n > a_recup:
        ### on récupère les premiers mots récupérés
        return (liste_mots[:a_recup])


#print(traduction_liste(['head', 'good', 'last', 'sion', 'happy', 'will', 'just', 'girl', 'time', 'real']))

user_id='barackobama'
listes_domaines= main_list

#print(final_recup_projvrac(user_id,10,listes_domaines))
