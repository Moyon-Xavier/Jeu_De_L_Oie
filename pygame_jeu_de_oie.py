# Créé par moyon, le 03/05/2021 en Python 3.7
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 15:18:29 2021

@author: moyon
"""
import projet_jeu_de_loie_beta_part1
import pygame,sys,time
from pygame.locals import*
from random import randint
import time


pygame.init()




class Ecran:
    def __init__(self,couleur,case,casenumber):#proportion pour donner quel taille l'ecran va prendre par rapport a l'ordi
        self.couleur=couleur
        self.fen_axex=900#longueur ecran
        self.fen_axey=900#hauteur ecran
        self.case=case#on stocke les nom des cases
        self.casenumber=casenumber#on stocke les numeros associes aux cases
        self.pointdedepartx=0#point de placement de base pour la premiere case du plateau en x et y
        self.pointdedeparty=self.fen_axey/9
        self.la=self.fen_axex//18#largeur des cases du plateau
        self.lon=self.fen_axey//15#longueur des cases du plateau
        self.taillejr=min(self.fen_axex,self.fen_axey)//45#taille des images des joueurs

        self.fen=pygame.display.set_mode((self.fen_axex,self.fen_axey))

def affichetourjr(plateaudejeu,jr,tour):
    ec=plateaudejeu.ecran_accueil
    pygame.draw.rect(plateaudejeu.ecran_accueil.fen,jr.color,(ec.fen_axex/1.8,ec.fen_axey/45,ec.fen_axex/22.5,ec.fen_axey/22.5))#on affiche la couleur du joueur a cote du texte pour mieux voir qui est le joueur sur le plateau
    font= pygame.font.Font(None ,int(min(ec.fen_axex,ec.fen_axey)/45))

    '''txt = "TOUR", tour , "C'EST A ",jr.nom,"DE JOUER"# on ecrit le texte txt sur le plateau pygame
    image =font.render(str(txt), 1 , (255,255,255) )

    plateaudejeu.ecran_accueil.fen.blit(image,(40,20))
    pygame.display.update()'''

    txt = "TOUR", tour , "C'EST A ",jr.nom,"DE JOUER"
    image =font.render(str(txt), 1 , (255,255,255) )

    plateaudejeu.ecran_accueil.fen.blit(image,(ec.fen_axex/22.5,ec.fen_axey/45))
    pygame.display.update()

def aff_casepos(plateaudejeu,txt):
    ec=plateaudejeu.ecran_accueil
    font= pygame.font.Font(None ,int(min(ec.fen_axex,ec.fen_axey)/45))
    image=font.render(str(txt), 1 , (255,255,255) )
    plateaudejeu.ecran_accueil.fen.blit(image,(ec.fen_axex/22.5,ec.fen_axey/11.25))
    pygame.display.update()


def affichage_temps_pause(plateaudejeu):
    ec=plateaudejeu.ecran_accueil
    coord=(ec.fen_axex/1.2413793,ec.fen_axey/3,ec.fen_axex/8.0357,ec.fen_axey/22.5)
    font= pygame.font.Font(None ,int(min(ec.fen_axex,ec.fen_axey)/45))

    image =font.render("Joueur Suivant", 1 , (255,255,255) )
    plateaudejeu.ecran_accueil.fen.blit(image,(coord[0],coord[1]+(coord[3]/2)))


    pygame.display.update()
    pygame.draw.rect(plateaudejeu.ecran_accueil.fen,(0,0,0),coord,5)
    pygame.display.update()
    boutsui=False
    while boutsui==False:
        for event in pygame.event.get():
                        #print(pygame.event.get)
                        if event.type==QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type==KEYDOWN:
                            print(event.key)
                        elif event.type == MOUSEBUTTONDOWN :
                            print("Event pos",event.pos)
                            if event.pos[0]>coord[0] and event.pos[0]<coord[0]+coord[2]:
                                print("x ok")
                                if event.pos[1]<coord[1]+coord[3] and event.pos[1]>coord[1]:
                                    print("Y ok")

                                    #print("reussi ev",event.pos)
                                    return True



def affichagepl(obj,liste_jr):#obj vient de la case ecran
##    pygame.display.update()
    #obj.affichage()
    obj.fen.fill(obj.couleur)
    #pygame.display.update()
    font= pygame.font.Font(None ,20)
    listecasecolor=[]
    for i in range(len(liste_jr)):
        listecasecolor.append(liste_jr[i].position)

    for i in range(len(obj.case)):
            #if i%2==0:
                for z in range(len(obj.case[i])):
                    if obj.case[i][z]!="":

                        #print("z=",z,"i=",i)
                        #print("lo=",z*obj.lon,"la=",z*obj.la)
                        #print("pointcase x",obj.pointdedepartx+(z*(obj.lon+0.1*obj.lon)),"pointcase y ",obj.pointdedeparty+(i*(obj.la+0.4*obj.la)))
                        pygame.draw.rect(obj.fen,(0,0,0),(obj.pointdedepartx+(z*(obj.lon+obj.fen_axex/9000*obj.lon)),obj.pointdedeparty+(i*(obj.la+obj.fen_axex/2250*obj.la)),obj.la,obj.lon),5)
                        image =font.render( obj.case[i][z], 1 , (255,255,255) )
                        obj.fen.blit(image,(obj.pointdedepartx+(z*(obj.lon+obj.fen_axex/9000*obj.lon)),obj.pointdedeparty+(i*(obj.la+obj.fen_axex/2250*obj.la))))
                        #print("obj",obj.casenumber[i][z] , "lst",listecasecolor)
                        #time.sleep(0.1)
                        #if obj.casenumber[i][z] in listecasecolor:
                         #   print("bien,1")
                        for d in range(len(listecasecolor)):
                                #print("lst",int(listecasecolor[d]),"obj",int(obj.casenumber[i][z]))
                               # print(int(obj.casenumber[i][z])==int(listecasecolor[d]))
                                if int(obj.casenumber[i][z])==int(listecasecolor[d]):
                                    #print("bien")
                                    positionjroncase=obj.pointdedepartx+z*(obj.lon+obj.fen_axex/9000*obj.lon)+(d+1)*(obj.fen_axex/90)
                                    while positionjroncase+obj.taillejr>obj.pointdedepartx+(z*(obj.lon+obj.fen_axex/9000*obj.lon))+obj.lon:

                                        obj.taillejr=obj.taillejr//2
                                        #print("o")
                                    pygame.draw.rect(obj.fen,liste_jr[d].color,(obj.pointdedepartx+z*(obj.lon+obj.fen_axex/9000*obj.lon)+(d+1)*obj.fen_axex/90,obj.pointdedeparty+(d+1)*obj.fen_axey/90+(i*(obj.la+obj.fen_axex/2250*obj.la)),obj.taillejr,obj.taillejr))
                                    pygame.display.update()
                        #time.sleep(0.1)
                        pygame.draw.rect(obj.fen,(0,0,0),(obj.fen_axex/1.24137931,obj.fen_axey/6.9767,obj.fen_axex/22.5,obj.fen_axey/22.5),5)
                        pygame.draw.rect(obj.fen,(0,0,0),(obj.fen_axex/1.125,obj.fen_axey/6.9767,obj.fen_axex/22.5,obj.fen_axey/22.5),5)

                        pygame.display.flip()
                        pygame.display.update()










def lancedeveri():
    delan=False
    while delan==False:
        for event in pygame.event.get():
                        #print(pygame.event.get)
                        if event.type==QUIT:
                            pygame.quit()
                            sys.exit()
                        #elif event.type==KEYDOWN:
                         #   print(event.key)
                        elif event.type == MOUSEBUTTONDOWN :
                            #print("Event pos",event.pos)
                            if event.pos[0]>600 and event.pos[0]<900:
                                if event.pos[1]>124 and event.pos[1]<172:

                                    #print("reussi ev",event.pos)
                                    return True
    #print("OO")
def affichede(de1,de2,plateaudejeu):
    font= pygame.font.Font(None ,20)
    image1 =font.render( str(de1), 1 , (255,255,255) )
    plateaudejeu.ecran_accueil.fen.blit(image1,(735,135))
    image2 =font.render( str(de2), 1 , (255,255,255) )
    plateaudejeu.ecran_accueil.fen.blit(image2,(810,135))
    font= pygame.font.Font(None ,30)
    image3 =font.render( str(de1+de2), 1 , (255,255,255) )


    plateaudejeu.ecran_accueil.fen.blit(image3,(772,200))
    pygame.display.flip()
    pygame.display.update()
##def avance(jr,poshypot):
##    if poshypot<jr.position
##    for i in range()
def affga(ecran,listejr):
    font= pygame.font.Font(None ,20)
    pos=(300,100)
    ecran.fen.fill(ecran.couleur)
    txt=str("LE GRAND GAGNANT EST "+ str(listejr[0].nom))
    texte =font.render( txt.upper(), 1 , (255,255,255) )
    ecran.fen.blit(texte,pos)
    pygame.display.flip()
    pygame.display.update()
    for i in range(1,len(listejr)):
        txt=str("LE Joueur en position " + str(i) +" est "+(str(listejr[i].nom)).upper() +" et est arriver en position : " + str(listejr[i].position) )
        texte =font.render( txt, 1 , (255,255,255) )
        ecran.fen.blit(texte,(pos[0],pos[1]+(40*i)))
        pygame.display.flip()
        pygame.display.update()
    pygame.draw.rect(ecran.fen,(0,0,0),(300,pos[1]+(i+5)*40,300,40),2)
    pygame.display.update()
    texte =font.render( "__FIN__", 1 , (255,255,255) )
    ecran.fen.blit(texte,(450,pos[1]+(i+5.5)*40))
    pygame.display.flip()
    pygame.display.update()
    over=False
    while not over:
        for event in pygame.event.get():
                        if event.type==QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == MOUSEBUTTONDOWN :
                            #print("Event pos",event.pos)
                            if event.pos[0]>300 and event.pos[0]<600:
                                if event.pos[1]>pos[1]+(i+5)*40 and event.pos[1]<pos[1]+(i+6)*40:

                                    #print("reussi ev",event.pos)
                                    return True

def jeu_plateau(plateaudejeu,liste_jr,tour,fin):

    #plateaudejeu.affichage()
    affichagepl(plateaudejeu.ecran_accueil,liste_jr)
    while not fin:

        for event in pygame.event.get():
                    #print(pygame.event.get)
                    if event.type==QUIT:
                        pygame.quit()
                        sys.exit()

        tour+=1


        for i in range(len(liste_jr)):
            if not fin:
                #plateaudejeu.affichage()
                affichagepl(plateaudejeu.ecran_accueil,liste_jr)
                affichetourjr(plateaudejeu,liste_jr[i],tour)
                projet_jeu_de_loie_beta_part1.jeu(plateaudejeu,liste_jr[i],tour)


                fin=liste_jr[i].gagnant()
            if not fin:
                affichage_temps_pause(plateaudejeu)

    liste_jr=projet_jeu_de_loie_beta_part1.classement_partie(liste_jr)
    affga(plateaudejeu.ecran_accueil,liste_jr)

    pygame.quit()
    sys.exit()


'''lass Boutton:
    def __init__(self,pos,color,taille,text=''):
        self.fen_axex=0
        self.fen_axey=0
##        self.x=pos[0]
##        self.y=pos[1]
        self.couleur=color
        self.largeur=taille[1]
        self.longueur=taille[0]
        self.texte=text
    def dessin(self,ecr):
        pygame.draw.rect(ecr.fen,self.couleur,(self.fen_axex,self.fen_axey,self.longueur,self.largeur))'''





#Partie lancement :
'''m=[["Depart","1","2","3","4","5","6","7","8","9"],
  ["","28","29","30","31","32","33","34","35","10"],
  ["","27","48","49","50","51","52","53","36","11"],
  ["","26","47","60","61","62","63","54","37","12"],
  ["","25","46","59","58","57","56","55","38","13"],
  ["","24","45","44","43","42","41","40","39","14"],
  ["","23","22","21","20","19","18","17","16","15"]]
p1=0.92
#lancement=Boutton(1/2,(255,0,0),(400,200),"Bjr")
ecran_accueil=Ecran(p1,(139,69,19),0,m)#lancement contient les bouttons
affichage(ecran_accueil)'''

#y=0 vers le haut
#x = 0 vers la gauche

