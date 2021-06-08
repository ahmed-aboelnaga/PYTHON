from render_connect4 import *
from affichage import *
from random import randint

def initialise(n,m):
    """
    C'est une fonction qui permet d'inititialise une grille de n-ligne et m-colonne a 0.
    Paramètre(n,m): n nombre de ligne et m nombre de colonne.
    CU: Aucune.
    Exemple:
    >>>initialise(3,4)
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    """
    l= list()
    for i in range(n):
        c = list()
        for j in range(m):
            c.append(0)
        l.append(c)
    return list(l)       

def nr(g):
    """
    C'est une fonction qui permet de retrouver le nombre de ligne de la grille.
    Paramètre(g): est la grille du jeu.
    CU: Aucune.
    Exemple:
    >>>nr([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    3
    """
    return len(g)
def nc(g):
    """
    C'est une fonction qui permet de retrouver le nombre de colonne de la grille.
    Paramètre(g): est la grille du jeu.
    CU: Aucune.
    Exemple:
    >>>nc([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    4
    """
    return len(g[0])

def saisie():
    case = (input("entrer une colonne à jouer: "))
    try:
        case=int(case)
    except ValueError:
        print('il faut un nombre')
        return saisie()
    while case<0 or case>6:
        print('il faut un nombre compris en 0 à 6')
        return saisie()
    
    return case

def coup_valide(c,g):
    """
    C'est une fonction qui permet de verifié si un coup est valide car de l'enoncé une case est valide si elle est different de 0 et de 1.
    Paramètre(c,g): est le numero de la case que le joueur a jouer et g la grille du jeu.
    CU: Aucune
    """
    i = len(g)-1
    valide = False
    while i>=0 and not valide:
        if g[i][c]==0:
            valide = True
        i=i-1    
    return valide
def ligne_tombe(g,c):
    """
    C'est une fonction qui calcule la ligne d'une grille l'effet de bord est de renvoyer l'indice de la ligne sur la grille
    parametre(g): c'est la grille.
    parametre(c): est la case jouer.
    CU: Aucune.
    
    """
    for i in range((len(g)-1),-1,-1):
        if g[i][c]==0:
            return i
    return -1    

def enregistrer(g):
    gre=list()
    for i in range(len(g)):
        gre.append(list(g[i]))
    return gre    
def case_jouer(g,k):
    """
    C'est une fonction qui prend en paramètre deux grille et qui renvoi la case jouer par le joueur.
    paramètre(g,k): les deux grille.
    CU: Aucune.
    """
    for i in range((len(g)-1),-1,-1):
        for j in range((len(g[i])-1),-1,-1):
            if g[i][j]!=k[i][j]:
                return j





def grille_remplie(g):
    """
    Cest une fonction qui verifie si une grille est remplie renvoie True si elle est remplie et False si non.
    paramètre(g): est la grille du jeu.
    CU: Aucune.
    Exemple:
    >>>grille_remplie([[2, 0, 0, 0], [1, 0, 0, 2], [1, 2, 2, 1]])
    False
    >>>grille_remplie([[2, 1, 2, 2], [1, 1, 1, 2], [1, 2, 2, 1]])
    True
    """
    for e in g:
        for k in e:
            if k==0:
                return False
    return True

def construire_ligne(g,r):
    """
    Cette fonction prend en paramètre une grille et l'indice d'une ligne et elle renvoie la list des cases qui constitue cette ligne.
    paramètre(g,r): g est la grille et r l'indice de ligne
    CU: Aucune.
    Exemple:
    >>> construire_ligne([[0, 0, 0, 2], [1, 0, 1, 2], [0, 0, 0, 0]],1)
    [1, 0, 1, 2]
    """
    nbre_ligne = nc(g)
    list_ligne = list()
    for i in range(nbre_ligne):
        list_ligne.append(g[r][i])
    return list_ligne
