# -*- coding: cp1252 -*-

## Importations
from Tkinter import *#importer la bibliotheque python pour faire de l'interface graphique
import time#importer la bibliotheque python time
import random#importer la bibliotheque python random
import webbrowser#importer la bibliotheque python webbroser


## Classes
class joueur: #création de la classe joueurs
    "Ensemble d'attributs que possede chaque joueur"
    ##Variables et dictionnaires de la classe
    compte=0
    mise_totale=0#variable représentant la mise totale durant un tour de jeu
    dict_montants={}#dictionnaire des montants des joueurs
    dict_guess={}#dictionnaire contenant les valeur sur le quel les joueurs misent
    dict_bet={}#dictionnaire contenant les mises
    joueur_dict={}#dictionnaire des joueurs
    noms=[]#liste contenant les noms des joueurs
    dict_ecarts={}#liste contenant l'écart entre la mise de chaque joueur et le score que le programme a generer

    ##Méthodes d'instance
    def __init__(self,nom="",montant_initial=0):#méthode qui s'enclenche avec l'appel de la classe
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

    ##Méthodes de classe
    @staticmethod
    def generateur(nom):
        joueur.joueur_dict[nom]=joueur(nom,120)#crée une instance de la classe ‘joueur' dans le #dictionnaire
        joueur.noms=joueur.joueur_dict.keys()
        return u"Vous avez créé un nouveau joueur:%s"%nom
    
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

## Dictionnaires et variables
dict_des={}

##Fonctions
def main_programme():#definition du programme principal
    """Fonction-programme global du jeu. En lançant cette fonction le jeu débute (ou recommence) du tout début"""
    global nbd, type_de#mettre global nbd et type_de
    type_de=1 #Variable identifiant le type de dé. Soit 1 soit 2.
    tk_nbjoueur()#appele cette fonction pour savoir le nombre de joueur
    for n in range(nbj):# pour un nombre de joueur représenter par nbj
        joueur.generateur(tk_nomjoueurs(n))#appele la methode joueur.générateur pour chaque nombre de joueur
    nbd=tk_nbdes()#la variable nbd est égale à la valeur retourné par la fonction tk_nbdes
    return tk_programme()#retouner tk_programme

def tk_nbjoueur():#définition d'une fonction qui determine le nombre de joueur
    """Fonction contenant un interface graphique tkinter pour demander le nombre de joueurs."""
    global window1,nbj#mettre en valeur globale window1 et nbj
    window1=Tk()#window1 est une fenetre dans tkinter
    window1.title("Combien de joueur?")#le titre de la fenetre window1 est donné
    label1=Label(window1,text="Combien de joueurs vont jouer? Entre 2 et 4.", font="Time 10 bold", fg="black")# un text gras, en noir time demande le nombre de joueur dans un label 
    label1.pack()#chargement de ce qu'il faut pour pouvoir afficher label1
    nbj=StringVar()#nbj est un variable de texte
    nbj.set("2")# la valeur de nbj est donné
    entry1=Entry(window1, textvariable=nbj, justify=CENTER, width=2)#une case ou l'utilisateur peur écrire quelque chose ou il y a deja nbj
    entry1.pack()#chargement de ce qu'il faut pour pouvoir afficher entry1
    button1=Button(window1, text="Okay", command=tk_nbjoueur_verif, cursor="dotbox")#création d'un bouton qui ferme la fenetre window
    button1.pack()#chargement de ce qu'il faut pour pouvoir afficher Button
    window1.mainloop()#cette fonction est appelé pour permettre a la fenetre de s'afficher
    nbj=int(nbj.get())#la valeur de nbj devient la valeur de nbj, mais en chiffre
    return #fermeture de la fontction

