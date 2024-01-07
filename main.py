
from president import President
import pygame
import image
import texte
import couleur
import bruitage
import bouton
from class_carte import Cartes

if __name__ == "__main__":
    
    pygame.init()
    
    FPS = 144

    game = President()
    son = bruitage
    
    pygame.display.set_caption("PRESIDENT")
    screen = pygame.display.set_mode((1080,720)) 
    
    #Variables permettant d'ouvrir différentes fenêtres durant la partie
    running_menu = True
    running_game = False
    running_joueur_suivant = False
    running_paramètre = False
    running_fin_game = False
    
    clock = pygame.time.Clock()

    background = image.background_bleu
    image_son = image.son_open
    
    background2 = image.background_bleu

    son.canal_1.play(bruitage.musique_ambiance)
    sound_playing = True
   
    while running_menu:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                
                running_menu = False
            
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_p :
                    
                    son.canal_3.play(son.totaly_spies)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
            
                mouse_position = pygame.mouse.get_pos()
                
                
                if (bouton.Play.collidepoint(mouse_position)):
                    
                    son.canal_2.play(son.clic)
                    running_joueur_suivant = True
                    running_menu = False
                    j1 = texte.police1.render ("JOUEUR 1", 1 , (0,0,0))
                
                elif (bouton.Thème_snk.collidepoint(mouse_position)):
                    
                    background = image.background_snk
                    Cartes.image_verso = pygame.image.load("images/images_cartes/snk_verso.jpg")
                    Cartes.image_verso = pygame.transform.scale(Cartes.image_verso,(71,96))
                    pygame.draw.rect(Cartes.image_verso, (255,255,255), [0,0,71,96], 1)
                    background2 = image.vert
                    son.canal_1.play(bruitage.sound_snk)
                    son.canal_2.play(son.clic)
                
                elif (bouton.Thème_harrypotter.collidepoint(mouse_position)):
                    
                    background = image.hp
                    Cartes.image_verso = pygame.image.load("images/images_cartes/verso_hp.png")
                    Cartes.image_verso = pygame.transform.scale(Cartes.image_verso,(71,96))
                    pygame.draw.rect(Cartes.image_verso, (255,255,255), [0,0,71,96], 1)
                    background2 = image.hp2
                    son.canal_1.play(bruitage.sound_hp)
                    son.canal_2.play(son.clic)
                
                elif (bouton.Thème_marvel.collidepoint(mouse_position)):
                    
                    background = image.marvel
                    Cartes.image_verso = pygame.image.load("images/images_cartes/verso_marvel.png")
                    Cartes.image_verso = pygame.transform.scale(Cartes.image_verso,(71,96))
                    pygame.draw.rect(Cartes.image_verso, (255,255,255), [0,0,71,96], 1)
                    background2 = image.marvel2
                    son.canal_1.play(bruitage.sound_marvel)
                    son.canal_2.play(son.clic)
                
                elif (bouton.Thème_basique.collidepoint(mouse_position)):
                    
                    background = image.background_bleu
                    Cartes.image_verso = pygame.image.load("images/images_cartes/verso.png")
                    Cartes.image_verso = pygame.transform.scale(Cartes.image_verso,(71,96))
                    pygame.draw.rect(Cartes.image_verso, (255,255,255), [0,0,71,96], 1)
                    background2 = image.background_bleu
                    son.canal_1.play(bruitage.musique_ambiance)
                    son.canal_2.play(son.clic)
                                   
        screen.blit(background2,(0,0))
        screen.blit(image.bouton_play,(454,370))
        screen.blit(texte.president, (290,220))    
        screen.blit(image.coeur,(355,200))
        screen.blit(image.diamant,(555,200))
        screen.blit(image.trefle,(455,200))
        screen.blit(image.pique,(655,200))
        screen.blit(texte.snk,(60,595))
        screen.blit(texte.harry,(300,630))
        screen.blit(texte.marvel,(595,620))
        screen.blit(texte.basique,(870,615))
        
        pygame.draw.rect(screen , couleur.rect_colour, bouton.Thème_snk, 4)
        pygame.draw.rect(screen , couleur.rect_colour, bouton.Thème_harrypotter, 4)
        pygame.draw.rect(screen , couleur.rect_colour, bouton.Thème_marvel, 4)
        pygame.draw.rect(screen , couleur.rect_colour, bouton.Thème_basique, 4)
        
        clock.tick(FPS)
        pygame.display.flip()   
    
    while running_joueur_suivant:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                
                running_joueur_suivant = False
            
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_p :
                    
                    son.canal_3.play(son.totaly_spies)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                if event.button == 1:
                    
                    running_game = True
                    running_joueur_suivant = False
                    son.canal_2.play(son.clic)
        
        screen.blit(background2,(0,0))
        screen.blit(texte.commence,(380,350))
        screen.blit(j1,(310,250))
        screen.blit(image.joueur_grand[0],(480,420))
        
        clock.tick(FPS)
        pygame.display.flip() 
                    
    while running_game:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                
                running_game = False
                
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_p :
                    
                    son.canal_3.play(son.totaly_spies)
                        
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                mouse_position = pygame.mouse.get_pos()
                game.carte_select(mouse_position)
                
                if (bouton.Jouer.collidepoint(mouse_position)):
                    
                    son.canal_2.play(son.clic)
                    
                    #Si le joueur à sélectionné des cartes alors on regarde si la fonction renvoit True/False affin d'afficher le bon texte à l'écran
                    if len(game.liste_joueur[game.joueur_en_cours-1].carte_selectionné) != 0:
                        
                        v = game.liste_joueur[game.joueur_en_cours-1].carte_selectionné.paquet[0].val
                                            
                        if game.jouer_cartes() == True:
                            
                            game.dernier_joueur = game.joueur_en_cours
                            texte.suivant = texte.suivant_bis
                            x=380
                            y=250
                            game.joueur_suivant()
                        
                        else:
                            
                            if v==15:
                            
                                texte.suivant = texte.fermeture_par
                                x=240
                                y=250
                                                      
                            else:
                                                               
                                texte.suivant = texte.impossible
                                x=380
                                y=250
                                
                    #Si le joueur n'a pas sélectionné de carte alors on passe juste au joueur suivant        
                    else:
    
                        game.joueur_suivant()
                        texte.suivant = texte.suivant_bis
                        x=380
                        y=250
                        
                        #Condition permettant de fermer automatiquement le tour si dernier joueur à avoir jouer est le joueur en cours
                        if game.dernier_joueur == game.joueur_en_cours:
                            
                            game.fermer_tour()
                            texte.suivant = texte.fermeture_tour
                            x=290
                            y=250
                    
                    #On regarde si un joueur n'a plus de carte afin de passer son tour automatiquement et ne plus afficher que c'est à lui de jouer
                    game.main_vide()
                    running_joueur_suivant = True
                    
                    #on regarde si 3 des 4 joueurs n'ont plus de carte dans le but de lancer l'écran de fin de partie
                    if game.fin_game()==True:
                        
                        running_fin_game = True
            
                        while running_fin_game:
                            
                            for event in pygame.event.get():
                                
                                if event.type == pygame.QUIT:
                                    
                                    running_fin_game = False
                                    running_game = False
                                    running_joueur_suivant = False
                                    
                                elif event.type == pygame.KEYDOWN:
                                    
                                    if event.key == pygame.K_p :
                                        
                                        son.canal_3.play(son.totaly_spies)
                                
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                    
                                    mouse_position = pygame.mouse.get_pos()
                                    
                                    if (bouton.fin_game.collidepoint(mouse_position)):
                                        
                                        son.canal_2.play(son.clic)
                                        running_fin_game = False
                                        running_game = False
                                        running_joueur_suivant = False
                            
                            screen.blit(background2,(0,0))
                            screen.blit(texte.merci,(220,220))
                            screen.blit(texte.quitter,(442,410))
                            pygame.draw.rect(screen,couleur.rect_colour,bouton.fin_game,2)
                                
                            clock.tick(FPS)
                            pygame.display.flip()
                    
                    joueur = texte.police1.render ("JOUEUR " +  game.joueur_en_cours.__str__(), 1 , (0,0,0))
                    image_joueur = image.joueur_grand[game.joueur_en_cours-1]
                        
                    while running_joueur_suivant:
                        
                        for event in pygame.event.get():
                            
                            if event.type == pygame.QUIT:
                                
                                running_joueur_suivant = False
                                running_game = False
                            
                            elif event.type == pygame.KEYDOWN:
                                
                                if event.key == pygame.K_p :
                                    
                                    son.canal_3.play(son.totaly_spies)
                            
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                
                                if event.button == 1:
                                    
                                    son.canal_2.play(son.clic)
                                    running_joueur_suivant = False
                        
                            screen.blit(background2,(0,0))
                            screen.blit(image_joueur,(480,420))
                            screen.blit(joueur,(310,300))
                            screen.blit(texte.suivant,(x,y))
                            clock.tick(FPS)
                            pygame.display.flip()  
                
                elif (bouton.Paramètre.collidepoint(mouse_position)):
                    
                    son.canal_2.play(son.clic)
                    running_paramètre = True
                    
                    while running_paramètre:
                        
                        for event in pygame.event.get():
                            
                            if event.type == pygame.QUIT:
                                
                                running_paramètre = False
                                running_game = False       
                            
                            elif event.type == pygame.KEYDOWN:
                                
                                if event.key == pygame.K_p :
                                    
                                    son.canal_3.play(son.totaly_spies)
                            
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                
                                mouse_position = pygame.mouse.get_pos()
                                
                                if (bouton.Exit.collidepoint(mouse_position)):
                                    
                                    son.canal_2.play(son.clic)
                                    running_paramètre = False
                                
                                elif (bouton.Thème_snk.collidepoint(mouse_position)):
                                    
                                    background = image.background_snk
                                    Cartes.image_verso = pygame.image.load("images/images_cartes/snk_verso.jpg")
                                    Cartes.image_verso = pygame.transform.scale(Cartes.image_verso,(71,96))
                                    pygame.draw.rect(Cartes.image_verso, (255,255,255), [0,0,71,96], 1)
                                    background2 = image.vert
                                    son.canal_1.play(bruitage.sound_snk)
                                    son.canal_2.play(son.clic)
                                
                                elif (bouton.Thème_harrypotter.collidepoint(mouse_position)):
                                    
                                    background = image.hp
                                    Cartes.image_verso = pygame.image.load("images/images_cartes/verso_hp.png")
                                    Cartes.image_verso = pygame.transform.scale(Cartes.image_verso,(71,96))
                                    pygame.draw.rect(Cartes.image_verso, (255,255,255), [0,0,71,96], 1)
                                    background2 = image.hp2
                                    son.canal_1.play(bruitage.sound_hp)
                                    son.canal_2.play(son.clic)
                                
                                elif (bouton.Thème_marvel.collidepoint(mouse_position)):
                                    
                                    background = image.marvel
                                    Cartes.image_verso = pygame.image.load("images/images_cartes/verso_marvel.png")
                                    Cartes.image_verso = pygame.transform.scale(Cartes.image_verso,(71,96))
                                    pygame.draw.rect(Cartes.image_verso, (255,255,255), [0,0,71,96], 1)
                                    background2 = image.marvel2
                                    son.canal_1.play(bruitage.sound_marvel)
                                    son.canal_2.play(son.clic)
                                
                                elif (bouton.Thème_basique.collidepoint(mouse_position)):
                                    
                                    background = image.background_bleu
                                    Cartes.image_verso = pygame.image.load("images/images_cartes/verso.png")
                                    Cartes.image_verso = pygame.transform.scale(Cartes.image_verso,(71,96))
                                    pygame.draw.rect(Cartes.image_verso, (255,255,255), [0,0,71,96], 1)
                                    background2 = image.background_bleu
                                    son.canal_1.play(bruitage.musique_ambiance)
                                    son.canal_2.play(son.clic)
                        
                        screen.blit(background2,(0,0))
                        screen.blit(image.retour,(1000,20))
                        screen.blit(texte.snk,(60,595))
                        screen.blit(texte.harry,(300,630))
                        screen.blit(texte.marvel,(595,620))
                        screen.blit(texte.basique,(870,615))
                        screen.blit(texte.règle1,(230,100))
                        screen.blit(texte.règle2,(230,140))
                        screen.blit(texte.règle3,(230,180))
                        screen.blit(texte.règle4,(230,220))
                        screen.blit(texte.règle5,(230,260))
                        screen.blit(texte.règle6,(230,300))
                        screen.blit(texte.règle7,(230,340))
                        screen.blit(texte.règle8,(230,380))
                        screen.blit(texte.règle9,(230,420))
                        screen.blit(texte.règle10,(230,460))
                        screen.blit(texte.règle11,(230,500))
                        screen.blit(texte.règle12,(230,540))
                        
                        pygame.draw.rect(screen , couleur.rect_colour, bouton.Thème_snk, 4)
                        pygame.draw.rect(screen , couleur.rect_colour, bouton.Thème_harrypotter, 4)
                        pygame.draw.rect(screen , couleur.rect_colour, bouton.Thème_marvel, 4)
                        pygame.draw.rect(screen , couleur.rect_colour, bouton.Thème_basique, 4)
                        
                        pygame.draw.rect (screen, couleur.rect_colour, bouton.Exit, 3)
                        clock.tick(FPS)
                        pygame.display.flip()
                        
                elif (bouton.Son.collidepoint(mouse_position)):
                    
                    son.canal_2.play(son.clic)
                    
                    if sound_playing:
                        
                        son.canal_1.pause()
                        image_son = image.son_close
                        
                    else:
                        
                        son.canal_1.unpause()
                        image_son = image.son_open
                    
                    sound_playing = not sound_playing

            screen.blit(background,(0,0))    
            pos_petits = [(516,150),(182,336),(516,522),(850,336)]
            for i in range(len(pos_petits)):
                screen.blit(image.joueur_petit[i], pos_petits[i])
            screen.blit(texte.jouer,(867,610))
            screen.blit(texte.passer,(869,640))
            screen.blit(texte.slash,(913.125,625))
            screen.blit(image.règle,(1001,21))
            screen.blit(image_son,(30,20))
            
            pygame.draw.rect (screen, couleur.rect_colour, bouton.Jouer, 3)
            pygame.draw.rect (screen, couleur.rect_colour, bouton.Paramètre, 2)
            pygame.draw.rect (screen, couleur.rect_colour, bouton.Son, 2)

            game.display_all(screen)
            clock.tick(FPS)
            pygame.display.flip() 
        
    pygame.quit()
    print("Fermeture du jeu")