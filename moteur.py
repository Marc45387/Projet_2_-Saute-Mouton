class Mouton:
    def __init__(self, x, y):
        #état jeu 
        self.zone = 'bas'
        self.mode_jeu = None
        self.mode_jeu_dim = None
        self.changement_zone = False
        #position
        self.x = x
        self.y = y
        #vecteur mouvement
        self.vx = 0
        self.vy = 0
        #conditions
        self.en_mouvement = False
        self.victoire = False
        #constantes
        self.HAUTEUR = 20
        self.LARGEUR = 20
        self.VMAX_X = 15.0
        self.VMAX_Y = 20.0
        self.GRAVITE = 0.9
        self.IMPACT = 0.5
        self.FROTTEMENT = 0.9

    
    def check_collision_map(self):
        """Fonction qui check les collisions entre le mouton le contour de la map (sol et murs) , et le repositionne """
        if self.y + self.HAUTEUR > 600 and self.vy >0:  #sol
            self.y= 600 - self.HAUTEUR
            self.vx = 0
            self.vy = 0
            self.en_mouvement = False
        
        if self.y < 0 :     #plafond
            if self.mode_jeu_dim == 'dimension': # pour le niveau infini 
                self.zone = 'haut'
                self.changement_zone = True
                self.y = 600
            else: # sinon mode normal 
                self.y = 0 
                self.vy = self.vy * self.IMPACT
        if self.x < 0:  #mur de gauche
            self.x = 0
            self.vx = -self.vx * self.IMPACT 
        
        if self.x + self.LARGEUR > 600:   #mur de droite
            self.x = 600 - self.LARGEUR
            self.vx = -self.vx * self.IMPACT
    
    def check_collision_bloc(self, obstacles: list):
        """Fonction qui check les collisions entre le mouton les les bloc , et le repositionne """
        for bloc in obstacles:
            if (self.x < bloc["bx"] and 
                self.x + self.LARGEUR > bloc["ax"] and 
                self.y < bloc["by"] and 
                self.y + self.HAUTEUR > bloc["ay"]):
                
                #cas 1 : on tombe dessus(vy > 0)
                if self.vy > 0 and (self.y + self.HAUTEUR - self.vy) <= bloc["ay"]:
                    self.y = bloc["ay"] - self.HAUTEUR
                    self.vy = 0 
                    # cas du glissement (galce)
                    if bloc.get("type") == "glace":
                        self.vx *= 0.98 
                        if abs(self.vx) < 0.2:
                            self.vx = 0
                            self.en_mouvement = False
                        else:
                            self.en_mouvement = True
                    else:
                        # bloc normal : on s'arrête net
                        self.vx = 0 
                        self.en_mouvement = False
                #cas 2 : on se cogne dessous(vy < 0)
                elif self.vy < 0:
                    self.y = bloc["by"]
                    self.vy = 0 
                    self.vx = self.vx * 0.8 #reduction de vitesse a l'impact pour la chute
                    
                    if self.vx > 0: self.x += 1 
                    elif self.vx < 0: self.x -= 1
                #cas 3 : on se cogne sur un cote
                else: 
                    self.vx = -self.vx * self.IMPACT
                    # On détermine de quel côté on est par rapport au centre du bloc
                    centre_bloc_x = (bloc["ax"] + bloc["bx"]) / 2
                    if self.x + (self.LARGEUR / 2) < centre_bloc_x:
                        # On est à gauche, on se place à gauche du bloc
                        self.x = bloc["ax"] - self.LARGEUR - 0.1
                    else:
                        # On est à droite, on se place à droite du bloc
                        self.x = bloc["bx"] + 0.1

    def check_arrivee(self, arrivee: dict):
        #par dessus
         if (arrivee["ax"] <= self.x <= arrivee["bx"]  and 
             arrivee["ay"] <= self.y <= arrivee["by"]):
             #print("VICTOIRE")
             self.victoire = True
        
    def check_collisions(self, obstacles: list, arrivee: dict):
        """check toutes les collisions possibles"""
        self.check_collision_map()
        self.check_collision_bloc(obstacles)
        self.check_arrivee(arrivee)

    def check_portail(self, liste_portail):
        for p in liste_portail:
            centre_x = self.x + (self.LARGEUR / 2)
            centre_y = self.y + (self.HAUTEUR / 2)

            dist = ((centre_x - p['ex'])**2 + (centre_y - p['ey']) ** 2) ** 0.5

            if dist < 20:
                self.x = p['sx']
                self.y = p['sy']
                self.vx *= 0.5 # On réduit un peu la vitesse pour éviter d'être désorienté
                self.vy *= 0.5
                break

    def impulsion(self, souris_x: int, souris_y: int):
        """ Calcule le saut en suivant exactement la direction de la souris """
        centre_x = self.x + (self.LARGEUR/2)
        centre_y = self.y + (self.HAUTEUR/2)
        
        diff_x = souris_x - centre_x
        diff_y = souris_y - centre_y
        distance = (diff_x**2 + diff_y**2)**0.5

        if distance > 0:
            # On calcule la direction pure (vecteur de longueur 1)
            dir_x = diff_x / distance
            dir_y = diff_y / distance

            # On définit une puissance proportionnelle à la distance, 
            # mais on bride la PUISSANCE totale, pas les axes séparément.

            puissance = min(distance * 0.1, 25.0) # 25.0 est ta nouvelle force max totale

            self.vx = dir_x * puissance
            self.vy = dir_y * puissance
            self.en_mouvement = True
    
    def deplacer(self, obstacles: list, arrivee: dict):
        """Fonction qui simule le saut du mouton"""
        if not self.en_mouvement and abs(self.vy) < self.GRAVITE and abs(self.vx) < 0.1:
            return 
        
        self.vy = self.vy + self.GRAVITE
        #maj de la position
        self.x += self.vx
        self.y += self.vy

        #check des collisions
        self.check_collisions(obstacles, arrivee)

        if not self.en_mouvement:
            self.x = round(self.x)
            self.y = round(self.y)
            self.vx = 0
            self.vy = 0

