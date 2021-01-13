#Package:
import pygame
import random
from numpy import*

#Initialisation:
pygame.init()

#Fenêtre:
win=pygame.display.set_mode((400,550))
pygame.display.set_caption("MineSweeper")

#Font:
font=pygame.font.SysFont('comicsans',30,True)        
#Différent carré:
def carré(x,y,chiffre):
    if chiffre ==0:
        pygame.draw.rect(win,(255,255,255),(x*25,y*25,20,20))
    elif chiffre ==10:
        pygame.draw.rect(win,(255,0,0),(x*25,y*25,20,20))
    else:
        pygame.draw.rect(win,(255,255,255),(x*25,y*25,20,20))
        text=font.render(str(int(chiffre)),1,(0,0,255))
        win.blit(text,(x*25,y*25))
    
#Placement des bombes:
def placement(bombe,matrice,hauteur,largeur):
    for a in range(bombe):
        condition=True
        while condition:
            j=random.randint(0,largeur)
            i=random.randint(0,hauteur)
            if matrice[i][j] ==0:
                matrice[i][j]=10
                condition=False
    return matrice

#Placement des indices:
def indices(matrice,hauteur,largeur):
    for a in range(0,hauteur):
        for b in range(0,largeur):
            if matrice[a][b]==10:
                if a >0 : 
                    if matrice[a-1][b] !=10:
                        matrice[a-1][b] +=1
                if a <hauteur-1: 
                    if  matrice[a+1][b] !=10:
                        matrice[a+1][b] +=1
                if b <largeur-1: 
                    if  matrice[a][b+1] !=10:
                        matrice[a][b+1] +=1
                if b>0: 
                    if  matrice[a][b-1] !=10:
                        matrice[a][b-1] +=1
                if a>0 and b>0: 
                    if matrice[a-1][b-1] !=10:
                        matrice[a-1][b-1] +=1
                if a<hauteur-1 and b<largeur-1: 
                    if matrice[a+1][b+1] !=10:
                        matrice[a+1][b+1] +=1
                if a> 0 and b < largeur-1: 
                    if matrice[a-1][b+1] !=10:
                        matrice[a-1][b+1] +=1
                if a< hauteur-1 and b>0: 
                    if matrice[a+1][b-1] !=10:
                        matrice[a+1][b-1] +=1
    return matrice

#Matrice:
class matrice(object):
    def __init__(self,hauteur,largeur,bombe):
        self.hauteur=hauteur
        self.largeur=largeur
        self.bombe=bombe
        a=zeros((hauteur,largeur))
        b= placement(self.bombe,a,self.hauteur,self.largeur)
        self.matrice=indices(b,self.hauteur,self.largeur)
    def dessin(self,win):
        #Grille
        for x in range(0,self.largeur):
            for y in range(0,self.hauteur):
                pygame.draw.rect(win,(0,255,0),(x*25,y*25,20,20))
                
    def dessin_jeu(self,win,position):
        #Jeu
        for x in range(0,self.largeur):
            for y in range(0,self.hauteur):
                if x*25 < position[0] < (x*25)+20:
                    if y*25 < position[1] < (y*25)+20:
                        chiffre=self.matrice[y][x]
                        carré(x,y,chiffre)
        
test=matrice(22,16,40)
test.dessin(win)






#Main Loop:
condition=True
while condition:

    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            condition=False
                
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            test.dessin_jeu(win,pos)
            
    
    pygame.display.update()


#Fermeture du jeu
pygame.quit()
