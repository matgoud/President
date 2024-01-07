# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 13:11:52 2022

@author: gouda
"""

import pygame

pygame.mixer.init()
#Création de 3 channels son
pygame.mixer.set_num_channels(3)

#Création des musiques
musique_ambiance = pygame.mixer.Sound("son/son.mp3")
clic = pygame.mixer.Sound("son/son_clic.mp3")
totaly_spies = pygame.mixer.Sound("son/connard.mp3")

sound_snk = pygame.mixer.Sound("son/snk.mp3")
sound_hp = pygame.mixer.Sound("son/hp.mp3")    
sound_marvel = pygame.mixer.Sound("son/marvel.mp3")           
                              
canal_1 = pygame.mixer.Channel(0)
canal_2 = pygame.mixer.Channel(1)
canal_3 = pygame.mixer.Channel(2)