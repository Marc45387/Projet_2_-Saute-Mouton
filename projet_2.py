from fltk import * 
from pathlib import Path 
from moteur import *
from time import *

base = Path(__file__).parent

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
        img = base / "img/main_menu.png"
        # boutons 
        rectangle(210, 150, 400, 200, couleur='black', remplissage='white')
        texte(220, 160, 'Commencer')
        rectangle(200, 250, 400, 300, couleur='black', remplissage='white')
        texte(210, 260, 'Règle du jeu')
        image(300,300,str(img))

        while True:
            ev = attend_ev()
            tev = type_ev(ev)
            
            if tev == 'Quitte':
                ferme_fenetre()
                break 
                
            if tev == 'ClicGauche':
                x, y = abscisse(ev), ordonnee(ev)
                
                if 120 <= x <= 440 and 280 <= y <= 350:
                    self.page_mode()
                    break 

                # zone de détecte 
                if 120 <= x <= 440 and 370 <= y <= 440:
                    self.page_regle()
                    break
            mise_a_jour()

    def page_mode(self):

        efface_tout()

        img = base / "img/mode.png"
        image(300,300,str(img),hauteur = 600, largeur = 600)
       
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
                if 50 <= x <= 210 and 500 <= y <= 540:
                    self.page_de_garde()
                    break
                if 310 <= x <= 460 and  500 <= y <= 540 and choix is not None:
                    self.page_niveau()
                
                if 150 <= x <= 450 and 170 <= y <= 240:
                    if not etat1:
                        choix = 'normal'
                        texte(120,170,'▶',tag= 'teste1',taille = 40, couleur = 'red')
                        etat1 = True
                    else:
                        efface('teste1')
                        etat1 = False
                if 150 <= x <= 450 and 265 <= y <= 330:
                    if not etat2:
                        choix = 'teleportation'
                        texte(120,265,'▶',tag= 'teste2',taille = 40 , couleur = 'red')
                        etat2 = True
                    else:
                        efface('teste2')
                        etat2 = False 
                if 150 <= x <= 450 and 355 <= y <= 420:
                    if not etat3:
                        choix = 'infinie'
                        texte(120,355,'▶',tag= 'teste3',taille = 40,couleur = 'red')
                        etat3 = True
                    else:
                        efface('teste3')
                        etat3 = False
                if choix is None:
                    texte(90,460,'Veuillez choisir un mode de jeu', couleur = 'red', taille = 20)
                mise_a_jour()

    def page_niveau(self):
        """
        page de choix des niveaux avec 3 carrés dessinés
        """
        efface_tout()
        texte(150, 20, 'Choix du niveau', taille=30)
        
        img = base / "img/niveau.png"
        image(300,300,str(img),hauteur = 600, largeur = 600)

        # variable à modifier 
        choix = None
        while True:
            ev = attend_ev()
            tev = type_ev(ev)
            if tev == 'Quitte':
                ferme_fenetre()
                break
            if tev == 'ClicGauche':
                x, y = abscisse(ev), ordonnee(ev)
                if 50 <= x <= 200 and 490 <= y <= 530:
                    self.page_mode()
                    break
                
                # à compléter
                if 100 <= x <= 490 and  180 <= y <= 280:
                    self.page_jeu()
                    break
                
                # niveau ramdom à ajouter 
                if 130 <= x <= 170 and 210 <= y <= 250:
                   pass

                if choix is None:
                    texte(80,450,'Veuillez choisir un niveau', couleur = 'red')

                mise_a_jour()

    def page_regle(self):
        """
        page des consignes et règle du jeu 
        """
        efface_tout()
        img = base / "img/page_regle.png"        
        image(300, 300, str(img), largeur=600, hauteur=600, ancrage='center')
        # rectangle(50,510,210,560)
        while True:
            ev = attend_ev()
            tev = type_ev(ev)
            if tev == 'Quitte':
                ferme_fenetre()
                break
            if tev == 'ClicGauche':
                x, y = abscisse(ev), ordonnee(ev)
                if 50 <= x <= 210 and 510 <= y <= 560:
                    self.page_de_garde()
                    break
            mise_a_jour()

    def dessiner(self):
            efface_tout()
            img = base / "img/mouton.png"
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
                image(self.mouton.x,self.mouton.y + 7,str(img))

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