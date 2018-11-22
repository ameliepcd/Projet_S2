from flickr import *
from final_recup_tweets_projvrac import *



def affichage_mot_twitter(liste_mots):
    ###à partir d'une liste de mots, renvoie la photo correspondante
    for word in liste_mots:
        url=print_by_tags(word)
        print_picture(url)
    return()

#liste_mots=['desk','cat','black','sing']
#affichage_mot_twitter(liste_mots)

def image_a_partir_du_nom_seule(user_id,listes_domaines,nombre):
    ###à partir d'un nom d'utilisateurs, récupère les 10 mots 
    ###et affiche les images
    liste_mots=final_recup_projvrac(user_id,nombre ,listes_domaines)
    print(liste_mots)
    affichage_mot_twitter(liste_mots)

#print(image_a_partir_du_nom('Potus',main_list,10))



def image_a_partir_du_nom_mosaique(user_id,listes_domaines,nombre):
    ###à partir d'un nom d'utilisateurs, récupère les 10 mots
    ###et affiche les images
    liste_mots=final_recup_projvrac(user_id,nombre ,listes_domaines)
    print(liste_mots)
    liste_url=récup_url_image(liste_mots)

    ##affiche la mosaïque à partir d'une liste d'url
    affichage_mosaique(liste_url)



def récup_url_image(liste_mots):
    ###à partir d'une liste de mots, renvoie la liste des url des images correspondantes
    liste_url=[]
    for word in liste_mots:
        url=print_by_tags(word)
        liste_url.append(url)
    return(liste_url)

from PIL import Image, ImageTk
import  tkinter as Tk


def affichage_mosaique(liste_url):
    ######on fait pour 3x3 ici
    ###code pas beau, mais pas réussi à la faire en bouclant..
    ###à partir d'une liste d'url d'image, affiche les images les unes en dessous des autres
    root = Tk.Tk()

    with urllib.request.urlopen(liste_url[0]) as url:
        with open('temp0.jpg', 'wb') as f:
            f.write(url.read())
    image0 = Image.open("temp0.jpg")
    photo0 = ImageTk.PhotoImage(image0)
    canvas0 = Tk.Canvas(root, width = image0.size[0], height = image0.size[1])
    canvas0.create_image(0,0, anchor = Tk.NW, image=photo0)

    with urllib.request.urlopen(liste_url[1]) as url:
        with open('temp1.jpg', 'wb') as f:
            f.write(url.read())
    image1 = Image.open("temp1.jpg")
    photo1 = ImageTk.PhotoImage(image1)
    canvas1 = Tk.Canvas(root, width = image1.size[0], height = image1.size[1])
    canvas1.create_image(0,1, anchor = Tk.NW, image=photo1)

    with urllib.request.urlopen(liste_url[2]) as url:
        with open('temp2.jpg', 'wb') as f:
            f.write(url.read())
    image2 = Image.open("temp2.jpg")
    photo2 = ImageTk.PhotoImage(image2)
    canvas2 = Tk.Canvas(root, width = image2.size[0], height = image2.size[1])
    canvas2.create_image(0,2, anchor = Tk.NW, image=photo2)

    with urllib.request.urlopen(liste_url[3]) as url:
        with open('temp3.jpg', 'wb') as f:
            f.write(url.read())
    image3 = Image.open("temp3.jpg")
    photo3 = ImageTk.PhotoImage(image3)
    canvas3 = Tk.Canvas(root, width = image3.size[0], height = image3.size[1])
    canvas3.create_image(1,0, anchor = Tk.NW, image=photo3)

    with urllib.request.urlopen(liste_url[4]) as url:
        with open('temp4.jpg', 'wb') as f:
            f.write(url.read())
    image4 = Image.open("temp4.jpg")
    photo4 = ImageTk.PhotoImage(image4)
    canvas4 = Tk.Canvas(root, width = image4.size[0], height = image4.size[1])
    canvas4.create_image(1,1, anchor = Tk.NW, image=photo4)

    with urllib.request.urlopen(liste_url[5]) as url:
        with open('temp5.jpg', 'wb') as f:
            f.write(url.read())
    image5 = Image.open("temp5.jpg")
    photo5 = ImageTk.PhotoImage(image5)
    canvas5 = Tk.Canvas(root, width = image5.size[0], height = image5.size[1])
    canvas5.create_image(1,2, anchor = Tk.NW, image=photo5)

    with urllib.request.urlopen(liste_url[6]) as url:
        with open('temp6.jpg', 'wb') as f:
            f.write(url.read())
    image6 = Image.open("temp6.jpg")
    photo6 = ImageTk.PhotoImage(image6)
    canvas6 = Tk.Canvas(root, width = image6.size[0], height = image6.size[1])
    canvas6.create_image(2,0, anchor = Tk.NW, image=photo6)

    with urllib.request.urlopen(liste_url[7]) as url:
        with open('temp7.jpg', 'wb') as f:
            f.write(url.read())
    image7 = Image.open("temp7.jpg")
    photo7 = ImageTk.PhotoImage(image7)
    canvas7 = Tk.Canvas(root, width = image7.size[0], height = image7.size[1])
    canvas7.create_image(2,1, anchor = Tk.NW, image=photo7)

    with urllib.request.urlopen(liste_url[8]) as url:
        with open('temp8.jpg', 'wb') as f:
            f.write(url.read())
    image8 = Image.open("temp8.jpg")
    photo8 = ImageTk.PhotoImage(image8)
    canvas8 = Tk.Canvas(root, width = image8.size[0], height = image8.size[1])
    canvas8.create_image(2,2, anchor = Tk.NW, image=photo8)


    canvas0.pack()
    canvas1.pack()
    canvas2.pack()
    canvas3.pack()
    canvas4.pack()
    canvas5.pack()
    canvas6.pack()
    canvas7.pack()
    canvas8.pack()

    root.mainloop()


#image_a_partir_du_nom_mosaique('Potus',listes_domaines,9)
