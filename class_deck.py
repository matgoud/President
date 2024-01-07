#Création de la class Deck

from class_carte import Cartes
import config
from random import shuffle
import pygame

class Deck(pygame.sprite.Group):
    
    #Initialisation de la class_deck qui va nous permetrre de créer un paquet de 52 cartes ou un paquet vide selon le besoin grâce à la variable type
    def __init__(self,type=config.DECK_52): 
        super().__init__()
        
        self.paquet = []
        
        #Si type = DECK_VIDE alors le paquet reste vide
        if type==config.DECK_VIDE:
            
            pass
        
        #Si type = DECK_52 alors le paquet est remplit avec 52 cartes
        if type==config.DECK_52: 
            for i in range(1,14):
                for j in Cartes.couleurs:
                    car = Cartes(i+2, Cartes.nom[i], j)
                    self.paquet.append(car)
                    
    #La fonction mélanger qui va nous servir à mélanger un paquet      
    def mélanger(self):
        #Nous faisons appel à la fonction shuffle de la class_random de python qui permet de mélanger une liste
        shuffle(self.paquet)
        
    #La fonction tirer nous permet de tirer la dernière carte du paquet et de la retirer de celui ci
    def tirer(self): 
        carte = None
        if self.paquet:
            carte = self.paquet.pop()
            self.remove(carte)
        carte.rect.y = -500
        carte.rect.y = -500
        return carte
    
    #La fonction ajouter nous permet d'ajouter une carte dans un paquet ainsi que son sprite (image de la carte)
    def ajouter(self,c): 
        self.paquet.append(c)
        self.add(c)
        
    #La fonction enlever permet d'enlever una carte d'un paquet ainsi que son sprite (image de la carte)
    def enlever(self,c): 
        self.paquet.remove(c)
        self.remove(c)
        
    