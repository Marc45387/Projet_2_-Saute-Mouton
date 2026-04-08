from fltk import * 

class Interface:
    def __init__(self):
        self.HAUTEUR = 400 
        self.LONGUEUR = 400 
    
    def page_garde(self):
        efface_tout 
        
        x, y  = self.LONGUEUR, self.HAUTEUR

        texte(x -220,40,'Saute Mouton', taille = 30)
        
        rectangle(200,200,400,150, couleur = 'black', remplissage = 'white')
        texte(220,160,'commencer')

        rectangle(200,300,400,250, couleur = 'black', remplissage = 'white')
        texte(210,260,'Règle du jeu')
        attend_ev()

    def run(self):
        x, y  = self.LONGUEUR * 1.5, self.HAUTEUR  
        cree_fenetre(x,y)
        self.page_garde()


interface = Interface() 
interface.run()