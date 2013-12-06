# -*- coding: cp1252 -*-

class joueur:
    "Ensemble d'attributs que possede chaque joueur"
    compte=0
    mise_totale=0
    dict_montants={}#dictionnaire des montants des joueurs
    dict_guess={}
    dict_bet={}
    joueur_dict={}#dictionnaire des joueurs
    noms=[]
    dict_ecarts={}
    def __init__(self,nom="",montant_initial=0):
        "definition des attributs de depart du joueur"
        self.nom=nom#attribut "nom"
        self.montant_ini=self.montant=montant_initial#attributs "montant #initial" et #"montant actuel"
        self.gain=self.perte=0#attributs "gain" et "perte"
        joueur.dict_montants[self.nom]=self.montant#attribut de classe:dictionnaire des #montants des joueurs
        joueur.dict_guess[self.nom]=[]
        joueur.dict_bet[self.nom]=[]
        joueur.compte+=1#nombre de joueurs incremente de 1
        self.attributs_joueur=vars(self)
        return

        joueur.noms=[]
    def Montant(self,gain=0,perte=0):
        "'methode' ou fonction determinant le montant d'argent que possede le joueur"
        self.gain+=gain#incremente l'attribut "gain"
        self.perte+=perte#incremente l'attribut "perte"
        self.montant=self.montant-perte+gain#redefinition de l'attribut "montant" en #fonction des gains et pertes
        joueur.dict_montants[self.nom]=self.montant
        return self.montant
    def guessing(self,guess,bet):
        self.guess=guess
        self.bet=bet
        joueur.dict_guess[self.nom].append(self.guess)
        joueur.dict_bet[self.nom].append(self.bet)
        joueur.mise_totale+=self.bet
        self.Montant(perte=bet)
        return (self.guess,self.bet)
    
    def delete(self):
        "Supprime l'instance du joueur et toutes ses références dans la classe."
        for n in(self.nom):
            del joueur.joueur_dict[n]
            joueur.noms.remove(n)
            del joueur.dict_montants[n]
            del joueur.dict_guess[n]
            del joueur.dict_bet[n]
            del joueur.dict_ecarts[n]
        joueur.compte-=1
        
        return "Le joueur %s a été supprimé."%self.nom
    @staticmethod
    def generateur(nom):
        joueur.joueur_dict[nom]=joueur(nom,120)#crée une instance de la classe ‘joueur' dans le #dictionnaire
        joueur.noms=joueur.joueur_dict.keys()
        return "Vous avez créé un nouveau joueur:%s"%nom
    @staticmethod
    def class_reset():
        "Réinitialise la classe complètement(incluant le dictionnaire des joueurs)"
        joueur.compte=0
        joueur.mise_totale=0
        joueur.dict_montants={}#dictionnaire des montants des joueurs
        joueur.dict_guess={}
        joueur.dict_bet={}
        joueur.joueur_dict={}#dictionnaire des joueurs
        joueur.noms=[]
        joueur.dict_ecarts={}
        return "Classe réinitialisée."
    def attributs(self):
        "Affiche tous les attributs de l'instance de classe"
        "Voici les attributs du joueur %s."%self.nom
        for n in self.attributs_joueur:
            print n,":",self.attributs_joueur[n]
        return
    @staticmethod
    def class_attributs():
        for n in joueur.__dict__:
            print n,":",joueur.__dict__[n]

    @staticmethod
    def gagnant():
        """Crée un dictionnaire des écarts entre le 'guess' de chacun des joueurs et
la valeur retournée par valeur_des(nbd),
et renvoie le nom du joueur don't l'écart est le plus petit. nbd=nombre de dés"""
        global valeur_totale
        for n in joueur.noms:
            joueur.dict_ecarts[n]=abs( valeur_totale-joueur.joueur_dict[n].guess)
        return [n for n in joueur.noms if joueur.dict_ecarts[n]==min(joueur.dict_ecarts.values())]

import random

dict_des={}
def valeur_des(nbd):
    """Assigne une valeur aléatoire à chaque dé et renvoi la somme de ces valeurs.'nbd'=nombre de dés"""
    global dict_des,valeur_totale
    for n in range(int(nbd)):
        dict_des["dé%d"%n]=random.randint(1,6)#chaque dé se voit assigner une valeur aléatoire #dans un dictionnaire
    valeur_totale=sum(dict_des.values())
    return



## Imports
from Tkinter import *
import time
## Functions
##def tk_menu_nbjoueur():
## global ismenu
## ismenu=True
## tk_nbjoueur()
## fenetre1.destroy
## return programme()