def construire_colonne(g,c):
    """
    Cette fonction prend en paramètre une grille et l'indice d'une colonne et elle renvoie la list des cases qui constitue cett colonne.
    paramètre(g,r): g est la grille et c l'indice de la colonne.
    CU: Aucune.
    Exemple:
    >>> construire_colonne([[2, 0, 0, 2], [1, 0, 1, 2], [0, 0, 0, 0]],0)
    [0, 1, 2]
    """    
    nbre_colonne = nr(g)
    list_colonne = list()
    for i in range(nbre_colonne-1,-1,-1):
        list_colonne.append(g[i][c])
    return list_colonne

def construire_diag1(g, r, c):
    """
    C'est une fonction qui prend en paramètre une grille, une ligne et une colonne et renvoi la liste des diagonale selon l'indice du diagonale et du ligne.
    paramètre(g,r,c): g est la grille r la ligne et c la colonne.
    CU: aucune.
    Exemple:
    >>> construire_diag1([[2, 2, 2, 0, 2, 0, 0], [2, 2, 1, 0, 2, 1, 0], [1, 1, 2, 0, 1, 1, 1], [2, 2, 2, 0, 2, 2, 2], [2, 2, 1, 1, 1, 1, 1], [1, 1, 1, 2, 1, 1, 1]], 2, 4)
    [2, 0, 1, 2, 1]
    """
    return [g[r+i][c+i] for i in range(-3,4) if (((r+i) in range(nr(g))) and ((c+i) in range(nc(g))))]

def construire_diag2(g, r, c):
    """
    C'est une fonction qui prend en paramètre une grille, une ligne et une colonne et renvoi la liste des diagonale selon l'indice du diagonale et du ligne.
    paramètre(g,r,c): g est la grille r la ligne et c la colonne.
    CU: aucune.
    Exemple:
    >>> construire_diag2([[2, 2, 2, 0, 2, 0, 0], [2, 2, 1, 0, 2, 1, 0], [1, 1, 2, 0, 1, 1, 1], [2, 2, 2, 0, 2, 2, 2], [2, 2, 1, 1, 1, 1, 1], [1, 1, 1, 2, 1, 1, 1]], 2, 4)
    [1, 1, 2, 1, 0]
    """    
   
    return [g[r-i][c+i] for i in range(-3,4) if (((r-i) in range(nr(g))) and ((c+i) in range(nc(g))))]


    
    
def is_aligne(lc,p):
    """
    C'est une fonction qui prend en paramètre une liste et un joueur qui renvoi True si le jouer aligne 4 case et False si non.
    Paramètre(lc,p): est une list et p un joueur.
    CU: aucune.
    Exemple:
    >>> is_aligne([1, 1, 2, 1, 0],1)
    False
    >>> is_aligne([1, 1, 1, 1, 0],1)
    True
    """
    cpt=0
    i=0
    gagne = False
    while i<len(lc) and not gagne:
        if lc[i]==p:
            cpt= cpt+1
            if cpt==4:
                gagne = True   
        else:
            cpt = 0
        i=i+1    
    return gagne
 
    
def is_win(g,r,c,p):
    """
    Cette fonction is_win prend en paramètre une grille et une ligne , une colonne et un joueur renvoie True si le joueur est gagnant et False si non.
    Paramètre(g,p): g est une grille et p un joueur.
    Paramètre(r,c): r est l'indice d'une ligne et c l'indice d'une colonne.
    CU: Aucune.
    Exemple:
    >>> is_win([[0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0], [2, 2, 2, 0, 0, 0, 0], [2, 2, 1, 1, 0, 0, 0], [1, 1, 1, 2, 0, 0, 0]],1,0,2)
    False
    >>> is_win([[0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0], [2, 2, 2, 0, 0, 0, 0], [2, 2, 1, 1, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0]],5,1,1)
    True
    
    """
    list_ligne=[]
    list_colonne=[]
    list_ligne = construire_ligne(g,r)
    list_colonne = construire_colonne(g,c)
    list_diag1= construire_diag1(g, r, c)
    list_diag2= construire_diag2(g, r, c)
    if is_aligne(list_ligne,p):
        return True
    elif is_aligne(list_colonne,p):
        return True
    elif is_aligne(list_diag1,p):
        return True
    elif is_aligne(list_diag2,p):
        return True
    else:
        return False
