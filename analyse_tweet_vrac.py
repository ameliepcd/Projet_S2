import stopwords as stopwords
from textblob import TextBlob
from stopwords import *
from textblob import *
from recup_tweet import *
from analyse_tweets_proj import *
from champs_lexicaux import *
from traduction_tweet_english import *


def liste_mots(tweets):
    #prend en entrée une liste de texte de tweets, que l'on met dans un seul string
    text=''
    mots_inutiles= stopwords.get_stopwords('en')
    mystopwords=['I','will','\'','The','http']
    for tweet in tweets:
        text+= str(tweet)
    liste=TextBlob(text)
    #wordlist fait une liste des mots de tous les tweets
    wordlist=liste.words
    unique=[]
    for word in wordlist:
        w=Word(word)
        #on récupère les mots qui ne sont pas des mots vides et qui sont dans leur forme de base +
        #qui sont plus long que 3 carac
        if word not in mots_inutiles and word not in mystopwords and len(word)>2:
            word_lemmatize= w.lemmatize()
            unique.append(word_lemmatize)
        ###renvoie les mots dans une LISTE
    return(unique)

a=('hello, and, the, desks, went,desk')
#print(a.stopwords)

#print(stopwords.get_stopwords('en'))

#print(liste_mots(a))

def frequence_word(list):
    #prend en entrée la liste des mots des tweets sans les stopwords
    ###permet de récupérer dans un dico, les mots en clés et en valeurs leur nb d'apparition
    nb_frequence = {}
    for word in list :
        if word in nb_frequence:
            nb_frequence[word]+=1
        else:
            nb_frequence[word]=1

    ###renvoie un dico
    return(nb_frequence)

#print(frequence_word(liste_mots(a)))

def mot_plus_frequent2(nb_frequence):
    # prend en entrée un dictionnaire (clé = mot ; valeur = occurence) sortant de la fction frequence_word pour récupérer
    #les mots les plus fréquents (si ils existent)
    if len(nb_frequence)==0:
        return()
    else:
        le_plus_fréquent=[]
        max_occur=1
        for cle in nb_frequence.keys():
            if nb_frequence[cle]>max_occur:
                max_occur=nb_frequence[cle]
        for cle in nb_frequence:
            if nb_frequence[cle]==max_occur:
                le_plus_fréquent.append(cle)
        ###on enlève les mots pris du dico d'entrée si on a besoin d'utiliser pls fois cette fonction
        for word in le_plus_fréquent:
            del nb_frequence[word]

    #on renvoie les mots avec la plus grande occurence et on les supprime du dico
    return(le_plus_fréquent, nb_frequence)

#print(mot_plus_frequent(frequence_word(liste_mots(a))))

tweet=collect_by_user('POTUS')
#print(liste_mots(tweet))

def recup_nb_mots(nb_frequence,nombre):
    ### prend en entrée le dico de nb_frequence
    ###permet de récuperer le nombre de mots voulus en itérant sur la fonction mot_plus_frequent(nb_frequence)
    a_recup = nombre
    liste_frequent=[]
    while len(liste_frequent) < a_recup:
        new=mot_plus_frequent2(nb_frequence)
        liste_frequent+= new[0]
        nb_frequence=new[1]
    ###on renvoie la liste correspondante
    return(liste_frequent)

def final_word_vrac(user_id,nombre):
    tweet=collect_by_user(user_id)
    ###on prend la lower liste car les stopwords sont en minuscules

    lower_tweet=lower_liste(tweet)
    word=liste_mots(tweet)
    frequence=frequence_word(word)
    ###on récupère les mots les + fréquents sous forme de liste
    return(recup_nb_mots(frequence,nombre))

#print(final_word_vrac('POTUS',10))