def tk_nbjoueur():
  global window1,ismenu,nbj
## click1=False
## if ismenu is True :
## window1=Toplevel()
## else:
  window1=Tk()
  window1.title("Combien de joueur?")
  label1=Label(window1,text="Combien de joueurs vont jouer? Entre 2 et 4.", font="Time 10 bold", fg="black")
  label1.pack()
  nbj=IntVar()
  entry1=Entry(window1, textvariable=nbj, justify=CENTER, width=2)
  entry1.pack()
  button1=Button(window1, text="Okay", command=tk_nbjoueur2, cursor="dotbox")
  button1.pack()
  window1.mainloop()
  nbj=nbj.get()

def tk_nbjoueur2():
  global nbj
  ismenu=False
  if nbj.get() in (2,3,4):
    window1.destroy()
  else:
    window2=Toplevel()
    window2.title("Attention!")
    label2=Label(window2, text="Attention, vous n'avez pas entrer un nombre de joueurs valide!", font="Times 10 bold", fg="black")
    label2.pack()
    button2=Button(window2, text="Okay", command=window2.destroy, cursor="dotbox")
    button2.pack()
    window2.grid()

def mise1(mise):
    bet.set(mise)
   

def autremise():
    global bet
    fenetre2=Toplevel()
    fenetre2.title("Autre mise?")
    fenetre2.geometry("200x50")
    saisie2=Entry(fenetre2, textvariable=bet, justify=CENTER, width=3)
    bouton8=Button(fenetre2, text="Confirmer", command=fenetre2.destroy, cursor="dotbox")
    saisie2.pack()
    bouton8.pack(pady=1)
    fenetre2.grid()
    return

def aide():
    fenetre3=Toplevel()
    fenetre3.title("Règles?")
    fenetre3.geometry("500x500")
    barredefilement=Scrollbar(fenetre3)
    barredefilement.pack(side=RIGHT, fill=Y)
    texte1=Text(fenetre3,wrap=WORD, yscrollcommand=barredefilement.set, bg="white", fg="black")
    texte1.insert(INSERT, """Bienvenue au jeu Dés Suprêmes: le destin des intervalles. Dans ce jeu de hasard, vous aurez l'occasion de miser une somme d'argent à partir d'un montant qui vous sera alloué initialement. Votre but sera d'être le dernier joueur à rester à la fin de la partie, c'est-à-dire de ne pas être ruiné par des coups de dés défavorables trop répétés.

Plus précisément, la partie sera amorcée avec le choix de la valeur des paramètres suivants: le nombre de joueurs que vous souhaitez voir participer au jeu et le nombre de dés qui seront lancés à chaque tour. Un montant initial de 120$ sera alors attribué à chacun des participants.

À chaque tour, les joueurs devront choisir une mise en argent. Ensuite, à tour de rôle, ils doivent effectuer une prédiction quant à la somme des chiffres affichés sur les dés après lancer. Ceux-ci seront par la suite effectivement lancés. Le gagnant du tour est le joueur dont la prédiction se rapproche le plus de la somme réelle des chiffres sur les dés obtenus. Celui-ci remporte alors la mise des autres joueurs.

Votre objectif est donc de produire les meilleures prédictions pour remporter le plus de manches possibles. Si vous perdez trop de manches, votre montant sera immanquablement porté à 0$ et vous serez éliminé. Si vous parvenenz à survivre jusqu'à la fin, vous gagnerez la partie et la totalité de l'argent de chacun des joueurs.

N. B. : En aucun vous ne pourrez parier plus que le montant possédé au moment de la mise. Les emprunts sont donc interdits.

Sur ce, sans plus tarder, bon jeu à tous!
""")
    texte1.config(state=DISABLED)
    texte1.pack(fill=Y, expand=1)
    barredefilement.config(command=texte1.yview)
    fenetre3.grid()
    return

def tk_dice(de_final, numde):
    global section1, comp, windowDice, last_numero, definal
    comp,last_numero =0,0
    definal=de_final
    num_de=numde+1
    windowDice=Tk()
    windowDice.geometry("130x112")
    windowDice.title("Dé #%d"%num_de)
    section1=Canvas(windowDice, width=130, height=112,background="white", cursor="pirate")
    section1.pack()
    windowDice.after(100,roll)
    windowDice.mainloop()