def tk_nbjoueur_verif():#fonction qui verifie si le nombre de joueur est bon
    """Fonction vérifiant le nombre de joueur entré dans l'interface graphique de tk_nbjoueur() et créant un avertissement avec tkinter si nécessaire"""
    global nbj#mettre en valeur globale nbj
    if nbj.get().isdigit()==False:#si nbj ne contient pas de chiffre
        attention=Tk()#attention est une fenetre dans tkinter
        attention.title("Attention!")#le titre de la fenetre ettention est donné
        alabel=Label(attention, text="Attention, vous n'avez pas entré uniquement des chiffre!", fg="black", font="Times 10 bold")# un text gras, en noir time dis au joueur qu'il n'as pas rentrer que des chiffre pour le nombre de joueur
        alabel.pack()#chargement de ce qu'il faut pour pouvoir afficher alabel
        abouton=Button(attention, text="Okay", command=attention.destroy, cursor="dotbox")#création d'un bouton qui ferme la fenetre attention
        abouton.pack()#chargement de ce qu'il faut pour pouvoir afficher abutton
        attention.mainloop()#cette fonction est appelé pour permettre a la fenetre de s'afficher
    elif int(nbj.get()) in (2,3,4):#si nbj est soit 2, 3 ou 4
        window1.destroy()#détruire la fenetre window1
    else:#sinon
        window2=Toplevel()#window2 est une fenetre dans tkinter
        window2.title("Attention!")#le titre de la fenetre ettention est donné
        label2=Label(window2, text="Attention, vous n'avez pas entrer un nombre de joueurs valide!", font="Times 10 bold", fg="black")# un text gras, en noir time dis au joueur qu'il n'as pas rentrer un chiffre valide pour le nombre de joueur
        label2.pack()#chargement de ce qu'il faut pour pouvoir afficher label2
        button2=Button(window2, text="Okay", command=window2.destroy, cursor="dotbox")#création d'un bouton qui ferme la fenetre attention
        button2.pack()#chargement de ce qu'il faut pour pouvoir afficher abutton
        window2.grid()
    return #fermeture de la fontction

def tk_nomjoueurs(num_joueur):#fonction qui definit les nombre de joueurs
    """Fonction avec interface tkinter demandant le nom d'un joueur"""
    global windowNom, nomjoueur#mettre en valeur globale windowNom et nomjoueur
    windowNom=Tk()#windowNom est une fenetre dans tkinter
    windowNom.geometry("175x65")#la taille de windowNom est donné en pixel
    windowNom.title("Joueur %d"%(num_joueur+1))#le titre de la fenetre est son numéro, soit num_joueur, qui est compté ailleurs, plus 1
    labelN=Label(windowNom, text="Quel est votre nom?", fg="black", font="Times 10 bold")# un text gras, en noir time demande au joueur son nom
    labelN.pack()#chargement de ce qu'il faut pour pouvoir afficher labelN
    nomjoueur=StringVar()#nomjoueur est un variable de texte
    entryN=Entry(windowNom, textvariable=nomjoueur, width=15)# la valeur de nomjoueur est donné dans une cette case
    entryN.pack()#chargement de ce qu'il faut pour pouvoir afficher entryN
    boutonN=Button(windowNom, text="Continuer", command=tk_nomjoueurs_verif, cursor="dotbox")#Bouton pour fermer la fenetre
    boutonN.pack()#chargement de ce qu'il faut pour pouvoir afficher buttonN
    windowNom.mainloop()#cette fonction est appelé pour permettre a la fenetre de s'afficher
    return nomjoueur.get()#retourner la valeur de nom joueur

def tk_nomjoueurs_verif():#fonction qui verifie le si le nom des joueurs est valide
    """Fonction analysant le noms des joueurs entrés par la fonction tk_nbjoueurs() et créant un avertissement avec tkinter si nécessaire"""
    inuse=False#pas utlisé
    for n in joueur.noms:#pour tous les noms de joueurs faire ce qui suit
        if nomjoueur.get()==n:#si un nom de joueur est utilisé
            inuse=True#inuse devient vrai
    if len(nomjoueur.get())<2:#si la longeur d'un nom est inférieur a 2
        attention=Tk()#attention est une fenetre dans tkinter
        attention.title("Attention!")#titre de la fenetre
        alabel=Label(attention, text="Attention, un nom contient au minimum 2 caractères!", fg="black", font="Times 10 bold")#label qui dit qui faut min 2 caracteres a un nom
        alabel.pack()#chargement de albal
        abouton=Button(attention, text="Okay", command=attention.destroy, cursor="dotbox")#bouton qui permet la detruction de la fenetre
        abouton.pack()#chargement de abutton
        attention.mainloop()#fonction   qui permet a a fenetre de rester ouverte
    elif inuse==True:#si un nom est utilisé
        inuse=False#inuse redevient faux, pour ne pas revenir ici indéféniment
        attention=Tk()#ouverture d'une fenetre tkinter
        attention.title("Attention!")#titre donné a la fenetre
        alabel=Label(attention, text="Attention, ce nom est déjà utilisé par un autre joueur!", fg="black", font="Times 10 bold")#explication que le nom choisi est deja utilisé
        alabel.pack()#chargement de alabel
        abouton=Button(attention, text="Okay", command=attention.destroy, cursor="dotbox")#bouton qui permet la detruction de la fenetre
        abouton.pack()#chargement de abutton
        attention.mainloop()#fonction   qui permet a a fenetre de rester ouverte
    else:
        windowNom.destroy()#
    return #fermeture de la fonction

