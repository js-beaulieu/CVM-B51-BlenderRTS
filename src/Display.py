#import bgui
#import bgui.bge_utils
import bge
import random
import os
os.chdir(bge.logic.expandPath('//')) # wtf?

class Display():
    def __init__(self,parent):
        self.parent=parent
        
    def afficheArtefact(self,j):
        for i in j:
            ass=j[i].asset
            a=j[i].auto
            if a.tourne:
                ass.applyRotation([0, 0, a.tourne], 0) # Rotate on the Z-axis by 0.1 radians (I think), on the global axis (that's what the last 0 does)
                a.tourne=0
            if a.vitesse:
                ass.applyMovement([0,a.vitesse,0.0],True)
            
    def afficheListeJoueurs(self,joueurs):
        b=bge.c.own['sys'].layout.block
        b.items=joueurs
        
    def trouveNom(self):
        nom=self.splash.inNom.text
        return nom
    
    def trouveIPServeur(self):
        ipserveur=self.splash.inIPconnecteClient.text
        return ipserveur