def roll():
    global comp, image_de, img_de, imgde, image_de_final, definal, imgdefinal, imgfinale, last_numero
    import random
    if comp<20:
        numero_img=random.randint(1,6)
        while numero_img==last_numero:
            numero_img=random.randint(1,6)
        last_numero=numero_img
        image_de="d6-face%d-%d.gif"%(numero_img,type_de)
        img_de=PhotoImage(file=image_de)#ref
        imgde=section1.create_image(65,56, image=img_de)
        comp=comp+1
        windowDice.after(100,roll)
    elif comp==20:
## definal=3
        image_de_final="d6-face%d-%d.gif"%(definal,type_de)
        imgdefinal=PhotoImage(file=image_de_final)#ref
        imgfinale=section1.create_image(65,56,image=imgdefinal)
        windowDice.after(5000, windowDice.destroy)

def tk_main_window(nom):
    
    ## Variables
    global bet,guess,fenetre1,name
    name=nom
    bet=None
    
    #Interface design
    
    
    fenetre1=Tk()
    fenetre1.title(nom)
    fenetre1.geometry("500x500")
    
    division=Frame(fenetre1)
    division.pack(side=LEFT, fill=BOTH, expand=1)
    
    section2=Frame(division)
    section2.pack(fill=X)
    libele1=Label(section2, text="Choisissez une mise", fg="black", font="Times 10 bold")
    libele1.pack()
    bet=IntVar()#variable contenant le bet
    bouton1=Button(section2, text="1", width=9, command=lambda:mise(1), cursor="dotbox")
    bouton1.pack(pady=1)
    bouton2=Button(section2, text="5", width=9, command=lambda:mise(5), cursor="dotbox")
    bouton2.pack(pady=1)
    bouton3=Button(section2, text="10", width=9, command=lambda:mise(10), cursor="dotbox")
    bouton3.pack(pady=1)
    bouton4=Button(section2, text="20", width=9, command=lambda:mise(20), cursor="dotbox")
    bouton4.pack(pady=1)
    bouton5=Button(section2, text="50", width=9, command=lambda:mise(50), cursor="dotbox")
    bouton5.pack(pady=1)
    bouton6=Button(section2, text="Autre mise", width=9, command=autremise, cursor="dotbox")
    bouton6.pack(pady=1)
    libele3=Label(section2, textvariable=bet, bg="black", fg="white")
    libele3.pack(fill=X)
    
    section3=Frame(division)
    section3.pack(side=BOTTOM, pady=1, fill=X)
    libele2=Label(section3, text="Quel nombre prédisez-vous?", fg="black", font="Times 10 bold")
    libele2.pack()
    guess=IntVar()#variable contenant le guess
    saisie1=Entry(section3, textvariable=guess, justify=CENTER, width=3)
    saisie1.pack()
    libele4=Label(section3, textvariable=guess, bg="black", fg="white")
    libele4.pack(fill=X)
    bouton7=Button(section3, text="Continuer", width=9, command=continuer, cursor="dotbox")
    bouton7.pack(pady=1)
    
    section4=Frame(fenetre1, width=200, height=500, background="white", cursor="pirate")
    section4.pack(side=RIGHT)
    
    
    dict_label_montant={}
    dict_label_nom={}
    photo=PhotoImage(file="jeton.gif")#créer un fichier jeton
    for a in joueur.noms:
            dict_label_nom[a]=Label(section4, text=a, fg="black", font="Times 10 bold", background="white")
            dict_label_nom[a].pack()
            jeton=Label(section4, image=photo, background="white")
            jeton.pack()
            dict_label_montant[a]=Label(section4, text=joueur.joueur_dict[a].montant, compound=CENTER, background="white", fg="green", font="Time 10 bold")
            dict_label_montant[a].pack()
    
    
    menus=Menu(fenetre1)
    
    menu1=Menu(menus, tearoff=0)
    menus.add_cascade(label="Fichier", menu=menu1)
## menu1.add_command(label="Recommencer")
    menu1.add_command(label="Quitter", command=fermeture_plus_tot)

    menu2=Menu(menus, tearoff=0)
    menus.add_cascade(label="Personnalisation", menu=menu2)
    
    sousmenu=Menu(menu2, tearoff=0)
    menu2.add_cascade(label="Type de design de dé", menu=sousmenu)
    sousmenu.add_command(label="Simplifié", command=type1)
    sousmenu.add_command(label="Réaliste", command=type2)