def tk_nbdes():#fonction qui demande le nombre de dé
    """Fonction avec interface tkinter qui demande le nombre de dé utilisé"""
    global windowDes, nbdes#mise en valeur globale
    windowDes=Tk()#windowDes est une fenetre dans tkinter
    windowDes.title("Nombre de dés")#le titre de la fenetre window1 est donné
    labelDes=Label(windowDes, text="Combien de dés à 6 faces voulez vous utiliser? Entre 1 et 4", fg="black", font="Times 10 bold")#label qui demande le nombre de dé
    labelDes.pack()#chargement de labelDes
    nbdes=StringVar()#nbdes est un variable de texte
    nbdes.set("1")# la valeur de nbdes est donné
    entrydes=Entry(windowDes, textvariable=nbdes, width=3, justify=CENTER)#une case ou l'utilisateur peur écrire quelque chose pour defini nbdes
    entrydes.pack()#chargement de entrydes
    boutonDes=Button(windowDes, text="Okay", command=tk_nbdes_verif, cursor="dotbox")#bouton qui vérifie le nombe de dé
    boutonDes.pack()#chargement de boutonDes
    windowDes.mainloop()#fonction   qui permet a a fenetre de rester ouverte
    return int(nbdes.get())#retourner nbdes en chiffre

def tk_nbdes_verif():#fonction qui vérifie le nombre de dé
    """Fonction vérifiant le nombre de dé donné dans la fonction tk_nbdes() et affichant un avertissement avec tkinter au besoin."""
    if nbdes.get().isdigit()==False:#si le nombre de dé n'est pas que des chiffre
        attention=Tk()#ouverture fenetre en tkinter
        attention.title("Attention!")#titre de la fenetre
        alabel=Label(attention, text="Attention, vous n'avez pas entré uniquement des chiffre!", fg="black", font="Times 10 bold")#label qui explique que l'utilisateur n'a pas rentré que des chiffre
        alabel.pack()#charment de alabel
        abouton=Button(attention, text="Okay", command=attention.destroy, cursor="dotbox")#bouton qui detruit la fenetre
        abouton.pack()#chargement de a bouton 
        attention.mainloop()#cette fonction est appelé pour permettre a la fenetre de s'afficher
    elif int(nbdes.get()) not in range(1,5):#si nbdes nest pas 1,2,3 ou 4
        attention=Tk()#attention est une fenetre dans tkinter
        attention.title("Attention!")#titre de la fenetre
        alabel=Label(attention, text="Attention, vous n'avez pas choisi entre 1 et 4 dé(s)!", fg="black", font="Times 10 bold")#label qui explique que le nombre de dé est mauvais
        alabel.pack()#chargement de alabel
        abouton=Button(attention, text="Okay", command=attention.destroy, cursor="dotbox")#bouton qui détruit la fenetre
        abouton.pack()#chargement de a bouton 
        attention.mainloop()#cette fonction est appelé pour permettre a la fenetre de s'afficher
    else:
        windowDes.destroy()#détruire la fenetre 
    return #fermeture de la fonction

