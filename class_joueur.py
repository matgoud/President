#Création de la class Joueur

from class_deck import Deck
import config

class Joueur:
    
    #Initialisation de la class_joueur qui va nous permettre de créer un joueur et de lui attribuer un id, une main et les cartes qu'il a sélectionné
    def __init__(self,id):
        
        self.id = id
        self.main = Deck(config.DECK_VIDE)
        self.carte_selectionné = Deck(config.DECK_VIDE)
