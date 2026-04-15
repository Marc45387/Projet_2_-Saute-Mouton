from fltk import * 
from pathlib import Path 
from moteur import *
from time import *

BASE_DIR = Path(__file__).parent

class Interface:
    def __init__(self):
        """
        définir les variables 
        """
        self.HAUTEUR = 400 
        self.LONGUEUR = 400 
        self.perso = {"x": 100, "y": 575, "w": 20, "h": 20}    
        self.perso_visible = True
        self.cible = None
        self.mouton = Mouton(100,575)
        self.EPAISSEUR = 20
        self.arrivee = {"ax" : 80,"ay" : 40,"bx" : 100, "by" : 60}
        self.lst_bloc = [{"ax" : 60,"ay" : 460,"bx" : 200, "by" : 470},
                         {"ax" : 260,"ay" : 360,"bx" : 400, "by" : 370},
                         {"ax" : 60,"ay" : 60,"bx" : 200, "by" : 70},
                         {"ax" : 180,"ay" : 260,"bx" : 300, "by" : 270}]

    def page_de_garde(self):
        """
        la page de départ avec un titre et quelque bouton
        """
        efface_tout()  
        # titre
        texte(180, 40, 'Saute Mouton', taille=30)
        
        # boutons 
        rectangle(210, 150, 400, 200, couleur='black', remplissage='white')
        texte(220, 160, 'Commencer')
        rectangle(200, 250, 400, 300, couleur='black', remplissage='white')
        texte(210, 260, 'Règle du jeu')

        while True:
            ev = attend_ev()
            tev = type_ev(ev)
            
            if tev == 'Quitte':
                ferme_fenetre()
                break 
                
            if tev == 'ClicGauche':
                x, y = abscisse(ev), ordonnee(ev)
                
                if 210 <= x <= 400 and 150 <= y <= 200:
                    self.page_mode()
                    break 

                # zone de détecte 
                if 200 <= x <= 400 and 250 <= y <= 300:
                    self.page_regle()
                    break
            
            mise_a_jour()
    def page_mode(self):
        
        efface_tout()
        texte(150, 20, 'Choix du mode', taille=30)
        
        rectangle(90,70,510,430)
       
        # case de coche
        rectangle(130,110,170,150)
        rectangle(130,210,170,250)
        rectangle(130,310,170,350)
        
        # bouton retour et continue
        rectangle(10, 550, 140, 590)
        texte(30, 550, 'Retour')
        rectangle(420, 550, 580, 590)
        texte(430, 550, 'Continue')
        
        # texte
        texte(200,110,'Normal')
        texte(200,210,'Téléportation')
        texte(200,310,'Infinie')

        # variable à modifier 
        etat1 = False
        etat2 = False
        etat3 = False
        choix = None
        while True:
            ev = attend_ev()
            tev = type_ev(ev)
            if tev == 'Quitte':
                ferme_fenetre()
                break
            if tev == 'ClicGauche':
                x, y = abscisse(ev), ordonnee(ev)
                if 10 <= x <= 140 and 550 <= y <= 590:
                    self.page_de_garde()
                    break
                if 420 <= x <= 580 and  550 <= y <= 590 and choix is not None:
                    self.page_niveau()
                
                if 130 <= x <= 170 and 110 <= y <= 150:
                    if not etat1:
                        choix = 'normal'
                        texte(130,100,'X',tag= 'teste1',taille = 40)
                        etat1 = True
                    else:
                        efface('teste1')
                        etat1 = False
                if 130 <= x <= 170 and 210 <= y <= 250:
                    if not etat2:
                        choix = 'teleportation'
                        texte(130,200,'X',tag= 'teste2',taille = 40)
                        etat2 = True
                    else:
                        efface('teste2')
                        etat2 = False 
                if 130 <= x <= 170 and 310 <= y <= 350:
                    if not etat3:
                        choix = 'infinie'
                        texte(130,300,'X',tag= 'teste3',taille = 40)
                        etat3 = True
                    else:
                        efface('teste3')
                        etat3 = False
                if choix is None:
                    texte(90,450,'Veuillez choisir un mode de jeu \n         ' \
                    'pour continuer',couleur = 'red')
                mise_a_jour()

    def page_niveau(self):
        """
        page de choix des niveaux avec 3 carrés dessinés par une boucle
        """
        efface_tout()
        texte(150, 20, 'Choix du niveau', taille=30)
        
        rectangle(90,70,510,430)
       
        # case de coche
        rectangle(130,110,170,150)
        rectangle(130,210,170,250)
        rectangle(130,310,170,350)
        
        # bouton retour et continue
        rectangle(10, 550, 140, 590)
        texte(30, 550, 'Retour')
        rectangle(420, 550, 580, 590)
        texte(430, 550, 'Continue')
        
        # texte
        texte(200,110,'Niveau 0')
        texte(200,210,'Niveau 1')
        texte(200,310,'Niveau random')

        # variable à modifier 
        etat1 = False
        etat2 = False
        etat3 = False
        choix = None
        while True:
            ev = attend_ev()
            tev = type_ev(ev)
            if tev == 'Quitte':
                ferme_fenetre()
                break
            if tev == 'ClicGauche':
                x, y = abscisse(ev), ordonnee(ev)
                if 10 <= x <= 140 and 550 <= y <= 590:
                    self.page_mode()
                    break
                if 420 <= x <= 580 and  550 <= y <= 590 and choix is not None:
                    self.page_jeu()
                
                if 130 <= x <= 170 and 110 <= y <= 150:
                    if not etat1:
                        choix = 'niveau1'
                        texte(130,100,'X',tag= 'teste1',taille = 40)
                        etat1 = True
                    else:
                        efface('teste1')
                        etat1 = False
                
                if 130 <= x <= 170 and 210 <= y <= 250:
                    if not etat2:
                        choix = 'niveau2'
                        texte(130,200,'X',tag= 'teste2',taille = 40)
                        etat2 = True
                    else:
                        efface('teste2')
                        etat2 = False
                if 130 <= x <= 170 and 310 <= y <= 350:
                    if not etat3:
                        choix = 'random'
                        texte(130,300,'X',tag= 'teste3',taille = 40)
                        etat3 = True
                    else:
                        efface('teste3')
                        etat3 = False
                if choix is None:
                    texte(80,450,'Veuillez choisir un niveau', couleur = 'red')

                mise_a_jour()

    def page_regle(self):
        """
        page des consignes et règle du jeu 
        """
        efface_tout()
        img = BASE_DIR / "img/souris.png"
    
        rectangle(0,0,700,700,remplissage = 'white')
        rectangle(120,50,520,450,epaisseur = 3)
        
        rectangle(10,550,140,590)
        texte(20,550,'Retour')  

        
        image(320, 250, str(img), largeur=200, hauteur=200, ancrage='center')
        
        ligne(240,130,280,180)
        texte(200,90,'Viser')
        ligne(420,130,360,180)
        texte(400,90,'Sauter')
        
        while True:
            ev = attend_ev()
            tev = type_ev(ev)
            if tev == 'Quitte':
                ferme_fenetre()
                break
            if tev == 'ClicGauche':
                x, y = abscisse(ev), ordonnee(ev)
                if 10 <= x <= 140 and 550 <= y <= 590:
                    self.page_de_garde()
                    break
            mise_a_jour()

    def dessiner(self):
            efface_tout()
            # cadre global 
            rectangle(0, 0, 600, 600, epaisseur=8, couleur='red')
            rectangle(self.arrivee["ax"],self.arrivee["ay"],self.arrivee["bx"],self.arrivee["by"],remplissage = 'yellow') # rectangle de point d'arrivé
            for m in self.lst_bloc:
                rectangle(m["ax"], m["ay"], m["bx"], m["by"] , remplissage='blue')
                # DEBUG HITBOX BLOC : rectangle(m["ax"], m["ay"], m["ax"] + m["bx"], m["ay"] + m["by"], couleur='green', epaisseur=1)
            if self.cible is not None:
                centre_x = self.mouton.x + (self.mouton.LARGEUR / 2)
                centre_y = self.mouton.y + (self.mouton.HAUTEUR / 2)
                #ligne(self.perso['x'] + 10, self.perso['y'] + 10, self.cible[0], self.cible[1], couleur='red', epaisseur=2)
                dx = (self.cible[0] - centre_x) * 0.15 
                dy = (self.cible[1] - centre_y) * 0.15

                if dx > self.mouton.VMAX_X: dx = self.mouton.VMAX_X
                elif dx < -self.mouton.VMAX_X: dx = -self.mouton.VMAX_X
                
                if dy > self.mouton.VMAX_Y: dy = self.mouton.VMAX_Y
                elif dy < -self.mouton.VMAX_Y: dy = -self.mouton.VMAX_Y

                visuel_x = centre_x + (dx * 5)
                visuel_y = centre_y + (dy * 5)

                # On dessine la ligne qui montre le futur saut
                ligne(centre_x, centre_y, visuel_x, visuel_y, couleur='red', epaisseur=2)
                    
            if self.perso_visible is not None:
                #rectangle(self.perso["x"], self.perso["y"], self.perso["x"] + self.perso["w"], self.perso["y"] + self.perso["h"], remplissage='orange', tag='perso')
                rectangle(self.mouton.x, self.mouton.y, self.mouton.x + self.mouton.LARGEUR, self.mouton.y + self.mouton.HAUTEUR, remplissage='orange', tag='perso')

    def page_jeu(self):
        efface_tout()
        self.perso_visible = True
        self.mouton.victoire = False
        self.cible = None
        self.mouton.en_mouvement = False

        self.mouton.x = 100 
        self.mouton.y = 575
        self.mouton.vx = 0
        self.mouton.vy = 0
        efface_tout()
        while True:
            self.mouton.deplacer(self.lst_bloc, self.arrivee)
            self.dessiner()
            
            if self.mouton.victoire:
                rectangle(200,200,400,400,remplissage = 'white')
                texte(370, 200, "X", couleur='red', taille=30)
                texte(220,270,'Victoire',taille='40')
            ev = donne_ev()
            tev = type_ev(ev)

            if ev is not None:
                x,y = abscisse(ev), ordonnee(ev)
                
                if tev == 'Quitte':
                    ferme_fenetre()
                    break            
                
                if self.mouton.victoire:
                    if 370 <= x <= 400 and 200 <= y <= 230:
                        self.mouton.victoire = False
                        self.page_de_garde()
                        break 
                if not self.mouton.victoire:
                    if tev == 'ClicGauche' and self.mouton.en_mouvement == False: #( si on veut jouer saut par saut, enlever la 2eme conditon)
                        self.cible = (abscisse(ev), ordonnee(ev))
                        print(f"Visée fixée sur : {self.cible}")
        
                    if tev == 'ClicDroit':
                        if self.cible is not None:
                            self.mouton.impulsion(self.cible[0], self.cible[1])
                            print("SAUUUUUUT")
                            self.cible = None
            mise_a_jour()
            sleep(1/60)
    
    def run(self):
        """
        lancement du création de la fenetre 
        """
        x, y  = self.LONGUEUR * 1.5, self.HAUTEUR * 1.5  
        cree_fenetre(x,y)
        self.page_de_garde()

interface = Interface() 
interface.run()