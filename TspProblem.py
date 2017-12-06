# -*- coding: utf-8 -*-
"""
Created on Wed Dec 06 12:07:10 2017

@author: Robin
"""
import copy
"""
Cette classe définit le probleme du transporteur de commerce.
Elle contient aussi l'algorithme de la recherche locale pour donner une solution acceptable au probleme.
"""
class TspProblem:
    #On entre en paramètres le nombre de villes
    #et une matrice de distances.
    def __init__(self, nb_villes, dist_matrice):
        self.nb_villes = nb_villes
        self.dist_matrice = dist_matrice
        self.tour = []#On initialise le tour de départ allant de la ville 1 ... ville n
        for e in range(nb_villes):
            self.tour.append(e+1)
    
    def current_dist(self):
        distance = 0
        for e in range(len(self.tour)-1):
            distance += self.dist_matrice[self.tour[e]-1][self.tour[e+1]-1]
        distance += self.dist_matrice[self.tour[0]-1][self.tour[len(self.tour)-1]-1]
        return distance
    #Cette classe crée 8 solutions
    def create_sol(self):
        sol_list = []
        index = 0
        s = copy.copy(self.tour)
        counter = 0
        while counter < 8:
            if index < len(self.tour)-1:
                temp = s[index]
                s[index] = s[index+1]
                s[index+1] = temp
                sol_list.append(copy.copy(s))
            else:
                index = 0
                temp = s[index]
                s[index] = s[index+1]
                s[index+1] = temp
                sol_list.append(copy.copy(s)) 
            index += 1
            counter += 1
        return sol_list
    
    def local_search(self):
        while True:
            s = self.tour
            dist1 = self.current_dist()
            s1 = []
            voisinage = self.create_sol()
            min_dist = self.current_dist()
            for e in voisinage:
                self.tour = e
                if self.current_dist() < min_dist:
                    min_dist = self.current_dist()
                    s1 = e
            if(min_dist >= dist1):
                self.tour = s
                break
            else:
                self.tour = s1 
        return self.tour
            
dist_matrice = [[0,2,1,3,4],
                [2,0,1,2,3],
                [1,1,0,1,2],
                [3,2,1,0,1],
                [4,3,2,1,0]]
        
tsp = TspProblem(5,dist_matrice)
print(tsp.tour)
print(tsp.current_dist())
tsp.local_search()
print(tsp.tour)
print(tsp.current_dist())