def play(g):
    """
    C'est une fonction nommer play qui permet de faire jouer deux personne tout en respectant les condition du jeu.
    Paramètre(g): est la grille du jeu.
    CU: Aucune.
    """
    joueur = 1
    fini= False
    while not fini and not grille_remplie(g):
        draw_connect4(g)
        gr = enregistrer(g)
        print("joueur ", joueur)
        grille = joue_un_coup(g,joueur)
        while grille== -1 and grille_remplie(g)==False:
            print("colonne deja prise choisir une autre colonne")
            grille = joue_un_coup(g,joueur)    
        
        affiche(grille)
        draw_connect4(g)
        c = case_jouer(gr,grille)
        r = ligne_tombe(gr,c)
        g = grille
        if is_win(g,r,c,joueur):
            fini = True
        gr = enregistrer(g)
        if grille_remplie(g)==False and not fini:
            if joueur ==1:
                joueur =2
            else:
                joueur = 1
    if joueur==1:
       print("Bravo le joueur ROUGE à gagner")
    else:
       print("Bravo le joueur JAUNE à gagner")



def is_aleat(g):
    """
    c'est une fonction qui a pour objectif de renvoyer une case aleatoire valide et renvoie -1 si la grille est remplie.
    Paramètre(g) est une grille.
    CU: Aucune.
    Exemple:
    >>> is_aleat([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    1
    """
    debut = 0
    fin = nc(g)-1
    trouve = False
    while not trouve:
        aleatoire = randint(debut,fin)
        if coup_valide(aleatoire,g):
            trouve = True
        debut= debut + 1
        if debut==fin:
            return -1
    return aleatoire
def unmove(g,ia):
    """
    Cette fonction du nom de unmove permet une case jouer dans la grille en mettant la case à 0 l'effet de bord de la fonction est que il vas modifier la grille.
    Paramètre(g,ia): g est une grille et ia une colonne jouer.
    CU: Aucune.
    """
    ligne = ligne_tombe(g,ia)
    if ligne==-1:
        ligne=0
    else:
         ligne= ligne + 1
    g[ligne][ia]=0
def ia_win(g,p):
    """
    Cette première fonction ia_win a pour but d'essayer toutes les colonne de la grille et de verifier si une colonne conduit à la victoire si non il renvoie une case aleatoire.
    Paramètre(g,p): g est une grille et p un joueur qui est l'ordinateur.
    CU: Aucune.
    Exemple:
    >>> ia_win([[0, 0, 0, 0], [0, 0, 0, 0], [2, 2, 0, 2]],2)
    2
    """
    
    gagne=False
    ia = 0
    ligne = ligne_tombe(g,ia)
    while ia<len(g[0]) and not gagne:
        ligne = ligne_tombe(g,ia)
        if ligne==-1:
            ia=ia+1
        else:
            g[ligne][ia]=p
            if is_win(g,ligne,ia,p):
                unmove(g,ia)
                gagne=True
            else:
                unmove(g,ia)
                ia = ia + 1
            
    if gagne==True:
        return ia
    else:
        ia = is_aleat(g)
        return ia
            
            
        
    
def coup_ordinateur(g,ordi):
    """
    Cette fonction coup_ordinateur permet de modifier la grille selon la case renvoyer par ia_win.
    Parametre(g,ordi): g est la grille et ordi est le joueuer qui est l'ordinateur.
    CU: Aucune.
    Exemple:
    coup_ordinateur([[0, 0, 0, 0], [0, 0, 0, 0], [2, 2, 0, 2]],2)
    [[0, 0, 0, 0], [0, 0, 0, 0], [2, 2, 2, 2]]
    """
    ia = ia_win(g,ordi)
    if ia==-1:
        return -1
    else:
        ligne = ligne_tombe(g,ia)
        g[ligne][ia]=ordi
        return g
