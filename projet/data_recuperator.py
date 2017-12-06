# -*- coding: utf-8 -*-
"""
Created on Wed Dec 06 15:55:17 2017

@author: Robin
"""
import os
#important sinon ça va pas fonctionner
#a remplacer par votre propre chemin d'accès
os.chdir("C:/Users/USER/Desktop/projet_opti/projet/data")

"""
Fonction qui prend en paramètre le nom d'un fichier pour le projet d'opti.
exemple 'data1.txt'
Et retourne n : le nombre de noeuds
        matrice_ring = la matrice contenant les distances du ring
        matrice_stars = la matrice contenant les distances des stars
"""
def opti_data_convertor(data):
    n = 0;
    counter = 0;
    matrice_ring = []
    matrice_stars = []
    with open(data) as f :
        for line in f :
            if counter == 0:
                n = int(line) 
            elif counter < n + 1:
                liste = map(int,line.split())
                matrice_ring.append(liste)
            else:
                liste = map(int,line.split())
                matrice_stars.append(liste)
            counter += 1
    return n, matrice_ring, matrice_stars

if __name__=='__main__':
    n,matrice, matrice2 = opti_data_convertor("data8.txt")
    print(matrice2)