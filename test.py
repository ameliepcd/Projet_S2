import pytest
import unittest
from final_recup_tweets_projvrac import *



class test(unittest.TestCase):

    def test_analyse(self):
        liste_domaine = ['fleur','jonquille','tulipe','pissenlit']
        liste_tweet1 = ['la maison blanche','cette fleur est une tulipe','tulipe']
        liste_tweet2=['la maison blanche','le souvenir du 24 Mai']
        liste1=['fleur','tulipe','tulipe']
        liste2=['bonjour']
        self.assertEqual(analyze(liste_domaine,liste_tweet1),liste1)
        self.assertNotEqual(analyze(liste_domaine,liste_tweet1),liste2)

    def test_nb_fréquence(self):
        list=['booba', 'booba', 'balavoine', 'balavoine', 'balavoine', 'balavoine']
        a=frequence_word(list)
        d={'booba':2, 'balavoine':4}
        e={4:5, 'bonjour':3}
        self.assertNotEqual(a,e)
        self.assertAlmostEqual(a,d)

    def test_mot_le_plus_fréquent(self):
        d={'booba':2, 'balavoine':4,'chien':4}
        word=mot_plus_frequent(d)
        self.assertNotEqual(word,['balavoine'])
        self.assertNotEqual(word,['balavoine','chien'])
        self.assertEqual(word,['chien','balavoine'])
        self.assertNotEqual(word,['Booba'])

    def test_final_recup_vracproj(self):
        


unittest.main()