def tk_programme():
    """Fonction-programme pour un tour de jeu. En lançant cette fonction, on part un nouveau tour de jeu. Elle utilise d'ailleurs tkinter pour afficher des félicitations au(x) vainqueur(s)"""
    for n in joueur.noms:#pour des nombre allan jusqua joueur.noms
            tk_main_window(n)#ouverture d'une fenetre
            joueur.joueur_dict[n].guessing(guess,bet)
    valeur_des(nbd)
    for n in range(nbd):#pour n jusqua le nombre de dé
        tk_brassage(dict_des["dé%d"%n],n)#il faut un nombre de brassage équivalent au nombre de dé
    for n in joueur.gagnant():#pour n qui est le 
        vainqueur=u"Félicitation "+n+u"! Vous avez gagné la ronde en prédisant le plus près de "+str(valeur_totale)+"."#remerciments au vainceur
        victory=Tk()#ouverture fenetre 
        victory.title("Bravo!")#titre de la fenetre
        MessageV=Label(victory, text=vainqueur, fg="black", font="Times 10 bold")#écrire dans un label vainceur
        MessageV.pack()#charmegemt du label
        portion=Frame(victory)#dans un frame
        portion.pack()#charmement de portion
        for n in range(nbd):
            if n==0:
                 fichier_face1="d6-singleface-%d.gif"%dict_des["dé%d"%n]
                 image_de1=PhotoImage(file=fichier_face1)
                 LabelV1=Label(portion, bg="white", cursor="pirate", image=image_de1)
                 LabelV1.pack(expand=1, side=LEFT)
            elif n==1:
                 fichier_face2="d6-singleface-%d.gif"%dict_des["dé%d"%n]
                 image_de2=PhotoImage(file=fichier_face2)
                 LabelV2=Label(portion, bg="white", cursor="pirate", image=image_de2)
                 LabelV2.pack(expand=1, side=LEFT)
            elif n==2:
                 fichier_face3="d6-singleface-%d.gif"%dict_des["dé%d"%n]
                 image_de3=PhotoImage(file=fichier_face3)
                 LabelV3=Label(portion, bg="white", cursor="pirate", image=image_de3)
                 LabelV3.pack(expand=1, side=LEFT)
            elif n==3:
                 fichier_face4="d6-singleface-%d.gif"%dict_des["dé%d"%n]
                 image_de4=PhotoImage(file=fichier_face4)
                 LabelV4=Label(portion, bg="white", cursor="pirate", image=image_de4)
                 LabelV4.pack(expand=1, side=LEFT)
        BoutonV=Button(victory, text="Okay", command=victory.destroy, cursor="dotbox")
        BoutonV.pack()
        victory.mainloop()
    for n in joueur.noms:
        if n in joueur.gagnant():
            joueur.joueur_dict[n].Montant(gain=joueur.mise_totale/len(joueur.gagnant()))
    if 0 in joueur.dict_montants.values():
        webbrowser.open("https://www.youtube.com/watch?v=9QS0q3mGPGg")
        return tk_rejouer()
    else:
        return tk_programme()

