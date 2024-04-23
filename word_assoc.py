import networkx as nx
import matplotlib.pyplot as plt

def dibuja_distr_grado(G):
    degree_counts = nx.degree_histogram(G)

    # Grafica la distribución de grado
    # plt.figure(figsize=(10, 6))
    plt.bar(range(len(degree_counts)), degree_counts)
    plt.xlabel("Grado")
    plt.ylabel("Número de Nodos")
    plt.title("Distribución de Grado")
    plt.grid()
    # plt.show()

# https://github.com/sujithps/Dictionary/tree/master

if __name__ == "__main__":
    # Lectura de grafos
    G_EAT = nx.read_pajek("Redes/EATnew_undir.net")
    G_Alc = nx.read_gml("Redes/Alchemist_final.gml")

    # Palabras en cada grafo
    words_Alc = set(G_Alc.nodes)
    words_EAT = set([x.lower() for x in list(G_EAT.nodes)])

    # Palabras que aparecen en cada grafo
    words = words_EAT.intersection(words_Alc)

    # Palabras que aparecen en el Alquimista pero no en el grafo EAT
    words_dis = words_Alc.difference(words)
    #print(words_dis)
    #print(len(words_Alc))
    #print(len(words_EAT))
    #print(len(words))
    #print(list(words)[0:20])
    words_up = [x.upper() for x in list(words)]

    # Subgrafos con las palabras en ambos grafos
    H_EAT = G_EAT.subgraph(words_up)
    H_Alc = G_Alc.subgraph(words)

    nx.write_gml(H_EAT,  "EAT_subgraph_Alc.gml")
    # Dibuja distribución de grafos
    plt.figure(1)
    plt.subplot(121)
    dibuja_distr_grado(H_Alc)
    plt.subplot(122)
    dibuja_distr_grado(H_EAT)
    plt.show()

    # Dibuja subgrafos
    plt.figure(2)
    plt.subplot(121)
    nx.draw(H_EAT)
    plt.subplot(122)
    nx.draw(H_Alc)
    plt.show()