##  menu2.add_command(label="Nombre de joueur", command=tk_menu_nbjoueur)
##  menu2.add_command(label="Nombre de dés", command=tk_menu_nbdes)
    
    menu3=Menu(menus, tearoff=0)
    menus.add_cascade(label="Aide", menu=menu3)
    menu3.add_command(label="Règles", command=aide)
    
    
    fenetre1.config(menu=menus)
    fenetre1.mainloop()
    
    bet=bet.get()
    guess=guess.get()

def type1():
    global type_de
    type_de=1

def type2():
    global type_de
    type_de=2

def continuer():
    if bet.get()>joueur.joueur_dict[name].montant:
        attention=Tk()
        attention.title("Attention!")
        alabel=Label(attention, text="Attention, vous avez misé plus que vous ne possédez!", fg="black", font="Times 10 bold")
        alabel.pack()
        abouton=Button(attention, text="Okay", command=attention.destroy, cursor="dotbox")
        abouton.pack()
        attention.mainloop()
    elif bet.get()<=0:
        attention=Tk()
        attention.title("Attention!")
        alabel=Label(attention, text="Attention, vous avez misé 0 ou moins!", fg="black", font="Times 10 bold")
        alabel.pack()
        abouton=Button(attention, text="Okay", command=attention.destroy, cursor="dotbox")
        abouton.pack()
        attention.mainloop()
    elif guess.get() not in range(1*nbd, 6*nbd+1):
        attention=Tk()
        attention.title("Attention!")
        alabel=Label(attention, text="Attention, vous avez prédit un nombre qui ne peut pas être généré par %d dé(s)!"%nbd, fg="black", font="Times 10 bold")
        alabel.pack()
        abouton=Button(attention, text="Okay", command=attention.destroy, cursor="dotbox")
        abouton.pack()
        attention.mainloop()
    else:
        fenetre1.destroy()
        

def fermeture_plus_tot():
    Merci=Tk()
    Merci.title("Merci!")
    MessageM=Label(Merci, text="Meric d'avoir été patient et d'avoir jouer à ce jeu!", fg="black", font="Times 10 bold")
    MessageM.pack()
    BoutonM=Button(Merci, text="Quitter", command=quit, cursor="dotbox")
    BoutonM.pack()
    Merci.mainloop()

##def tk_menu_nbdes():
## global nbd, ismenu
## ismenu=True
## nbd=tk_nbdes()
## fenetre1.destroy()
## return programme()
    

def tk_nbdes():
    global ismenu, windowDes, nbdes
## if ismenu is True:
## windowDes=Toplevel()
## else:
    windowDes=Tk()
    windowDes.title("Nombre de dés")
    labelDes=Label(windowDes, text="Combien de dés à 6 faces voulez vous utiliser? Entre 1 et 4", fg="black", font="Times 10 bold")
    labelDes.pack()
    nbdes=IntVar()
    entrydes=Entry(windowDes, textvariable=nbdes, width=3, justify=CENTER)
    entrydes.pack()
    boutonDes=Button(windowDes, text="Okay", command=continuerDes, cursor="dotbox")
    boutonDes.pack()
    windowDes.mainloop()
    ismenu=False
    return nbdes.get()

def continuerDes():
    if nbdes.get() not in range(1,5):
        attention=Tk()
        attention.title("Attention!")
        alabel=Label(attention, text="Attention, vous n'avez pas choisi entre 1 et 4 dé(s)!", fg="black", font="Times 10 bold")
        alabel.pack()
        abouton=Button(attention, text="Okay", command=attention.destroy, cursor="dotbox")
        abouton.pack()
        attention.mainloop()
    else:
        windowDes.destroy()

def tk_nomjoueurs():
    global windowNom, nomjoueur
    windowNom=Tk()
    windowNom.title("Nom")
    labelN=Label(windowNom, text="Quel est votre nom?", fg="black", font="Times 10 bold")
    labelN.pack()
    nomjoueur=StringVar()
    entryN=Entry(windowNom, textvariable=nomjoueur, width=15)
    entryN.pack()
    boutonN=Button(windowNom, text="Continuer", command=continuerNoms, cursor="dotbox")
    boutonN.pack()
    windowNom.mainloop()
    return nomjoueur.get()

def continuerNoms():
    inuse=False
    for n in joueur.noms:
        if nomjoueur.get()==n:
            inuse=True
    if len(nomjoueur.get())<2:
        attention=Tk()
        attention.title("Attention!")
        alabel=Label(attention, text="Attention, un nom contient au minimum 2 caractères!", fg="black", font="Times 10 bold")
        alabel.pack()
        abouton=Button(attention, text="Okay", command=attention.destroy, cursor="dotbox")
        abouton.pack()
        attention.mainloop()
    elif inuse==True:
        inuse=False
        attention=Tk()
        attention.title("Attention!")
        alabel=Label(attention, text="Attention, ce nom est déjà utilisé par un autre joueur!", fg="black", font="Times 10 bold")
        alabel.pack()
        abouton=Button(attention, text="Okay", command=attention.destroy, cursor="dotbox")
        abouton.pack()
        attention.mainloop()
    else:
        windowNom.destroy()

