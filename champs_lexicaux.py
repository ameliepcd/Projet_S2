from textblob import TextBlob
from countries import *
from films import *
from historical_era import *
from Hobbies import *
from Hollywood import *
from instru import *
from musician import *
from musictype import *


liste_series_brute=["Beavis and Butt-Head","The Good Wife","Avatar: The Last Airbender","Dr. Katz, Professional Therapist"
    ,"Happy Days","Will & Grace","Justified","Golden Girls","Frasier","Good Times","Soap","Rome","Boardwalk Empire",
    "The Real World","Oz","Rick and Morty","Alias","Downton Abbey","The Americans","Hannibal","ER","I, Claudius",
    "The Wonder Years" "Survivor","House of Cards","The Mary Tyler Moore Show","The Shield","Hill Street Blues",
    "The Andy Griffith Show","The Honeymooners","Sex and the City","The Muppet Show","Doctor Who","The Office",
    "Fargo","Better Call Saul","Star Trek","The X-Files","Twin Peaks","Futurama","Friends","Buffy the Vampire Slayer",
    "South Park","Saturday Night Live","Game of Thrones","The Simpsons","Lost","Mad Men","Breaking Bad",
    "How I Met Your Mother","The Walking Dead","American Dad", "Gotham", "Black Mirror", "Sherlock",
    "Narcos", "The Mentalist", "Vikings", "Doctor House", "The Handmade Tale","Criminal Mind","Westworld", "Peaky Blinders", "Marvel"]

liste_sport_brute=["Football","Basketball","Dance","Tennis","Volleyball","gymnastics","judo","handball",
                   "boxing","bowling","jujitsu","biathlon","triathlon","soccer","swimming","snowboarding",
                   "skiing","scuba diving","diving","curling","track and field","lacrosse","riding"]


liste_parti_politique_brute=["EnMarche","Parti Socialiste","PS","Front National","Les Républicains",
                             "Fillon","LePen","Macron","Sarkozy","Lasalle","Hollande","Mélenchon",
                             "La France Insoumise","Democrats","Republicans","Trump","Obama","Clinton","Chirac",
                             "Edouard Philippe", "no pasaran"]

def get_queries(file_path):
    #renvoie une liste de domaine à partir d'un fichier texte
    mon_fichier = open(file_path,'r')
    queries=[]
    for line in mon_fichier:
        a=line.replace('\n','')
        queries.append(a)
    final_queries=[]
    for i in range (len(queries)):
        if len(queries[i])>1:
            final_queries.append(queries[i])
    return(final_queries)


liste_animaux_brutes=get_queries('animaux.txt')

#print(lower_liste(liste_series_brute))

