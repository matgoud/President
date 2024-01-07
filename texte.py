# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 10:34:15 2022

@author: gouda
"""

import pygame
import couleur

pygame.init()

#On définit nos polices ainsi que leur taille
police1 = pygame.font.Font("police/Baloo-Regular.ttf", 100)
police2 = pygame.font.Font("police/Baloo-Regular.ttf", 50)
police3 = pygame.font.Font("police/Baloo-Regular.ttf", 15)
police4 = pygame.font.Font("police/snk.TTF",100)
police5 = pygame.font.Font("police/hp.TTF",50)
police6 = pygame.font.Font("police/Avengers.otf",50)
police7 = pygame.font.Font("police/Baloo-Regular.ttf", 20)

#Création de différents texte à afficher durant la partie
president = police1.render ("PRESIDENT", 1 , couleur.rect_colour)
vide = police1.render ("", 1 , couleur.rect_colour)
jouer = police3.render ("JOUER CARTES", 1 , couleur.rect_colour)
passer = police3.render ("PASSER TOUR", 1 , couleur.rect_colour)
slash = police3.render ("/", 1 , couleur.rect_colour)
texte7 = police1.render ("", 1 , couleur.rect_colour)
commence = police2.render ("COMMENCE", 1 , couleur.rect_colour)
suivant = police2.render("AU TOUR DU", 1 , couleur.rect_colour)
fermeture_par = police2.render("FERMETURE DU TOUR PAR:", 1 , couleur.rect_colour)
suivant_bis = police2.render("AU TOUR DU", 1 , couleur.rect_colour)
impossible = police2.render("IMPOSSIBLE:", 1 , couleur.rect_colour)
fermeture_tour = police2.render("FERMETURE DU TOUR", 1 , couleur.rect_colour)
snk = police4.render ("snk", 1 , couleur.rect_colour)
harry = police5.render ("Harry Potter", 1 ,couleur.rect_colour)
marvel = police6.render("Avengers", 1 ,couleur.rect_colour)
basique = police2.render("Basique", 1 ,couleur.rect_colour)
merci =  police1.render("FIN DE PARTIE", 1 , couleur.rect_colour)
quitter = police2.render("QUITTER", 1 , couleur.rect_colour)

règle1  = police7.render("Les cartes sont hiérarchisées de la façon suivante :", 1 ,couleur.rect_colour)
règle2  = police7.render("| 2 | As | Roi | Dame | Valet | 10 | 9 | … | 3 |", 1 ,couleur.rect_colour)
règle3  = police7.render("Le 2 étant la carte la plus forte et le 3 la plus faible.", 1 ,couleur.rect_colour)
règle4  = police7.render("Si le joueur 1 pose une carte simple,", 1 ,couleur.rect_colour)
règle5  = police7.render("le joueur 2 (et les suivants) doit poser une carte supérieure.", 1 ,couleur.rect_colour)
règle6  = police7.render("Si le joueur 1 pose une paire, c’est-à-dire deux cartes de même chiffre,", 1 ,couleur.rect_colour)
règle7  = police7.render("le joueur 2 (et les suivants) doit également jouer avec deux cartes,", 1 ,couleur.rect_colour)
règle8  = police7.render("qui ont le même chiffre mais toujours supérieures aux cartes précédentes.", 1 ,couleur.rect_colour)
règle9  = police7.render("La même règle s’applique pour trois et quatre cartes du même chiffre.", 1 ,couleur.rect_colour)       
règle10 = police7.render("Quand un 2 est joué alors le tour se ferme automatiquement.", 1 ,couleur.rect_colour)  
règle11 = police7.render("Quand les 4 dernières cartes de la défausse,", 1 ,couleur.rect_colour) 
règle12 = police7.render("sont de même hauteur le tour se ferme automatiquement.", 1 ,couleur.rect_colour)
