from render_connect4 import *
from party import *



def affiche(l):
    """
    C'est une fonction qui permet d'affiche une grille.
    Paramètre(l): est la grille passer en parametre sous forme de liste.
    CU: Aucune.
    Exemple:
    >>> affiche([[2,0,0,0],[1,0,0,2],[1,0,2,1]])
    
    X---
    0--X
    0-X0
    ====
    0123
    """
    s =""
    car1 = ""
    t=""
    for e in l:
        nbre = len(e) 
        for k in e: 
            if k ==1:
                s=s+'0'
            elif k==2:
                s=s+'X'
            else:
                s =s+'-'
        print(s)
        s=""        
    for i in range(nbre):
        car1 = car1 + "="
        t = t + str(i) 
       
    print(car1)
    print(t)
    
                
def joue_un_coup(g,p):
    """
    Cette fonction permet de jouer un coup et de modifier la grille selon la case jouer par le joueur.
    Paramètre(g,p): g est la grille et p est le joueur.
    CU: Aucune.
    """
    case = saisie()
    modification = False
    if coup_valide(case,g)==True:
        ligne = ligne_tombe(g,case)
        g[ligne][case] = p
        modification= True
    if modification:
        return g
    elif modification == False:
        return -1
        
    
wait_quit()
