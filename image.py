# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 10:22:29 2022

@author: gouda
"""

import pygame

#Création de toutes les images

background_bleu = pygame.image.load('images/background/fond_bleu.jpg')
background_bleu = pygame.transform.scale(background_bleu,(1080,720))

background_snk = pygame.image.load("images/background/fondSNK.png")
background_snk = pygame.transform.scale(background_snk,(1080,720))
vert = pygame.image.load("images/background/fondColossal.png")

hp = pygame.image.load("images/background/fondhp.png")
hp = pygame.transform.scale(hp,(1080,720))
hp2 = pygame.image.load("images/background/fondhp2.jpeg")

marvel = pygame.image.load("images/background/fondAvengers.png")
marvel2 = pygame.image.load("images/background/fondAvengers2.png")

boite_de_nuit = pygame.image.load("images/background/boite.jpg")

joueur_petit = []
for i in range(1,5):
    joueur_petit.append(pygame.image.load ("images/images_joueurs/joueur"+str(i)+".png"))

joueur_grand = []
for i in range(1,5):
    joueur_grand.append(pygame.image.load ("images/images_joueurs/joueur"+str(i)+"_grand.png"))
    
son_open = pygame.image.load("images/images_son/son_open.png")
son_close = pygame.image.load("images/images_son/son_close.png")

coeur = pygame.image.load("images/images_icones/coeur.png")
diamant = pygame.image.load("images/images_icones/diamant.png")
trefle = pygame.image.load("images/images_icones/trefle.png")
pique = pygame.image.load("images/images_icones/pique.png")

règle = pygame.image.load("images/images_icones/parametre.png")
retour = pygame.image.load("images/images_icones/parametre2.png")

bouton_play = pygame.image.load('images/images_bouton/bouton_play.png')