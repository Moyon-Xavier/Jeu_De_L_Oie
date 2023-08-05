# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 21:43:58 2021

@author: moyon
"""

"""importation des modules......................................................
................................................................................"""
import pygame_jeu_de_oie
from random import *
import time

"""Creation la classe plateau qui va stocker le plateau et va gerer les interractions
 liee aux plateaux..................................................................
 ............................"""


class plateau():
    def __init__(self,liste_jr):
        self.liste_case=crea_pla(liste_jr)
        self.case_spe=[]
        self.liste_jr=liste_jr
        for i in range(len(self.liste_case[1:])):
            if type(self.liste_case[i][0])!=int:
                self.case_spe.append(self.liste_case[i])
        print(self.case_spe)


    def joueurpos(self,jr):
        self.liste_case[jr.position].append(jr)
    def cases_prises(self,pos):
       # print("case prises test ", self.liste_case)
        return self.liste_case[pos][1] != ""

    def echangespos(self,jr,pos1,pos2):#pos1 est la position du joueur qui joue actuellement pos 2 poshypot
        print("self.liste_case[pos1]:",self.liste_case[pos1],"self.liste_case[pos2]",self.liste_case[pos2])

        #for i in self.liste_case[pos1][1:]:
            #print("pos1 : ",i.nom)

        #for i in self.liste_case[pos2][1:]:
            #print("pos2 : ",i.nom)
        if self.liste_case[pos2] in self.case_spe and pos2!=pos1:# on ajoute une condition pour permettre aux joueur d'etre sur une meme case et de debloquer d'autres joueur(puits , ..)
            #print("spe")
            if self.liste_case[pos2][0]=="hotel":
                 self.deplacement(pos2 , jr)#on fait avancer normalement le joueur

            elif self.liste_case[pos2][0]=="prison":
                #print("eh o ")
                #on fait avancer normalement le joueur

                #self.liste_case[pos1][1].prisontour=None#On se libere soi meme et l'autre joueur
                #if self.cases_prises(pos2):

                if self.liste_case[pos2][-1].prisontour!=None:
                    self.liste_case[pos2][-1].prisontour=None

                self.deplacement(pos2 , jr)


            elif self.liste_case[pos2][0]=="puit":
                txt=("Bravo , ", self.liste_case[pos2][-1].nom ," Tu as fait preuve de malice et tu as reussi a berner ",self.liste_case[pos1][1].nom,"Qui prend desormais ta place dans le puit")
                pygame_jeu_de_oie.aff_casepos(self,txt)

                self.liste_case[pos2][-1].puittour=None
                self.deplacement(pos2 , jr)#on fait avancer normalement le joueur

            else:

                jr.position=pos2#on inverse les position des joueurs de la class Joueur
                self.liste_case[pos2][1].position=pos1#
                self.liste_case[pos1][self.liste_case[pos1].index(jr)],self.liste_case[pos2][1]=self.liste_case[pos2][1],self.liste_case[pos1][self.liste_case[pos1].index(jr)]

                print("Gare a toi voyageur du Temps , tu ne peux pas etre present sur la case de ton adversaire , Ainsi Commence un combat acharner entre ", self.liste_case[pos1][1].nom ,"et", self.liste_case[pos2][1].nom)
                time.sleep(1)
                print("Le Gagnant est evidement ",self.liste_case[pos1][1].nom ," Bravo A lui , il echange alors sa place avec ",self.liste_case[pos2][1].nom)

        elif pos1!=pos2:#Cas de Base
            self.liste_case[pos2][1].position=pos1#on inverse les position des joueurs de la class Joueur
            self.liste_case[pos1][self.liste_case[pos1].index(jr)].position=pos2#

            self.liste_case[pos1][self.liste_case[pos1].index(jr)],self.liste_case[pos2][1]=self.liste_case[pos2][1],self.liste_case[pos1][self.liste_case[pos1].index(jr)]

            print("Gare a toi voyageur du Temps , tu ne peux pas etre present sur la case de ton adversaire , Ainsi Commence un combat acharner entre ", self.liste_case[pos1][1].nom ,"et", self.liste_case[pos2][1].nom)
            time.sleep(1)
            print("Le Gagnant est evidement ",self.liste_case[pos1][1].nom ," Bravo A lui , il echange alors sa place avec ",self.liste_case[pos2][1].nom)




    def deplacement(self,pos_hypot,jr):
        if len(self.liste_case[jr.position])<=2:#self.cases_prises a remplacer par liste_case[0]==["depart",jr]
            self.liste_case[jr.position][1]=""
            if self.liste_case[pos_hypot][1]=="":
                self.liste_case[pos_hypot][1]=jr
            else:
                self.liste_case[pos_hypot].append(jr)
        else:
            self.liste_case[jr.position].pop(self.liste_case[jr.position].index(jr))
            if self.liste_case[pos_hypot][1]=="":
                self.liste_case[pos_hypot][1]=jr
            else:
                self.liste_case[pos_hypot].append(jr)

    def est_jrsurcasespe(self,pos_hypot,jr):

        if type(self.liste_case[pos_hypot][0])==str and pos_hypot!=0:#si il s'agit d'une case spe != de de depart
            if jr.hoteltour==None and jr.prisontour==None:
                if jr.puittour==None:
                    if self.liste_case[pos_hypot][0]=="prison":


                        return (True,3)#si le joueur va sur la case prison pour la premiere fois
                    else:
                        return (True,1)#si le joueur est sur une autre case speciale

        if type(self.liste_case[jr.position][0])==str and jr.position!=0:
            if (jr.hoteltour!=None or  jr.prisontour!=None) or jr.puittour!=None:#si c'est egale a None alors il le jopueur veint de sortir du puits ou de la prison,..,.....
                return (True,2)#si le joueur vient d'une case speciale de type hotel prison et puits

        return (False,1)#si le joueur ne va pas sur une case speciale

    def jrsurcasespe(self,de,poshypot,jr):
        if self.est_jrsurcasespe(poshypot,jr)==(True,1) or self.est_jrsurcasespe(poshypot,jr)==(True,3):
            if self.liste_case[poshypot][0]=="oie":
                return cases_oie(de ,jr , poshypot,self)

            if self.liste_case[poshypot][0]=="pont":
                return cases_pont(de , jr , poshypot,self)

            if self.liste_case[poshypot][0]=="hotel":
                return cases_hotelarri(de, jr ,poshypot,self)

            if self.liste_case[poshypot][0]=="puit":
                return cases_puitarri(de, jr ,poshypot,self)

            if self.liste_case[poshypot][0]=="labyrinthe":
                return cases_labyrinthe(de,jr,poshypot,self)

            if self.liste_case[poshypot][0]=="prison":
                return cases_prisonarri(jr,poshypot,self)

            if self.liste_case[poshypot][0]=="mort":
                return cases_mort(de,jr,poshypot,self)

        if self.est_jrsurcasespe(poshypot,jr)==(True,2):


            if self.liste_case[jr.position][0]=="hotel":
                return cases_hotelfin(de, jr ,poshypot,self)

            if self.liste_case[jr.position][0]=="puit":
                return cases_puitfin(de, jr ,poshypot,self)

            if self.liste_case[jr.position][0]=="prison":
                return cases_prisonfin(de,jr,poshypot,self)
        else:
            return poshypot


    def affichage(self):
        print("on affi")
        '''for i in range(len(self.liste_case)):
            print("|| ",self.liste_case[i][0],end="")
            for z in range(1,len(self.liste_case[i])):
                if self.liste_case[i][z]=="":
                    print(" *",end="    ")
                else:

                    print("  ",self.liste_case[i][z].nom)
            print("|| ")'''
        plateauvisu=[["Depart","1","2","3","4","Oie","Pont","7","8","Oie"],
        ["","28","29","30","Puit","Oie","33","34","35","10"],
        ["","Oie","48","49","Oie","51","Prison","53","Oie","11"],
        ["","26","47","60","61","62","63","Oie","37","12"],
        ["","25","46","Oie","LA MORT","57","56","55","38","13"],
        ["","24","Oie","44","43","Labyrinthe","Oie","40","39","Oie"],
        ["","Oie","22","21","20","Hotel","Oie","17","16","15"]]
        plateau=[["0","1","2","3","4","5","6","7","8","9"],
        ["","28","29","30","31","32","33","34","35","10"],
        ["","27","48","49","50","51","52","53","36","11"],
        ["","26","47","60","61","62","63","54","37","12"],
        ["","25","46","59","58","57","56","55","38","13"],
        ["","24","45","44","43","42","41","40","39","14"],
        ["","23","22","21","20","19","18","17","16","15"]]

        self.ecran_accueil=pygame_jeu_de_oie.Ecran((139,69,19),plateauvisu,plateau)
        #pygame_jeu_de_oie.affichagepl(self.ecran_accueil,self.liste_jr)



def cases_oie(de, jr ,poshypot,plateaudejeu):
    newpos=sum(de)+poshypot
    txt=("Interdiction de restee sur les cases 'oie' vas t-en aussi vite que tu peux va a la case ",newpos  )
    pygame_jeu_de_oie.aff_casepos(plateaudejeu,txt)
    return newpos


def cases_pont(de, jr ,poshypot,plateaudejeu):
     txt=("Bonjour a toi jeune Voyageur Bienvenue Sur le petit pont de bois qui te premettra d'aller jusqu'a la case 12")
     pygame_jeu_de_oie.aff_casepos(plateaudejeu,txt)
     return 12

def cases_hotelarri(de, jr ,poshypot,plateaudejeu):
    txt=("Bienvenue a l'hotel 3 tours tu devras attendre Afin de pouvoir sortir")
    pygame_jeu_de_oie.aff_casepos(plateaudejeu,txt)
    jr.hoteltour=0
    return poshypot

def cases_puitarri(de, jr ,poshypot,plateaudejeu):
    if not plateaudejeu.cases_prises(poshypot):
        txt=("Bienvenue dans le puit , fait preuve de patiente et de ruse afin que quelqu'un prenne ta place")
        pygame_jeu_de_oie.aff_casepos(plateaudejeu,txt)
    jr.puittour=0
    return poshypot

def cases_prisonarri(jr,poshypot,plateaudejeu):
    if plateaudejeu.cases_prises(poshypot):
        if plateaudejeu.liste_case[poshypot][-1].prisontour!=None:
            txt=("Sonner l'alarme ", jr.nom , "prepare une evasion dans la prison")
            pygame_jeu_de_oie.aff_casepos(plateaudejeu,txt)
            return poshypot
        else:
            txt=("Bienvenue en prison tu devras attendre que quelqu'un t'aide a t'evader afin de sortir")
            pygame_jeu_de_oie.aff_casepos(plateaudejeu,txt)
            jr.prisontour=0
            return poshypot
    else:
        txt=("Bienvenue en prison tu devras attendre que quelqu'un t'aide a t'evader afin de sortir")
        pygame_jeu_de_oie.aff_casepos(plateaudejeu,txt)
        jr.prisontour=0
        return poshypot



def cases_labyrinthe(de,jr,poshypot,plateaudejeu):
    txt=("Tu T'aventure dans des Bien trop complexes tu retourne a la case 30")
    pygame_jeu_de_oie.aff_casepos(plateaudejeu,txt)
    return 30
def cases_mort(de,jr,poshypot,plateaudejeu):
    txt=("Tu echoue si proche du but , la vie t'offre une nouvelle chance mais tu repart au point de depart")
    pygame_jeu_de_oie.aff_casepos(plateaudejeu,txt)
    return 0




def cases_hotelfin(de,jr,poshypot,plateaudejeu):
    jr.hoteltour+=1
    txt=("Tu es a l'hotel depuis ",jr.hoteltour," Tour ; Plus Que",4-jr.hoteltour, " a l'hotel")
    if jr.hoteltour>3:
        txt="Tu sors de l'hotel (et oui toute les bonnes choses ont une fin )"
        jr.hoteltour=None
        pygame_jeu_de_oie.aff_casepos(plateaudejeu,txt)
        return poshypot
    else:
        pygame_jeu_de_oie.aff_casepos(plateaudejeu,txt)
        return jr.position

def cases_prisonfin(de,jr,poshypot,plateaudejeu):
    jr.prisontour+=1
    txt=("Tu es enfermee en prison Depuis ", jr.prisontour," tour(s)")
    pygame_jeu_de_oie.aff_casepos(plateaudejeu,txt)
    print("prison",jr.position)
    return jr.position

def cases_puitfin(de,jr,poshypot,plateaudejeu):
    jr.puittour+=1
    txt=("Tu es Bloquee Dans Le Puit Depuis ", jr.puittour," tour(s)" )
    pygame_jeu_de_oie.aff_casepos(plateaudejeu,txt)
    print("puit",jr.position)
    return jr.position

'''creation de la fonction qui va permettre de creer le plateau en uttilisant
une methode d'encapsulation via la classe plataeu.........................'''

def crea_pla(liste_jr):
    case_spe=[[6,"pont"],[19,"hotel"],[31,"puit"],[42,"labyrinthe"],[52,"prison"],[58,"mort"]]

    plateau=[[i,""] for i in range(1,64)]
    plateau=[["Depart"]] +plateau

    for i in range(5,63,9):
        plateau[i][0]="oie"
    for i in range(9,63,9):
        plateau[i][0]="oie"


    for i in range(len(case_spe)):
        plateau[case_spe[i][0]][0]=case_spe[i][1]


    for i in liste_jr:
        plateau[0].append(i)

    return plateau



'''Creation de la classe joueur pour stocker les nom et les position ,le nombre de
tour a l'hotel  et qui va verifier si il y a un gagnant.........................
................................................................................'''
class joueur():
    def __init__(self,nom,colorrg):
        self.nom=nom
        self.position=0
        self.tour=0
        self.hoteltour=None
        self.prisontour=None
        self.puittour=None
        self.color=colorrg
    def gagnant(self):
        return self.position==63




def lancement_jeu():
    liste_jr=[]
    nbr_jr=int(input("combien de joueurs vont jouer( il doit y a avoir -= 4 jr : \n"))
    while nbr_jr>4:
        nbr_jr=int(input("combien de joueurs vont jouer( il doit y a avoir -= 4 jr : \n"))

    lcolor=[["vert",(0,255,0)],["bleu",(0,0,255)],["rouge",(255,0,0)],["jaune",(255,255,0)]]
    for i in range(nbr_jr):
        nom=str(input("quel est le nom du joueur :"))
        print("liste des couleurs : ")
        for i in range (len(lcolor)):
            print(lcolor[i][0]," = ",i)

        color=int(input("Quelle couleur souhaite-il : "))

        while color > len(lcolor)-1 or color<0:
            print("liste des couleurs : ")
            for i in range (len(lcolor)):
                print(lcolor[i][0]," = ",i)

            color=int(input("Quelle couleur souhaite-il : "))

        nom=joueur(nom,lcolor[color][1])
        liste_jr.append(nom)
        lcolor.pop(color)
    plateaudejeu=plateau(liste_jr)
    print(liste_jr)
    fin=False
    tour=0
    plateaudejeu.affichage()
    pygame_jeu_de_oie.jeu_plateau(plateaudejeu,liste_jr,tour,fin)
    '''while not fin:
        tour+=1

        for i in range(len(liste_jr)):

            print("Tour",tour,"\n a " ,liste_jr[i].nom,"de jouer")
            jeu(plateaudejeu,liste_jr[i])


            fin=liste_jr[i].gagnant()'''
    return 0

def jeu(plateaudejeu,jr,tour):

    jr.tour+=1
    #print(plateaudejeu.affichage())
    print("Voici la position ",jr.nom," joueur au debut du tour  ; Case = ",jr.position)
    position=jr.position
    pygame_jeu_de_oie.lancedeveri()

    de=dee_lancement(plateaudejeu)
    print("de1", de[0] , "de2" , de[1])
    pos_hypot=position+sum(de)
    pos_hypot=premier_tour_exception(jr,de,pos_hypot)
    pos_hypot=supa63(pos_hypot)
    if plateaudejeu.est_jrsurcasespe(pos_hypot,jr)[0]==True:#ici on met une condition pour la
        #print("pl",plateaudejeu.est_jrsurcasespe(pos_hypot,jr))

        #print("posi1",pos_hypot)
        pos_hypot=plateaudejeu.jrsurcasespe(de,pos_hypot,jr)

        #print("posi",pos_hypot)
        pos_hypot=supa63(pos_hypot)

        while plateaudejeu.est_jrsurcasespe(pos_hypot,jr)==(True,1):
            pos_hypot=plateaudejeu.jrsurcasespe(de,pos_hypot,jr)
            pos_hypot=supa63(pos_hypot)

    avance(jr,pos_hypot,plateaudejeu)

    print(jr.position)
    #time.sleep(4)

def dee_lancement(plateaudejeu):

    de1=randint(1,6)
    de2=randint(1,6)
    #de1=int(input("valde1"))
    #de2=int(input("valde2"))
    pygame_jeu_de_oie.affichede(de1,de2,plateaudejeu)

    return [de1,de2]

def premier_tour_exception(jr,de,poshypot):
    if jr.tour==1:
        if sum(de)==9:
            if de==[6,3] or de==[3,6]:
                return 26
            else:
                return 53
        else:
            return poshypot
    else:
        return poshypot

def avance(jr,pos_hypot,plateaudejeu):
    pos_hypot=supa63(pos_hypot)#
    if plateaudejeu.cases_prises(pos_hypot):
        plateaudejeu.echangespos(jr,jr.position,pos_hypot)#jr.position = pos1
    else:
        plateaudejeu.deplacement(pos_hypot,jr)
    jr.position=pos_hypot

def supa63(pos_hypo):

    if pos_hypo>63:

        return 63-(pos_hypo-63)
    return pos_hypo




"""def aff_class(liste_jrtrie):
    aff_gagn(liste_jrtrie)
    #time.sleep(1)
    print("Voici le classement des Joueurs : ")
    for i in range(1,len(liste_jrtrie)):
        print("Le joueur en position ", i+1 ," est ",liste_jrtrie[i].nom,"qui est arrive a la case",liste_jrtrie[i].position )
        #time.sleep(1)"""


def classement_partie(liste_jr):
    for i in range(0,len(liste_jr)-1):
        imax=i
        for z in range(i+1,len(liste_jr)):
            if liste_jr[z].position>liste_jr[imax].position:
                imax=z
        liste_jr[i],liste_jr[imax]=liste_jr[imax],liste_jr[i]
    for t in range(len(liste_jr)):
        print(liste_jr[t].position)
    return liste_jr

liste_jr=lancement_jeu()