def main_programme():
    global nbd, type_de
    type_de=1
    tk_nbjoueur()
    for n in range(nbj):
        joueur.generateur(tk_nomjoueurs())
    nbd=tk_nbdes()
    programme()

def programme():
    for n in joueur.noms:
            tk_main_window(n)
            joueur.joueur_dict[n].guessing(guess,bet)
    valeur_des(nbd)
    for n in range(nbd):
        tk_dice(dict_des["dé%d"%n],n)
    for n in joueur.gagnant():
        vainqueur="Félicitation "+n+"! Vous avez gagné la ronde en prédisant le plus près de "+str(valeur_totale)+"."
    victory=Tk()
    victory.title("Bravo!")
    MessageV=Label(victory, text=vainqueur, fg="black", font="Times 10 bold")
    MessageV.pack()
    BoutonV=Button(victory, text="Okay", command=victory.destroy, cursor="dotbox")
    BoutonV.pack()
    victory.mainloop()
    
    for n in joueur.noms:
        if n in joueur.gagnant():
            joueur.joueur_dict[n].Montant(gain=joueur.mise_totale)
    if 0 in joueur.dict_montants.values():
        import webbrowser
        webbrowser.open("https://www.youtube.com/watch?v=9QS0q3mGPGg")
        return replay()
    else:
        return programme()
    
def replay():
    global Replay
    Replay=Tk()
    Replay.title("Rejouer?")
    MessageR=Label(Replay, text="Souhaitez-vous rejouer?", fg="black", font="Time 10 bold")
    MessageR.pack()
    BoutonR1=Button(Replay, text="Oui", command=rejouer, width=10, cursor="dotbox")
    BoutonR1.pack(side=LEFT)
    BoutonR2=Button(Replay, text="Non", command=fin, width=10, cursor="dotbox")
    BoutonR2.pack(side=LEFT)
    Replay.mainloop()

def rejouer():
    Replay.destroy()
    joueur.class_reset()
    main_programme()

def fin():
    Replay.destroy()
    Merci=Tk()
    Merci.title("Merci!")
    MessageM=Label(Merci, text="Meric d'avoir été patient et d'avoir jouer à ce jeu!", fg="black", font="Times 10 bold")
    MessageM.pack()
    BoutonM=Button(Merci, text="Quitter", command=Merci.destroy, cursor="dotbox")
    BoutonM.pack()
    Merci.mainloop()
    quit()
print """ Bienvenue au jeu Dés Suprêmes: le destin des intervalles. Dans ce jeu de hasard, vous aurez l'occasion de miser une somme d'argent à partir d'un montant qui vous sera alloué initialement. Votre but sera d'être le dernier joueur à rester à la fin de la partie, c'est-à-dire de ne pas être ruiné par des coups de dés défavorables trop répétés.

Plus précisément, la partie sera amorcée avec le choix de la valeur des paramètres suivants: le nombre de joueurs que vous souhaitez voir participer au jeu et le nombre de dés qui seront lancés à chaque tour. Un montant initial de 120$ sera alors attribué à chacun des participants.

À chaque tour, les joueurs devront choisir une mise en argent. Ensuite, à tour de rôle, ils doivent effectuer une prédiction quant à la somme des chiffres affichés sur les dés après lancer. Ceux-ci seront par la suite effectivement lancés. Le gagnant du tour est le joueur dont la prédiction se rapproche le plus de la somme réelle des chiffres sur les dés obtenus. Celui-ci remporte alors la mise des autres joueurs.

Votre objectif est donc de produire les meilleures prédictions pour remporter le plus de manches possibles. Si vous perdez trop de manches, votre montant sera immanquablement porté à 0$ et vous serez éliminé. Si vous parvenez à survivre jusqu'à la fin, vous gagnerez la partie et la totalité de l'argent de chacun des joueurs.

N. B. : En aucun vous ne pourrez parier plus que le montant possédé au moment de la mise. Les emprunts sont donc interdits.

Sur ce, sans plus tarder, bon jeu à tous!"""
ismenu=False
main_programme()