def tk_main_window(nom):#fenetre principale
    """Fonction qui fait apparaitre avec tkinter une fenêtre de jeu où l'on peu miser et prédire, ainsi que voir l'argent de chaque joueur."""
    ##Variables et dictionnaires de la fonction
    global bet,guess,fenetre1,name# mettre globale plusieurs valeur
    name=nom#atribution de valeur
    bet=None#la mise est nul
    dict_label_montant={}#le dictionnaire des montants est vide
    dict_label_nom={}#le dictionnaire des noms est vide

    ##Commandes tkinter
    fenetre1=Tk()#ouverture fenete1
    fenetre1.title(nom)#titre de la fenetre qui est le nom du joueur
    fenetre1.geometry("500x500")#grosseur de la fenetre en pixel
    
    division=Frame(fenetre1)#nom de la premiere partie
    division.pack(side=LEFT, fill=BOTH, expand=1)#chargement de division
    
    section2=Frame(division)#faire un morceau dans division
    section2.pack(fill=X)#chargement de setion2
    libele1=Label(section2, text="Choisissez une mise", fg="black", font="Times 10 bold")#label pour une mise
    libele1.pack()#chargemetn du label
    bet=StringVar()#variable contenant le bet
    bet.set("1")#donner la valeur textuelle de 1 a bet
    bouton1=Button(section2, text="1", width=9, command=lambda:bet.set("1"), cursor="dotbox")#bouton pour une mise prédeterminé de 1
    bouton1.pack(pady=1)#chargement du bouton
    bouton2=Button(section2, text="5", width=9, command=lambda:bet.set("5"), cursor="dotbox")#bouton pour une mise prédeterminé de 5
    bouton2.pack(pady=1)
    bouton3=Button(section2, text="10", width=9, command=lambda:bet.set("10"), cursor="dotbox")#bouton pour une mise prédeterminé de 10
    bouton3.pack(pady=1)#chargement du bouton
    bouton4=Button(section2, text="20", width=9, command=lambda:bet.set("20"), cursor="dotbox")#bouton pour une mise prédeterminé de 20
    bouton4.pack(pady=1)#chargement du bouton
    bouton5=Button(section2, text="50", width=9, command=lambda:bet.set("50"), cursor="dotbox")#bouton pour une mise prédeterminé de 50
    bouton5.pack(pady=1)#chargement du bouton
    bouton6=Button(section2, text="Autre mise", width=9, command=tk_autremise, cursor="dotbox")#bouton pour une mise a déterminé
    bouton6.pack(pady=1)#chargement du bouton
    libele3=Label(section2, textvariable=bet, bg="black", fg="white")#label qui montre la mise finale
    libele3.pack(fill=X)#chargement du bouton
    
    section3=Frame(division)#autre morceau dans division
    section3.pack(side=BOTTOM, pady=1, fill=X)#chargement de section 3
    libele2=Label(section3, text="Quel nombre prédisez-vous?", fg="black", font="Times 10 bold")#label qui demande la nombre prédit
    libele2.pack()#chargement de libele2
    guess=StringVar()#variable contenant le guess
    guess.set(str(nbd))# le nombre estimé est donné comme valeur a guess
    saisie1=Entry(section3, textvariable=guess, justify=CENTER, width=3)#l'utilisateur peut rentré le nombre qu'il veut
    saisie1.pack()#chargement de saisie1
    libele4=Label(section3, textvariable=guess, bg="black", fg="white")
    libele4.pack(fill=X)#chargement de libele4
    bouton7=Button(section3, text="Continuer", width=9, command=tk_main_window_verif, cursor="dotbox")#bouton qui détruit la fenetre
    bouton7.pack(pady=1)#chargement du bouton 7
    
    section4=Frame(fenetre1, width=200, height=500, background="white", cursor="pirate")
    section4.pack(side=RIGHT)
    libele5=Label(section4, text="Voici vos montants:", fg="black",  font="Times 12 bold", background="white")
    libele5.pack()
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
    menu1.add_command(label="Recommencer", command=recommencer)
    menu1.add_command(label="Quitter", command=tk_quitter)

    menu2=Menu(menus, tearoff=0)
    menus.add_cascade(label="Personnalisation", menu=menu2)
    sousmenu=Menu(menu2, tearoff=0)
    menu2.add_cascade(label="Type de design de dé", menu=sousmenu)
    sousmenu.add_command(label="Simplifié", command=lambda:type(1))
    sousmenu.add_command(label="Réaliste", command=lambda:type(2))
    
    menu3=Menu(menus, tearoff=0)
    menus.add_cascade(label="Aide", menu=menu3)
    menu3.add_command(label="Règles", command=tk_aide)
    
    fenetre1.config(menu=menus)
    fenetre1.mainloop()


    ##Commandes post-interface
    bet=int(bet.get())
    guess=int(guess.get())
    return 

def tk_autremise():
    """Fonction créant une fenêtre tkinter offrant la possibilité d'entrer une autre mise et attribuant cette valeur à bet"""
    global bet, fenetre2
    fenetre2=Toplevel()
    fenetre2.title("Autre mise?")
    fenetre2.geometry("200x50")
    saisie2=Entry(fenetre2, textvariable=bet, justify=CENTER, width=3)
    bouton8=Button(fenetre2, text="Confirmer", command=tk_autremise_verif, cursor="dotbox")
    saisie2.pack()
    bouton8.pack(pady=1)
    fenetre2.grid()
    return

def tk_autremise_verif():
    """Fonction vérifiant que la mise entrée dans l'interface tkinter de tk_autremise() ne contient pas des caractères autres que numériques."""
    if bet.get().isdigit()==False:
        attention=Tk()
        attention.title("Attention!")
        alabel=Label(attention, text="Attention, vous n'avez pas entré uniquement des chiffre!", fg="black", font="Times 10 bold")
        alabel.pack()
        abouton=Button(attention, text="Okay", command=attention.destroy, cursor="dotbox")
        abouton.pack()
        attention.mainloop()
    else:
        fenetre2.destroy()
    return

