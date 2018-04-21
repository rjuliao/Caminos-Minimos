# -*- coding: utf-8 -*-
"""

@author: amaldonadop
@author: vapaternina
@author: raulj

"""
#Librerias
import numpy as np
from matplotlib import mlab as ml
import graph as g
#vector costo que es global
#vector pred que es global
# n = número de nodos
#---------------------------------------------------
def relax(u, v, w):
    
    if costo[v] > costo[u] + w[u,v]:
        costo[v] = costo[u] + w[u,v]
        pred[v]= u

#---------------------------------------------------
def initSource(w, s):
    for v in range(len(w)):
        costo[v]=99999999
        pred[v]= -1
        
    costo[s]= 0
#---------------------------------------------------
def bellmanFord(w, s):
    initSource(w, s)
    n = len(w);
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if w[i,j] != 0:
                    relax(i,j,w)
    print(costo)
    print(pred)
    dest = ml.find(costo == max(costo))[0]
    for i in range(n-1):
        for j in range(n-1):
             if costo[j]>costo[i]+w[i,j]:
                 print('Hay ciclo negativo en el grafo');
                 sw=False
                 return sw, dest 
        
    sw = True
    return sw, dest
#---------------------------------------------------
        
#Programa principal

print("Ingrese matriz de pesos de la forma: 0 0;0 0")
p = input("Ingrese matriz de pesos w = ")
s = int(input("Ingrese el nodo fuente s = "))

p = p.split(';') #len(p) corresponde al número de nodos
n = len(p)
w = np.zeros((n,n))

for i in range(n):
    sb = p[i].split(' ')
    for j in range(len(sb)):
        w[i,j]=sb[j]

costo = np.zeros(n)
pred= np.zeros(n)
l = g.obt(w)
g.dibG(l,n)
sw, dest = bellmanFord(w,s)

print(dest)

c = []
i = ml.find(pred == s)[0]#Encontramos el nodo fuente y obtenemos su indice que es la primera pareja
c.append((str(s), str(i)))
if i == dest:
    t= False
else:
    t= True
    
while t:
    j = ml.find(pred == i)[0]
    c.append((str(i), str(j)))
    i=j
    if i == dest:
        t = False

g.dibC(l,c)
    