def calcul_score(lc):
    """
    Cette fonction permet de calculer le score d'une liste passer en paramètre toutes en respectant le sujet et les règles de priorite apres l'etude elle le score de la list.
    Paramètre(lc): c'est la list passer en paramètre.
    CU: Aucune.
    Exemple:
    >>> calcul_score([1,1,1,0,2,2])
    -500
    >>> calcul_score([2,2,0,1,2,2,2])
    100
        
    """
    cpt_adversaire=0
    cpt_joueur=0
    score_joueur=0
    score_adversaire=0
    score=0
    i=0
    j=0
    tmp=0
    list1=[]
    list2=[]
    dic1=dict()
    dic2=dict()
    cpt=0
    trouve=False
    #gagne=False
    #perd=False
    if 1 in lc or 2 in lc:
        while i<len(lc):
            if lc[i]==2:
                
                cpt_joueur=cpt_joueur+1
                tmp=tmp+1
                if cpt_joueur==1:
                    score_joueur=1
                   
                elif cpt_joueur==2:
                    score_joueur=100
                    
                else:
                    score_joueur=1000
                    #gagne=True
                    
                    
            else:
                cpt_joueur=0
                list1.append(score_joueur)
                dic1[tmp]=score_joueur
                score_joueur=0
                tmp=tmp+1
                
            i=i+1    
        list1.sort(reverse=True)
        while cpt<len(list1) and not trouve:
            for key in dic1:
                if dic1[key]==list1[cpt]:
                    if lc[key]==0 and lc[key-1]==2:
                        score_joueur=list1[cpt]
                        trouve=True
                    else:    
                        score_joueur=0
            cpt=cpt+1
        tmp=0
        trouve =False
        cpt=0
        while j<len(lc): 
            if lc[j]==1:
                cpt_adversaire=cpt_adversaire+1
                tmp=tmp+1
                if cpt_adversaire==1:
                    score_adversaire=-1
                    
                    
                elif cpt_adversaire==2:
                    score_adversaire=-10
                    
          
                else:
                    score_adversaire=-500
            else:
                cpt_adversaire=0
                list2.append(score_adversaire)
                dic2[tmp]=score_adversaire
                score_adversaire=0
                tmp=tmp+1
            j=j+1
        list2.sort()
        while cpt<len(list2) and not trouve:
            for key1 in dic2:
                if dic2[key1]==list2[cpt]:
                    if lc[key1]==0 and lc[key1-1]==1:
                        score_adversaire=list2[cpt]
                        trouve=True
                    else:
                        score_adversaire=0     
            cpt=cpt+1
        if score_adversaire==-500:
            score=-500
        elif score_joueur==1000:
            score=1000
        elif score_joueur==100:
            score=100
        elif score_joueur==10:
            score=10
        
        elif score_joueur==1:
            score=score_joueur
        elif score_joueur==0:
            score=score_joueur    
        elif score_adversaire==-10:
            score=score_adversaire
        else:    
            score=score_adversaire 
    return score
            
            
                
def score(g,r,c):
    """
    Cette fonction score prend en Paramètre est une grille, une ligne et une colonne et renvoie la somme des sommes quadruplet.
    Paramètre(g,c,r): g est une grille r est une ligne et c est une colonne.
    CU: Aucune
    Exemple:
    >>> score([[0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0], [2, 2, 2, 0, 0, 0, 0], [2, 2, 1, 1, 0, 0, 0], [1, 1, 1, 2, 0, 0, 0]],5,2)
    1
    """
    list_ligne = construire_ligne(g,r)
    list_colonne = construire_colonne(g,c)
    list_diag1= construire_diag1(g, r, c)
    list_diag2= construire_diag2(g, r, c)
    score_ligne = calcul_score(list_ligne)
    score_colonne = calcul_score(list_colonne)
    score_diag1= calcul_score(list_diag1)
    score_diag2= calcul_score(list_diag2)
    if score_diag2==-500 or score_diag1==-500 or score_colonne==-500 or score_ligne==-500:
        return -500
    elif score_diag2==1000 or score_diag1==1000 or score_colonne==1000 or score_ligne==1000:
        return 1000
    elif score_diag2==100 or score_diag1==100 or score_colonne==100 or score_ligne==100:
        return 100
    elif score_diag2==10 or score_diag1==10 or score_colonne==10 or score_ligne==10:
        return 10
    elif score_diag2==1 or score_diag1==1 or score_colonne==1 or score_ligne==1:
        return 1
    elif score_diag2==0 or score_diag1==0 or score_colonne==0 or score_ligne==0:
        return 0
    else:
        return min(score_diag2,score_diag1,score_colonne,score_ligne)
        
 
