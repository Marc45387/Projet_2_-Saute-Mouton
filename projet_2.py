from fltk import * 
from pathlib import Path 

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
        self.lst_bloc = [(60, 460, 200, 470),
                    (260, 360, 400, 370),
                    (60, 60, 200, 70),
                    (180, 260, 300, 270)]

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
                    self.page_niveau()
                    break 

                # zone de détecte 
                if 200 <= x <= 400 and 250 <= y <= 300:
                    self.page_regle()
                    break
            
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
                if 420 <= x <= 580 and  550 <= y <= 590:
                    self.page_jeu()
                
                if 130 <= x <= 170 and 110 <= y <= 150:
                    if not etat1:
                        texte(130,100,'X',tag= 'teste1',taille = 40)
                        etat1 = True
                    else:
                        efface('teste1')
                        etat1 = False
                
                if 130 <= x <= 170 and 210 <= y <= 250:
                    if not etat2:
                        texte(130,200,'X',tag= 'teste2',taille = 40)
                        etat2 = True
                    else:
                        efface('teste2')
                        etat2 = False
                if 130 <= x <= 170 and 310 <= y <= 350:
                    if not etat3:
                        texte(130,300,'X',tag= 'teste3',taille = 40)
                        etat3 = True
                    else:
                        efface('teste3')
                        etat3 = False
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
            rectangle(80,40,100,60,remplissage = 'yellow') # rectangle de point d'arrivé
            for m in self.lst_bloc:
                rectangle(m[0], m[1], m[2], m[3], remplissage='blue')
            if self.cible is not None:
                ligne(self.perso['x'] + 10, self.perso['y'] + 10, self.cible[0], self.cible[1], couleur='red', epaisseur=2)
            if self.perso_visible is not None:
                rectangle(self.perso["x"], self.perso["y"], self.perso["x"] + self.perso["w"], self.perso["y"] + self.perso["h"], remplissage='orange', tag='perso')

    def page_jeu(self):
        efface_tout()
        self.perso_visible = True
        while True:
            self.dessiner()
            ev = attend_ev()
            tev = type_ev(ev)

            if tev == 'Quitte':
                ferme_fenetre()
                break            

            if tev == 'ClicGauche':
                self.cible = (abscisse(ev), ordonnee(ev))
                ligne(self.perso['x'] + 10 ,self.perso['y'] + 10,abscisse(ev),ordonnee(ev))
                print(f"Visée fixée sur : {self.cible}")
                attend_ev()
            
            if tev == 'ClicDroit':
                self.cible = ((abscisse(ev),ordonnee(ev)))
                self.perso_visible = not self.perso_visible
                
                if not self.perso_visible:
                    efface('perso') 
            mise_a_jour()
    
    def run(self):
        """
        lancement du création de la fenetre 
        """
        x, y  = self.LONGUEUR * 1.5, self.HAUTEUR * 1.5  
        cree_fenetre(x,y)
        self.page_de_garde()

interface = Interface() 
interface.run()