from textblob import TextBlob
from recup_tweet import *
from champs_lexicaux import *

def lower_liste(liste):
    L=[]
    for word in liste:
        new=word.lower()
        L.append(new)
    return(L)

def analyze(liste_domaine,liste_tweet):
    #prend en entrée une liste de textes de tweet et
    # une liste avec le champ lexical d'un domaine EN MINUSCULE
    ###RECUPERE LES MOTS TROUVES DANS LES TWEETS DU CHAMP LEXICAL CORRESPONDANT
    mot_a_trouver = liste_domaine

    tweet_a_analyser=liste_tweet

    L=[]
    #dans la liste L, on ajoute les mots du domaine trouvés dans les tweets
    for tweet in liste_tweet:
        current_tweet=TextBlob(tweet)
        current_tweet=current_tweet.lower()
        words=current_tweet.words
        for word in words:
            if word in mot_a_trouver:
                L.append(word)
    return(L)



def frequence_word(list):
    #prend en entrée la liste résultante de la recherche d'un domaine de la fction analyse
    #ici, on va déterminer récupérer la fréquence de chaque mot dans la liste
    nb_frequence = {}
    for word in list :
        if word in nb_frequence:
            nb_frequence[word]+=1
        else:
            nb_frequence[word]=1
    return(nb_frequence)

#list=['booba', 'booba', 'balavoine', 'balavoine', 'balavoine', 'balavoine']
#a=frequence_word(list)
#print(a)


def mot_plus_frequent(nb_frequence):
    # prend en entrée un dictionnaire sortant de la fction frequence_word pour récupérer
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
    return(le_plus_fréquent)


### TEST avec le compte netflix sur le domaine des séries
liste_domaine = lower_liste(liste_parti_politique_brute)
user_id ='EmmanuelMacron'



def main_domaine(user_id,liste_domaine):
    #####Retourne pour un profil et un domaine, le mot correspondant le + fréquent
    tweet=collect_by_user(user_id)
    a = analyze(liste_domaine,tweet)
    freq = frequence_word(a)
    print(freq)
    return(mot_plus_frequent(freq))

print(main_domaine(user_id,liste_domaine))

def recup_tous_domaines(user_id,listes_domaines):
    ###listes_domaines est une liste de listes de domaines
    ###RETOURNE LA REQUETE FINALE POUR FLICKR
    mots_user_id=[]
    for liste in liste_domaine:
        mot_correspondant= main_domaine(user_id,liste)
        mots_user_id.append(mot_correspondant)
    return(mots_user_id)




