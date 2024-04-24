import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_gml("Red Diccionario/Oxford_Dict_Graph_Adj.gml")

c = 'dumb'
for i in G.neighbors(c):
    if G.edges[(c, i)]['weight'] >= 1:
        print(i)
# H = G.subgraph()

