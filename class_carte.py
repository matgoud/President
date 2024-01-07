#Création de la class Cartes

import pygame

class Cartes(pygame.sprite.Sprite): 
    
    #Création variable longeur/largeur
    height = 96 
    width = 71
    
    #Attribution d'une image pour le verso des cartes
    image_verso = pygame.image.load("images/images_cartes/verso.png")
    image_verso = pygame.transform.scale(image_verso,(71,96))
    
    #Liste nom et couleurs qui va nous servir pour la création du deck
    nom=["zero","3","4","5","6","7","8","9","10","Valet","reine","roi","As","2"]
    couleurs=["pique","coeur","carreau","trefle"]
    
    #Initilisation de la class_carte qui va nous permttre d'attribuer les propriétés d'une carte
    def __init__(self,val,nom,couleurs): 
        
        super().__init__()
        
        self.val = val
        self.nom = nom
        self.couleurs = couleurs
        self.rect = pygame.Rect(-500, -500, Cartes.height, Cartes.width)
        self.image_recto = pygame.image.load("images/images_cartes/" + self.__str__().replace(" ", "_") + ".png")
        pygame.draw.rect(Cartes.image_verso, (255,255,255), [0,0,71,96], 2)
        self.maj_image()
        
    #La fonction update va nous permettre d'attribuer les dimensions de chaque carte    
    def update(self): 
            
        self.image_recto = pygame.transform.scale(self.image_recto, (Cartes.width, Cartes.height))
        self.rect.height = Cartes.height
        self.rect.width  = Cartes.width
        self.maj_image()
        
    def maj_image(self):
        self.image = self.image_recto 
        
    def __str__(self):
        return str(self.nom) + " de " +str(self.couleurs)
