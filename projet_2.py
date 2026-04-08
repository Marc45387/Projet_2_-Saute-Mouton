from fltk import * 


class Interface:
    def __init__(self):
        """
        définir les variables 
        """
        self.HAUTEUR = 400 
        self.LONGUEUR = 400 
    
    def page_de_garde(self):
        """
        la page de départ avec un titre et quelque bouton
        """
        efface_tout 
        texte(180,40,'Saute Mouton', taille = 30)
        
        rectangle(210,200,400,150, couleur = 'black', remplissage = 'white')
        texte(220,160,'Commencer')

        rectangle(200,300,400,250, couleur = 'black', remplissage = 'white')
        texte(210,260,'Règle du jeu')

        while True:
            ev = attend_ev()
            tev = type_ev(ev)
            x,  y = abscisse(ev), ordonnee(ev)
            if tev == 'Quitte':
                ferme_fenetre()
            if tev == 'ClicGauche':
                if 200 <= x <= 400 and 200 <= y <= 150:
                    self.page_niveau()  
                if 200 <= x <= 400 and 300 <= y <= 250:
                    self.page_regle()
                mise_a_jour()
            

    def page_niveau(self):
        """
        page de niveau des étages
        """
        efface_tout
        texte(160,40,'Choix du niveaux', taille = 30)
        
        rectangle(100,140,500,350)
        rectangle(150,200,200,150, couleur = 'black', remplissage = 'white')
        
        rectangle(100,140,500,350)
        texte(320,370,'Continue')

        attend_ev()
        
        # à terminer

    def page_regle(self):
        """
        page des consignes et règle du jeu 
        """
        efface_tout
        rectangle(120,100,520,350,epaisseur = 3)
        
        rectangle(10,370,90,400)
        texte(20,380,'Retour')
        
        while True:
            ev = attend_ev()
            tev = type_ev(ev)
            x, y = abscisse(ev), ordonnee(ev)

        # à terminer

    def run(self):
        """
        lancement du création de la fenetre 
        """
        x, y  = self.LONGUEUR * 1.5, self.HAUTEUR  
        cree_fenetre(x,y)
        self.page_de_garde()

interface = Interface() 
interface.run()