def tk_main_window_verif():
    """Fonction vérifiant que les mises et prédictions entrées dans tk_main_window() soient valides et affichant un message d'avertissement avec tkinter au besoin"""
    if guess.get().isdigit()==False:
        attention=Tk()
        attention.title("Attention!")
        alabel=Label(attention, text="Attention, vous n'avez pas entré uniquement des chiffre!", fg="black", font="Times 10 bold")
        alabel.pack()
        abouton=Button(attention, text="Okay", command=attention.destroy, cursor="dotbox")
        abouton.pack()
        attention.mainloop()
    elif int(bet.get())>joueur.joueur_dict[name].montant:
        attention=Tk()
        attention.title("Attention!")
        alabel=Label(attention, text="Attention, vous avez misé plus que vous ne possédez!", fg="black", font="Times 10 bold")
        alabel.pack()
        abouton=Button(attention, text="Okay", command=attention.destroy, cursor="dotbox")
        abouton.pack()
        attention.mainloop()
    elif int(bet.get())<=0:
        attention=Tk()
        attention.title("Attention!")
        alabel=Label(attention, text="Attention, vous avez misé 0 ou moins!", fg="black", font="Times 10 bold")
        alabel.pack()
        abouton=Button(attention, text="Okay", command=attention.destroy, cursor="dotbox")
        abouton.pack()
        attention.mainloop()
    elif int(guess.get()) not in range(1*nbd, 6*nbd+1):
        attention=Tk()
        attention.title("Attention!")
        alabel=Label(attention, text="Attention, vous avez prédit un nombre qui ne peut pas être généré par %d dé(s)!"%nbd, fg="black", font="Times 10 bold")
        alabel.pack()
        abouton=Button(attention, text="Okay", command=attention.destroy, cursor="dotbox")
        abouton.pack()
        attention.mainloop()
    else:
        fenetre1.destroy()
    return 

def recommencer():
    """Fonction fermant la fenêtre d'interface, vidant les dictionnaires de la classe et recommençant le programme"""
    fenetre1.destroy()
    joueur.class_reset()
    return main_programme()

def tk_quitter():
    """Fonction affichant un remerciement avec tkinter qui quitte le programme si on clique sur le bouton."""
    Merci=Tk()
    Merci.title("Merci!")
    MessageM=Label(Merci, text="Meric d'avoir été patient et d'avoir jouer à ce jeu!", fg="black", font="Times 10 bold")
    MessageM.pack()
    BoutonM=Button(Merci, text="Quitter", command=quit, cursor="dotbox")
    BoutonM.pack()
    Merci.mainloop()
    return 

def type(n):
    """Fonction qui indique d'utiliser les images de dés simplifiées(n=1), soit toutes avec le même chiffre sur toutes ses faces ou les images de dés réalistes(n=2), soit avec des chiffres différent sur les faces voisines"""
    global type_de
    type_de=n
    return 

def tk_aide():
    """Fonction créant avec tkinter une fenêtre contenant les règles et les instructions du jeu"""
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

