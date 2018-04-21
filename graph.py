# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 11:47:02 2018

@author: raulh
"""
import networkx as g
from matplotlib import pyplot as plt

    
    #w es la matriz de pesos
def obt( w):
    l = []
    for i in range(len(w)):
        for j in range(len(w)):
            if w[i,j] != 0:
                l.append((str(i), str(j), w[i,j]))
    return l

def dibG(l, n):
    
    dg = g.DiGraph()
    dg.add_weighted_edges_from(l)
    
    pos = g.spring_layout(dg)
    g.draw_networkx_nodes(dg, pos)
    
    lb = g.get_edge_attributes(dg, 'weight')
    g.draw_networkx_edge_labels(dg,pos, edge_labels= lb)
    g.draw_networkx_labels(dg, pos, font_size=10, font_family='sans-serif')
    g.draw(dg,pos)
    
    plt.show()
    
def dibC(l,c):
    
    
    dg = g.DiGraph()
    dg.add_weighted_edges_from(l)
    
    pos = g.spring_layout(dg)
    g.draw_networkx_nodes(dg, pos)
    
    lb = g.get_edge_attributes(dg, 'weight')
    g.draw_networkx_edge_labels(dg,pos, edge_labels= lb)
    g.draw_networkx_edges(dg, pos, edgelist=c,
                       width=6, alpha=0.5, edge_color='b', style='dashed')
    g.draw_networkx_labels(dg, pos, font_size=10, font_family='sans-serif')
    g.draw(dg,pos)
    
    plt.show()