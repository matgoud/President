#Création de la class_president

from class_deck import Deck
from class_joueur import Joueur
from class_carte import Cartes
import config
import pygame
import bruitage

class President:

    def __init__(self):

        self.all_cartes = pygame.sprite.Group()
        self.defausse = Deck(config.DECK_VIDE)
        self.pioche = Deck(config.DECK_52)
        self.liste_joueur = []
        self.selected_carte = None
        self.all_cartes.add(self.pioche)
        self.nb_carte_tour = 1
        self.dernier_joueur = 0
        
        #Création de nos 4 joueurs et de leurs main
        self.pioche.mélanger()
        id_joueur=[1,2,3,4]
        for u in id_joueur:
            j = Joueur(u)
            for g in range (0,13):
                carte = self.pioche.tirer()
                j.main.ajouter(carte)
            self.liste_joueur.append(j)
        
        #Création de la variable joueur_en_cours qui va nous permettre pendant la partie de savoir quel joueur est entrain de jouer
        self.joueur_en_cours  = self.liste_joueur[0].id  
    
    #La fonction dessine_main_joueur va nous permettre de dessiner les cartes de la main d'un joueur
    #Elle parcourt la main du joueur est dessine chaque carte
    def dessine_main_joueur (self,x,y,joueur,screen):
        
        main = joueur.main
        joueur_en_cours = (joueur.id == self.joueur_en_cours)
        id = joueur.id
        
        #Si l'id du joueur est paire alors chaque carte dessinée est décalée de 30 en y
        #Si l'id du joueur est impaire alors chaque carte dessinée est décalée de 30 en x
        
        if id%2 == 0:
            
            dx = 0
            dy = 30
            
        else:
            
            dx = 30
            dy = 0
            
        for carte in main:
            
            if joueur_en_cours == False:
                
                carte.image = Cartes.image_verso
                
            else : 
                
                carte.image = carte.image_recto
                
            carte.rect.x = x
            carte.rect.y = y
            x += dx
            y += dy            
            
            #Condition qui va permettre de bouger les cartes sélectionnées
            #En fonction de l'id (paire ou impaire) c'est le x ou le y qui est modiffié
            
            if carte in self.liste_joueur[self.joueur_en_cours-1].carte_selectionné and self.joueur_en_cours == 1:
                carte.rect.y -= 25
            
            elif carte in self.liste_joueur[self.joueur_en_cours-1].carte_selectionné and self.joueur_en_cours == 2:
                carte.rect.x += 25
                
            elif carte in self.liste_joueur[self.joueur_en_cours-1].carte_selectionné and self.joueur_en_cours == 3:
                carte.rect.y -= 25
                
            elif carte in self.liste_joueur[self.joueur_en_cours-1].carte_selectionné and self.joueur_en_cours == 4:
                carte.rect.x -= 25          
                        
        main.draw(screen)
    
    #La fonction display_main_joueur fait appelle à la fonction dessine_main_joueur, elle va nous permettre de dessiner les mains de nos 4 joueurs
    def display_main_joueur(self, screen):
        
        #Les variables x,y de la fonction dessine_main_joueurs sont dynamiques en fonction de l'id du joueurs
        #Le fait qu'elles soient dynamiques va permettre que la main du joueur soit toujours centré grâce à la formule suivante: 
        #(longeur ou largeur (selon l'id) de l'écran/2)-((longeur ou largeur (selon l'id) d'une carte + la longeur de la main du joueur*30)/2)
        self.dessine_main_joueur((screen.get_width()/2) - ((Cartes.width + len(self.liste_joueur[0].main.paquet)*30)/2),50,self.liste_joueur[0],screen)
        self.dessine_main_joueur(109,(screen.get_height()/2) - ((Cartes.height + len(self.liste_joueur[1].main.paquet)*30)/2),self.liste_joueur[1],screen)
        self.dessine_main_joueur((screen.get_width()/2) - ((Cartes.width + len(self.liste_joueur[2].main.paquet)*30)/2),574,self.liste_joueur[2],screen)
        self.dessine_main_joueur(900,(screen.get_height()/2) - ((Cartes.height + len(self.liste_joueur[3].main.paquet)*30)/2),self.liste_joueur[3],screen)
    
    #La fonction display_dessine_defausse permet de dessiner les cartes de la defausse
    def display_dessine_defausse(self,screen):
        
        x = 512
        y = 290
        cpt = 0
        
        if len(self.defausse.paquet)==0:
            
            pass
        
        else:
            
            for carte in self.defausse:
                
                a=len(self.defausse)
                carte.image = carte.image_recto
                carte.rect.x = x
                carte.rect.y = y
                
                if a != len(self.defausse):
                    
                    carte.rect.x = x
                    carte.rect.y = y
                    a=len(self.defausse)
                    
                x += 15
                cpt+=1
                
                #Permet de ragarder si le nombre de carte jouée correspond au nb_carte_tour et alors de décaler l'affichage des prochaines cartes
                #Dans le but que les cartes joueés ne cache pas les cartes jouées précedement
                if cpt%self.nb_carte_tour == 0:
                    
                    y+= 15
                    x=512
                    
        self.defausse.draw(screen)
    
    #La fonction display_all nous permet d'utiliser les deux fonctions en même temps
    def display_all(self, screen):

        self.display_main_joueur(screen)
        self.display_dessine_defausse(screen)    
    
    #La fonction joueur_suivant permet de changer de joueur
    def joueur_suivant(self):
        
        if self.joueur_en_cours == 4:
                
            self.joueur_en_cours  = 1
            self.liste_joueur[self.joueur_en_cours-1].carte_selectionné = Deck(config.DECK_VIDE)                   
            
        else:
            
            self.liste_joueur[self.joueur_en_cours].carte_selectionné = Deck(config.DECK_VIDE)
            self.joueur_en_cours  = self.joueur_en_cours + 1         
    
    #La fonction carte_select permet au joueur_en_cours de sélectionner les cartes de sa main            
    def carte_select (self, mouse_position):
        
        liste = []
        carte2 = None
        
        for carte in self.liste_joueur[self.joueur_en_cours-1].main.paquet:
           
           if carte.rect.collidepoint(mouse_position):
             
                liste.append(carte)
                carte2 = liste.pop()
                #Cella permet d'attribuer un bruit quand on clic sur carte
                bruitage.canal_2.play(bruitage.clic)
            
        if carte2 != None:
            
            #Si la carte est déja sélectionner alors on la déselectionne 
            if carte2 in self.liste_joueur[self.joueur_en_cours-1].carte_selectionné:
                
                    self.liste_joueur[self.joueur_en_cours-1].carte_selectionné.enlever(carte2)
            
            else:
                
                if self.liste_joueur[self.joueur_en_cours-1].carte_selectionné.paquet != []:
                    
                    #Si la valeur de la carte sélectionner est différente de la valeur de la première carte sélectionner alors la première carte sélectionner
                    #est automatiquement déselectionner et la seconde est sélectionner
                    if carte2.val !=  self.liste_joueur[self.joueur_en_cours-1].carte_selectionné.paquet[0].val:
                        
                        while len(self.liste_joueur[self.joueur_en_cours-1].carte_selectionné.paquet)!=0:
                                
                            self.liste_joueur[self.joueur_en_cours-1].carte_selectionné.enlever(self.liste_joueur[self.joueur_en_cours-1].carte_selectionné.paquet[0])
                
                self.liste_joueur[self.joueur_en_cours-1].carte_selectionné.ajouter(carte2)
      
    #La fonction jouer_cartes permet au joueur_en_cours de jouer les cartes qu'il a sélectionné
    def jouer_cartes (self):  
         
        if len(self.defausse) == 0:
            
            #Permet d'établir le nombre de carte à jouer dans le tour (simple,paire,brelan)
            self.nb_carte_tour = len(self.liste_joueur[self.joueur_en_cours - 1].carte_selectionné)
            
            v=self.liste_joueur[self.joueur_en_cours-1].carte_selectionné.paquet[0].val
            
            #Si la valeur de la carte est différente de 15 alors la carte apparaît dans la defausse
            if v != 15:
                
                for i in range (0,len(self.liste_joueur[self.joueur_en_cours-1].carte_selectionné)):
                        
                    c = self.liste_joueur[self.joueur_en_cours-1].carte_selectionné.tirer()
                    self.defausse.ajouter(c)
                    self.liste_joueur[self.joueur_en_cours-1].main.enlever(c)
            
            #Si la valeur de la carte est égale à 15 alors la defausse est vider est le joueur en cours ne change pas
            else:
                
                for i in range (0,len(self.liste_joueur[self.joueur_en_cours-1].carte_selectionné)):
                    
                    c = self.liste_joueur[self.joueur_en_cours-1].carte_selectionné.tirer()
                    self.defausse.ajouter(c)
                    self.liste_joueur[self.joueur_en_cours-1].main.enlever(c)
                    
                self.fermer_tour()
                return False

        else :
            
            if len(self.liste_joueur[self.joueur_en_cours-1].carte_selectionné) == self.nb_carte_tour and self.liste_joueur[self.joueur_en_cours-1].carte_selectionné.paquet[0].val >= self.defausse.paquet[len(self.defausse)-1].val:
                
                v=self.liste_joueur[self.joueur_en_cours-1].carte_selectionné.paquet[0].val
                
                if v!= 15:
                    
                    for i in range (0,len(self.liste_joueur[self.joueur_en_cours-1].carte_selectionné)):
                        
                        c = self.liste_joueur[self.joueur_en_cours-1].carte_selectionné.tirer()
                        self.defausse.ajouter(c)
                        self.liste_joueur[self.joueur_en_cours-1].main.enlever(c)
                
                else :
                    
                    for i in range (0,len(self.liste_joueur[self.joueur_en_cours-1].carte_selectionné)):
                        
                        c = self.liste_joueur[self.joueur_en_cours-1].carte_selectionné.tirer()
                        self.defausse.ajouter(c)
                        self.liste_joueur[self.joueur_en_cours-1].main.enlever(c)
                        
                    self.fermer_tour()
                    
                    return False
                
            #Si le nombre de cartes jouées est différent de nb_carte_tour alors les cartes sélectionnées du joueur sont vidées et il peut rejouer
            else:
                
                while len(self.liste_joueur[self.joueur_en_cours-1].carte_selectionné.paquet)!=0:
                    
                    self.liste_joueur[self.joueur_en_cours-1].carte_selectionné.enlever(self.liste_joueur[self.joueur_en_cours-1].carte_selectionné.paquet[0])

                return False
                
        y = len(self.defausse)
        
        #Si la valeur des 4 dernières cartes de la defausse est la même alors le tour est fermé automatiquement 
        if len(self.defausse) >= 4 and self.defausse.paquet[y-1].val == self.defausse.paquet[y-2].val == self.defausse.paquet[y-3].val == self.defausse.paquet[y-4].val:
            
            self.fermer_tour()
            
            return False
        
        return True
    
    #La fonction fermer_tour permet de vider la defausse
    def fermer_tour (self) :
        
        if len(self.defausse) != 0:
            
            while len(self.defausse)!=0:
                
                self.defausse.enlever(self.defausse.paquet[0])
    
    #la fonction fin_game regarde si 3 joueurs n'ont plus de cartes et nous permet alors de lancer l'écran de fin de partie
    def fin_game(self):
        
        if len(self.liste_joueur[0].main) == 0 and len(self.liste_joueur[1].main) == 0 and len(self.liste_joueur[2].main) == 0:
            
            return True
        
        elif len(self.liste_joueur[0].main) == 0 and len(self.liste_joueur[1].main) == 0 and len(self.liste_joueur[3].main) == 0:
            
            return True
            
        elif len(self.liste_joueur[0].main) == 0 and len(self.liste_joueur[2].main) == 0 and len(self.liste_joueur[3].main) == 0:
            
            return True
            
        elif len(self.liste_joueur[1].main) == 0 and len(self.liste_joueur[2].main) == 0 and len(self.liste_joueur[3].main) == 0:
            
            return True
    
    #La fonction main_vide permet que si un joueur n'a plus de carte alors on passe automatiquement au joueur suivant
    #Elle permet aussi que si le dernier joueur à avoir joué n'a plus de carte alors le tour se ferme automatiquement
    def main_vide(self):
        
        for i in range (0,4):
            if len(self.liste_joueur[i].main) == 0 and self.joueur_en_cours == self.liste_joueur[i].id:
                self.joueur_suivant()
                
        for i in range (0,4):
            if len(self.liste_joueur[i].main) == 0 and self.dernier_joueur == self.liste_joueur[i].id:
                self.fermer_tour()