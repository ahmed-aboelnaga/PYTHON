from tkinter import *
from render_connect4 import *
from affichage import *
from party import *

def bonjour():
    #print("Bonjour le monde")
    g = initialise(6,7)
    play_ordi_facile(g)
    
mon_apply = Tk()
mon_apply.title("Programme Choix utilisateur")
mon_apply.geometry("650x450")
mon_apply.minsize(480, 360)
mon_apply.config(background="#41b77f")
mon_titre = Label(mon_apply, text="Jeu puissance 4", font=("Arial",20), bg="#41b77f", fg="white")
mon_titre.pack()
mon_sousTitre = Label(mon_apply, text="\nEntrer votre niveau", font=("Arial",15), bg="#41b77f", fg="white")
mon_sousTitre.pack()

mon_objet = Frame(mon_apply, bg="#41b77f")
boutton_facile = Button(mon_objet, text="Facile", font=("Arial",20), bg="white", fg="#41b77f",command = bonjour)
boutton_facile.pack(pady=15)
boutton_normal = Button(mon_objet, text="Normal", font=("Arial",20), bg="white", fg="#41b77f")
boutton_normal.pack(pady=15)
boutton_maitre = Button(mon_objet, text="Maître", font=("Arial",20), bg="white", fg="#41b77f")
boutton_maitre.pack(pady=15)
mon_objet.pack()
mon_apply.mainloop()