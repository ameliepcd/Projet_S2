# Projet_S2
Projet : à partir d'un nom d'utilisateur twitter, on récupère 9 images représentatives du compte de la personne. 

ETAPE 0 : 
Récupération des tweets que l'on traduit en anglais avec l'API twitter en enlevant les mots vides ("the","and"...) 
(recup_tweets.py)

ETAPE 1 : 
Récupérer à partir d'une collection de thème (série, film, lieu), les mots présents dans les tweets de l'utilisateur avec l'API Twitter. 
(analyse_tweets_proj.py) 

ETAPE 2 : 
Rebasculer sur la méthode "classique" qui récupère seulement les mots les plus fréquents présents dans les tweets si on ne récupère
9 mots avec l'étape 1.
(analyse_tweet_vrac.py)

ETAPE 3: 
On met ensemble les deux étapes précédents de façon à obtenir la liste finale des 9 mots avec un nom d'utilisateur donné. 
(final_recup_tweets_projvrac.py)

ETAPE 4: 
Récupération d'une image ou d'un url à partir d'un mot clé sur FLICK grâce à l'API FLICKR.
(flickr.py)

ETAPE 5: 
Assemblage de tous les codes, de façon à afficher à partir du nom d'utilisateur directement les 9 images sous forme d'un ticket
sur python. 
(affichage_image.py)

ETAPE 6: 
Quelques tests unitaires ont été réalisés (pas sous pytest par manque de temps pour prendre en main le package)
(test.py)


