from fltk import * 

class Interface:
    def __init__(self) -> None:
        self.HAUTEUR = 400 
        self.LONGUEUR = 400 
    
    def page_garde(self):
        efface_tout 
        x, y  = self.LONGUEUR, self.HAUTEUR
        rectangle(x,y,x - 400,y - 400)
        ferme_fenetre()

    def run(self):
        x, y  = self.LONGUEUR, self.HAUTEUR  
        cree_fenetre(x,y)
        self.page_garde()

Interface.run()