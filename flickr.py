from code import *
from flickrapi import FlickrAPI
from pprint import pprint
from PIL import Image
import urllib.request
import tkinter

def print_by_thema(object):
    ### prend en entrée un texte relatif à un objet
    flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
    extras='url_sq'#,url_t,url_s,url_q,url_m,url_n,url_z,url_c,url_l,url_o'
    thema = flickr.photos.search(text=object, per_page=1, extras=extras)
    photos = thema['photos']
    ###renvoie un url pour ouvrir l'image sur fb


def print_by_tags(tag):
    flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
    extras='url_sq'
    dossier = flickr.photos.search(tags=tag, per_page=1, extras=extras, sort='relevance')
    photos = dossier['photos']
    #picture=pprint(photos['photo'][0]['url_sq'])
    return(photos['photo'][0]['url_sq'])



def print_picture(url):
    URL=url
    #URL = 'https://farm5.staticflickr.com/4881/45884451622_b952ed1472_s.jpg'
    with urllib.request.urlopen(URL) as url:
        with open('temp.jpg', 'wb') as f:
            f.write(url.read())

    img = Image.open('temp.jpg')
    img.show()