Sur ce, sans plus tarder, bon jeu à tous!""")
    texte1.config(state=DISABLED)
    texte1.pack(fill=Y, expand=1)
    barredefilement.config(command=texte1.yview)
    fenetre3.grid()
    return 

def valeur_des(nbd):
    """Fonction qui assigne une valeur aléatoire à chaque dé et met la somme dans une variable globale.'nbd'=nombre de dés"""
    global dict_des,valeur_totale
    for n in range(int(nbd)):
        dict_des["dé%d"%n]=random.randint(1,6)#chaque dé se voit assigner une valeur aléatoire #dans un dictionnaire
    valeur_totale=sum(dict_des.values())
    return

def tk_brassage(de_final, numde):
    """Fonction qui affiche une fenêtre tkinter contenant une succession d'image simulant le brassage d'un dé"""
    global section1, comp, windowDice, last_numero, definal
    comp,last_numero =0,0
    definal=de_final
    num_de=numde+1
    windowDice=Tk()
    windowDice.geometry("130x112")
    windowDice.title("Dé #%d"%num_de)
    section1=Canvas(windowDice, width=130, height=112,background="white", cursor="pirate")
    section1.pack()
    windowDice.after(100,tk_succession_image)
    windowDice.mainloop()
    return
    
def tk_succession_image():
    """Fonction qui génère la succession d'image montrée dans l'interface tkinter de tk_brassage()"""
    global comp, image_de, img_de, imgde, image_de_final, definal, imgdefinal, imgfinale, last_numero
    if comp<20:
        numero_img=random.randint(1,6)
        while numero_img==last_numero:
            numero_img=random.randint(1,6)
        last_numero=numero_img
        image_de="d6-face%d-%d.gif"%(numero_img,type_de)
        img_de=PhotoImage(file=image_de)#ref
        imgde=section1.create_image(65,56, image=img_de)
        comp=comp+1
        windowDice.after(100,tk_succession_image)
    elif comp==20:
## definal=3
        image_de_final="d6-face%d-%d.gif"%(definal,type_de)
        imgdefinal=PhotoImage(file=image_de_final)#ref
        imgfinale=section1.create_image(65,56,image=imgdefinal)
        windowDice.after(1000, windowDice.destroy)
    return

def tk_rejouer():
    """Fonction demandant si on veut rejouer à l'aide d'une fenêtre tkinter."""
    global Replay
    Replay=Tk()
    Replay.title("Rejouer?")
    MessageR=Label(Replay, text="Souhaitez-vous rejouer?", fg="black", font="Time 10 bold")
    MessageR.pack()
    BoutonR1=Button(Replay, text="Oui", command=tk_rejouer_oui, width=10, cursor="dotbox")
    BoutonR1.pack(side=LEFT)
    BoutonR2=Button(Replay, text="Non", command=tk_rejouer_non, width=10, cursor="dotbox")
    BoutonR2.pack(side=LEFT)
    Replay.mainloop()
    return

def tk_rejouer_oui():
    """Fonction fermant la fenetre tkinter ouverte par tk_rejouer, remettant la classe à neuf et renvoyant à la fonction main_programme()"""
    Replay.destroy()
    joueur.class_reset()
    return main_programme()

def tk_rejouer_non():
    """Fonction fermant la fenetre tkinter ouverte par tk_rejouer, affichant des remerciement et fermant le programme"""
    Replay.destroy()
    Merci=Tk()
    Merci.title("Merci!")
    MessageM=Label(Merci, text="Meric d'avoir été patient et d'avoir jouer à ce jeu!", fg="black", font="Times 10 bold")
    MessageM.pack()
    BoutonM=Button(Merci, text="Quitter", command=Merci.destroy, cursor="dotbox")
    BoutonM.pack()
    Merci.mainloop()
    return quit()


## Code à la "racine" du programme 
print """ Bienvenue au jeu Dés Suprêmes: le destin des intervalles. Dans ce jeu de hasard, vous aurez l'occasion de miser une somme d'argent à partir d'un montant qui vous sera alloué initialement. Votre but sera d'être le dernier joueur à rester à la fin de la partie, c'est-à-dire de ne pas être ruiné par des coups de dés défavorables trop répétés.

Plus précisément, la partie sera amorcée avec le choix de la valeur des paramètres suivants: le nombre de joueurs que vous souhaitez voir participer au jeu et le nombre de dés qui seront lancés à chaque tour. Un montant initial de 120$ sera alors attribué à chacun des participants.

À chaque tour, les joueurs devront choisir une mise en argent. Ensuite, à tour de rôle, ils doivent effectuer une prédiction quant à la somme des chiffres affichés sur les dés après lancer. Ceux-ci seront par la suite effectivement lancés. Le gagnant du tour est le joueur dont la prédiction se rapproche le plus de la somme réelle des chiffres sur les dés obtenus. Celui-ci remporte alors la mise des autres joueurs.

Votre objectif est donc de produire les meilleures prédictions pour remporter le plus de manches possibles. Si vous perdez trop de manches, votre montant sera immanquablement porté à 0$ et vous serez éliminé. Si vous parvenez à survivre jusqu'à la fin, vous gagnerez la partie et la totalité de l'argent de chacun des joueurs.

N. B. : En aucun vous ne pourrez parier plus que le montant possédé au moment de la mise. Les emprunts sont donc interdits.

Sur ce, sans plus tarder, bon jeu à tous!"""# écrire ce texte
main_programme()# appeler le programme
