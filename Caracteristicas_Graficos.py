# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 23:05:56 2024

@author: j_g_r
"""
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Carga tus archivos de red para cada tiempo (ajusta las rutas de archivo según corresponda)
network_files = ["Alquimista_{}%.gml".format(t) for t in range(5, 96, 5)]
network_files.append("Alquimista_final.gml")

# Inicializa listas para almacenar los datos de evolución
time_points = []
average_degrees = []
densities = []
clustering_coefficients = []
giant_component_sizes = []
diameters = []

# Itera sobre cada punto de tiempo
for t, file_path in zip(range(5, 101, 5), network_files):
    # Carga la red desde el archivo
    G = nx.read_gml(file_path)
    
    # Calcula y almacena las características
    time_points.append(t)
    average_degrees.append(nx.average_degree_connectivity(G))
    densities.append(nx.density(G))
    clustering_coefficients.append(nx.average_clustering(G))
    
    # Calcula el tamaño de la componente gigante
    giant_component = max(nx.connected_components(G), key=len)
    giant_component_sizes.append(len(giant_component) / len(G))
    
    # Calcula el diámetro solo para la componente gigante
    diameter = nx.diameter(G.subgraph(giant_component))
    diameters.append(diameter)

# Crea un DataFrame para usar con Plotly
df = pd.DataFrame({
    "Tiempo": time_points,
    "Grado Medio": average_degrees,
    "Densidad": densities,
    "Coeficiente de Clustering": clustering_coefficients,
    "Tamaño Componente Gigante": giant_component_sizes,
    "Diámetro": diameters
})

# Grafica la evolución del grado medio con Plotly
# fig1 = px.line(df, x="Tiempo", y="Grado Medio", title="Evolución del Grado Medio")
# fig1.show()

# Grafica la evolución de la densidad con Plotly
fig2 = px.line(df, x="Tiempo", y="Densidad", title="Evolución de la Densidad")
fig2.show()



# # Calcula la distribución de grado para una sola red (por ejemplo, en t=5)
# degree_sequence = [d for n, d in G.degree()]
# degree_counts = nx.degree_histogram(G)

# # Grafica la distribución de grado
# plt.figure(figsize=(10, 6))
# plt.bar(range(len(degree_counts)), degree_counts)
# plt.xlabel("Grado")
# plt.ylabel("Número de Nodos")
# plt.title("Distribución de Grado en t=5")
# plt.grid()
# plt.show()
