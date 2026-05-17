from moteur import *
from math import *
from fltk import *

def simule_saut(coord_x: int, coord_y: int, souris_x: int, souris_y: int, obstacles: list, arrivee: dict):
    """
    Simule un saut et renvoie la position finale (x, y) du mouton après s'être arrêté 
    ou avoir atteint l'arrivée.
    """
    fantome = Mouton(coord_x, coord_y)
    fantome.LARGEUR = 20 
    fantome.HAUTEUR = 20

    fantome.impulsion(souris_x, souris_y)
    
    #simulation sur 800 frames
    limit = 0
    while limit < 800:
        fantome.deplacer(obstacles, arrivee)
        limit += 1

        if not fantome.en_mouvement:
            break

        if fantome.victoire:
            break
    
    fantome.x = round(fantome.x)
    fantome.y = round(fantome.y)
    return (fantome.x, fantome.y)

def ia_multi_options(coord_x: int, coord_y: int, obstacles: list, arrivee: dict, nb_options=16):
    """
    Simule plein de sauts différents (angles/puissances) et renvoie la liste 
    des 'nb_options' meilleurs coups trouvés.
    """
    toutes_les_options = []
    cx = (arrivee['ax'] + arrivee['bx']) // 2
    cy = (arrivee['ay'] + arrivee['by']) // 2

    #balayage de differents angles et puissances
    for angle_deg in range(0, 181, 1): 
        angle_rad = radians(angle_deg)
        for force in range(50, 251, 10): 
            test_x = coord_x + int(force * cos(angle_rad))
            test_y = coord_y - int(force * sin(angle_rad))

            x,y = simule_saut(coord_x, coord_y, test_x, test_y, obstacles, arrivee)
            

            dist_arrivee = sqrt((cx - x)**2 + (cy - y)**2)
            dist_parcourue = sqrt((x - coord_x)**2 + (y - coord_y)**2)
            
            #accepte même les petits mouvements si on est bloqué
            if dist_parcourue < 30: 
                continue
            
            dist_laterale = abs(x - coord_x)
            progression_y = coord_y - y

            if progression_y < -20:
                score_tmp = dist_arrivee + 2000 
            
            else:
                score_tmp = dist_arrivee - (progression_y * 10) - (dist_laterale * 2)

            toutes_les_options.append((score_tmp, (x,y), (test_x, test_y)))

    toutes_les_options.sort(key=lambda x: x[0])
    # Renvoie le top des meilleurs coups
    return [(opt[1], opt[2]) for opt in toutes_les_options[:nb_options]]

def meilleur_coup(coord_x: int, coord_y: int, obstacles: list, arrivee: dict):
    """
    Calcule et renvoie le chemin optimal (suite de sauts) pour amener le mouton 
    jusqu'à la zone d'arrivée.
    """
    # Frontière : [(priorité, position, chemin)]
    frontiere = [(0, (coord_x, coord_y), [])]
    deja_visite = [] 
    toutes_simulations = []
    max_sauts = 10
    
    meilleur_essai = [] 
    min_dist_globale = float('+inf')

    while frontiere:
        frontiere.sort(key=lambda x: x[0])
        score_actuel, (curr_x, curr_y), chemin = frontiere.pop(0)

        if arrivee["ax"] <= curr_x <= arrivee["bx"] and arrivee["ay"] <= curr_y <= arrivee["by"]:
            return chemin, deja_visite, toutes_simulations

        if len(chemin) >= max_sauts:
            continue

        options = ia_multi_options(curr_x, curr_y, obstacles, arrivee)
        
        for option in options:
            nouvelle_pos, coord_souris = option
            toutes_simulations.append(nouvelle_pos)
            
            # Vérifie si on a déjà visité cette zone
            if any(sqrt((v[0]-nouvelle_pos[0])**2 + (v[1]-nouvelle_pos[1])**2) < 20 for v in deja_visite):
                continue
            
            deja_visite.append(nouvelle_pos)
            nouveau_chemin = chemin + [option]
            
            d = sqrt(((arrivee['ax']+arrivee['bx'])/2 - nouvelle_pos[0])**2 + 
                     ((arrivee['ay']+arrivee['by'])/2 - nouvelle_pos[1])**2)
            
            # Sauvegarde du meilleur essai au cas où
            if d < min_dist_globale:
                min_dist_globale = d
                meilleur_essai = nouveau_chemin

            priorite = len(nouveau_chemin) * 500 + d
            frontiere.append((priorite, nouvelle_pos, nouveau_chemin))

    return meilleur_essai, deja_visite, toutes_simulations