def ia_win2(g,p):
    """
    Cette deuxieme fonction ia_win2 qui prend en Paramètre une grille et un joueur et renvoie une case a jouer pour l'ordinateur tout en calculant le bon score en privilegeant la fonction is_win.
    Parametre(g,p): g est une grille et p l'ordinateur.
    CU: Aucune.
    Exemple:
    >>> ia_win2([[0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0], [2, 2, 2, 0, 0, 0, 0], [2, 2, 1, 1, 0, 0, 0], [1, 1, 1, 2, 0, 0, 0]],2)
    3
    """
    gagne=False
    trouve = False
    j=0
    i=0
    ia = 0
    dic=dict()
    li=[]
    tmp=0
    ligne = ligne_tombe(g,ia)
    while ia<len(g[0]) and not gagne:
        ligne = ligne_tombe(g,ia)
        if ligne==-1:
            ia=ia+1
        else:
            g[ligne][ia]=p
            if is_win(g,ligne,ia,p):
                unmove(g,ia)
                gagne=True
            
            else:
                unmove(g,ia)
                dic[ia]=score(g,ligne,ia)
                li.append(score(g,ligne,ia))
                ia = ia + 1
                print(li)
                print("\n")
                print(dic)
    lis_tmp=[]            
    li.sort(reverse=True)
    if gagne==True:
        return ia
    else:
        for cle in dic:
            lis_tmp.append(cle)
        lis_tmp.sort()    
        while i<len(li) and not trouve:
            if -500 in li:
                while j<len(lis_tmp) and not trouve:
                    if dic[lis_tmp[j]]==-500:
                        tmp=lis_tmp[j]
                        trouve=True
                    j=j+1    
            else:
                while j<len(lis_tmp) and not trouve:
                    if dic[lis_tmp[j]]==li[0]:
                        tmp=lis_tmp[j]
                        trouve=True
                    j=j+1 
            i=i+1            
        return tmp

    
def coup_ordinateur2(g,ordi):
    """
    Cette deuxieme fonction coup_ordinateur2 utiliser la case renvoyer par la fonction ia_win2 et modifie la grille selon la case jouer.
    Paramètre(g,ordi): g est une grille et ordi est le joueur qui reprensente l'ordinateur.
    CU: Aucune.
    Exemple:
    >>> coup_ordinateur2([[0, 0, 0, 0], [0, 0, 0, 0], [1, 2, 0, 0]],2)
    [[0, 0, 0, 0], [0, 2, 0, 0], [1, 2, 0, 0]]
    
    """
    ia = ia_win2(g,ordi)
    if ia==-1:
        return -1
    else:
        ligne = ligne_tombe(g,ia)
        g[ligne][ia]=ordi
        return g
def move_ia(g,nb_round,player):
    end  = False
    list_move =[0]
    player_round = player
    backtrack = False
    next_move= False
    while not end:
        if len(list_move)==0:
            end = True
        elif next_move:
            next_move=False
            list_move[-1]+=1
        elif backtrack:
            backtrack=False
            list_move.pop()
            next_move=True
            player_round = player%2
        elif list_move[-1]==nc(g):
            backtrack = True
        elif coup_valide(list_move[-1],g):
            list_move[-1]+=1
        else:
            column = list_move[-1]
            r = ligne_tombe(g,column)
            
            g[r][column]=player
            draw_connect4(g)
            input()
            
            if is_win(g,r,column,player):
                next_move=True
            elif len(list_move)==nb_round:
                next_move = True
            else:
                list_move.append(0)
                player= player%2
    return list_move                   
    