liste_pays_fr=["Afghanistan", "Afrique du Sud", "Albanie", "Algérie", "Allemagne", "Andorre", "Angola",
            "Antigua-et-Barbuda", "Arabie saoudite", "Argentine", "Arménie", "Australie","Autriche",
            "Azerbaïdjan", "Bahamas", "Bahreïn", "Bangladesh", "Barbade", "Belgique", "Belize", "Bénin",
            "Bhoutan", "Biélorussie", "Bolivie", "Bosnie-Herzégovine", "Botswana", "Brésil", "Brunei", "Bulgarie",
            "Burkina Faso"," Burundi", "Cambodge", "Cameroun", "Canada", "Cap-Vert?", "Chili", "Chine", "Chypre",
            "Colombie", "Comores", "Congo", "Corée du Sud", "Costa Rica", "Côte d’Ivoire", "Croatie", "Cuba",
            "Danemark", "Djibouti", "Dominique", "Égypte", "Émirats arabes unis", "Équateur", "Érythrée",
            "Espagne", "Estonie", "États-Unis d’Amérique", "Éthiopie","Macédoine", "Fidji", "Finlande",
            "France", "Gabon", "Gambie", "Géorgie", "Ghana", "Guatemala", "Grèce", "Grenade", "Guinée",
            "Guinée-Bissau", "Guinée équatoriale", "Guyana, Haïti", "Honduras", "Hongrie", "Inde", "Indonésie",
            "Irlande", "Iran", "Iraq", "Islande", "Israël", "Italie", "Jamaïque", "Japon", "Jordanie",
            "Kazakhstan", "Kenya", "Kirghizstan", "Kiribati", "Koweït", "Laos", "Lesotho", "Lettonie", "Liberia",
            "Liban", "Libye", "Liechtenstein", "Lituanie", "Luxembourg", "Madagascar", "Malaisie", "Maldives",
            "Malawi", "Mali", "Malte", "Marshall", "Maroc", "Maurice", "Mauritanie", "Mexique", "Micronésie",
            "Moldavie", "Monaco", "Mongolie", "Mozambique", "Myanmar", "Namibie", "Nauru", "Népal", "Nicaragua",
            "Niger", "Nigeria", "Norvège", "Nouvelle-Zélande", "Oman", "Ouganda", "Ouzbékistan", "Pakistan",
            "Palaos", "Panama", "Papouasie-Nouvelle-Guinée", "Paraguay", "Pays-Bas", "Pérou", "Philippines",
            "Pologne", "Portugal", "Qatar", "République centrafricaine", "République démocratique du Congo",
            "République dominicaine", "République tchèque", "Royaume-Uni", "Roumanie", "Russie", "Rwanda",
            "Sainte-Lucie", "Saint-Kitts-et-Nevis","Saint-Marin", "Saint-Vincent-et-les-Grenadines", "Salomon",
            "Salvador", "Samoa", "Sao Tomé-et-Principe?", "Sénégal", "Seychelles", "Sierra Leone", "Singapour",
            "Slovaquie", "Slovénie", "Somalie", "Soudan", "Sri Lanka", "Suède", "Suisse", "Suriname", "Swaziland",
            "Syrie", "Tadjikistan", "Tanzanie", "Tchad", "Thaïlande", "Timor oriental", "Togo", "Tonga",
            "Trinité-et-Tobago", "Tunisie", "Turkménistan", "Turquie", "Tuvalu", "Ukraine", "Uruguay","Vanuatu",
            "Vatican", "Venezuela", "Viêt Nam", "Yémen", "Yougoslavie", "Zambie", "Zimbabwe"]

def traduire_en_anglais(liste):
    liste_traduite = []
    for word in liste:
        new_word=TextBlob(word)
        word_traduit=new_word.translate(from_lang='fr', to='en')
        liste_traduite.append(word_traduit)
    return(liste_traduite)

#print(traduire_en_anglais(liste_pays_fr))


liste_films =["2001: A Space Odyssey","Pulp Fiction","Shining","Gattaca","A Clockwork Orange",
             "One FLew Over the Cuckoo's Nest","The Green Mile","Edward Scissorhands","Fight Club",
             "Taxi Driver","Usual Suspects","Sleepers","Rain Man","The Place Beyond The Pines",
             "Le Roi et l'Oiseau","Full Metal Jacket","The Truman Show","Apocalypse Now","Reservoir Dogs",
             "The Shawshank Redemption","Eternal Sunshine of the Spotless Mind","Scarface","Death Proof",
             "Schindler's List","No Country for Old Men","Requiem for a Dream","Se7en","Titanic",
             "The Wolf of Wall Street","American Beauty","American History X","Once Upon A Time In The West",
             "Alien","La vita è bella","Metropolis","The Great Dictator","the Big Lebowski","Django Unchained",
             "Good Morning England","Argo","Who Framed Roger Rabbit","Into the Wild","The Blues Brothers",
             "Point Break","Brazil","Drive","The Longest Day","The Birds","La Piel que habito","Star Wars",
             "Harry Potter", "Pirate of The Carabean Sea","Avatar", "Interstellar","Inception","Batman",
             "Lalaland","Lord of the Rings","The Silence of the Lamb","Marvel"]

liste_hollywood = ["Stanley Kubrick","Tarantino","Francis Ford Coppola","Tim Burton","Davind Fincher","David Lynch",
                 "Martin Scorsese","Georges Lucas","Wes Anderson","Steven Spielberg","Ethan Cohen","James Cameron",
                 "Disney","Pixar","Angelina Jolie","Brad Pitt","Ben Affleck","Jennifer Aniston","Leonardo DiCaprio",
                "Charlize Theron","Jennifer Lopez","Megan Fox","Nathalie Portman","Julia Roberts","Johnny Depp",
                 "Nicole Kidman","Sandra Bullock","Scarlett Johansson","Netflix","Disney"]


main_list=[liste_hollywood,liste_series_brute,liste_animaux_brutes,liste_pays_fr,liste_parti_politique_brute,liste_sport_brute,
           musictype, historical_era,hobbies, instru,countries,musician, ]

#print(main_list)