def play_ordi_facile(g):
    """
    Cette fonction play_ordi permet de faire le jeu entre un joueur et l'ordinateur et de renvoie le joueur gagnant si non si la grile est remplie il renvoie grille remplie.
    Paramètre(g): c'est la grille du jeu.
    CU: Aucune.
    
    """
    joueur = 1
    fini= False
    while not fini and not grille_remplie(g):
        draw_connect4(g)
        gr = enregistrer(g)
        if joueur ==1:
            print("joueur ", joueur)
            grille = joue_un_coup(g,joueur)
            while grille== -1 and grille_remplie(g)==False:
                print("colonne deja prise choisir une autre colonne")
                grille = joue_un_coup(g,joueur)    
        
            affiche(grille)
            draw_connect4(g)
            c = case_jouer(gr,grille)
            r = ligne_tombe(gr,c)
            g = grille
            if is_win(g,r,c,joueur):
                fini = True
            
            if grille_remplie(g)==False and not fini:
                if joueur ==1:
                    joueur =2
                else:
                    joueur = 1
        if joueur==2:
            gr = enregistrer(g)
            grille = coup_ordinateur(g,joueur)
            while grille== -1 and grille_remplie(g)==False:
                grille = coup_ordinateur(g,joueur)
            affiche(grille)
            draw_connect4(g)
            c = case_jouer(gr,grille)
            r = ligne_tombe(gr,c)
            g = grille
            if is_win(g,r,c,joueur):
                fini = True
            if grille_remplie(g)==False and not fini:
                joueur = 1
    if fini==True:            
        if joueur==1:
           print("Bravo le joueur ROUGE à gagner")
        else:
           print("Bravo le joueur JAUNE à gagner")
    else:
        print("grille remplie et aucun joueur n'a gagner")
        
    
    
def play_ordi_normale(g):
    """
    Cette fonction play_ordi permet de faire le jeu entre un joueur et l'ordinateur et de renvoie le joueur gagnant si non si la grile est remplie il renvoie grille remplie.
    Paramètre(g): c'est la grille du jeu.
    CU: Aucune.
    
    """
    joueur = 1
    fini= False
    while not fini and not grille_remplie(g):
        draw_connect4(g)
        gr = enregistrer(g)
        if joueur ==1:
            print("joueur ", joueur)
            grille = joue_un_coup(g,joueur)
            while grille== -1 and grille_remplie(g)==False:
                print("colonne deja prise choisir une autre colonne")
                grille = joue_un_coup(g,joueur)    
        
            affiche(grille)
            draw_connect4(g)
            c = case_jouer(gr,grille)
            r = ligne_tombe(gr,c)
            g = grille
            if is_win(g,r,c,joueur):
                fini = True
            
            if grille_remplie(g)==False and not fini:
                if joueur ==1:
                    joueur =2
                else:
                    joueur = 1
        if joueur==2:
            gr = enregistrer(g)
            grille = coup_ordinateur2(g,joueur)
            while grille== -1 and grille_remplie(g)==False:
                grille = coup_ordinateur2(g,joueur)
            affiche(grille)
            draw_connect4(g)
            c = case_jouer(gr,grille)
            r = ligne_tombe(gr,c)
            g = grille
            if is_win(g,r,c,joueur):
                fini = True
            if grille_remplie(g)==False and not fini:
                joueur = 1
    if fini==True:            
        if joueur==1:
           print("Bravo le joueur ROUGE à gagner")
        else:
           print("Bravo le joueur JAUNE à gagner")
    else:
        print("grille remplie et aucun joueur n'a gagner")
        
    
        
    
    
    

        



wait_quit()

