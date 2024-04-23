import spacy
import networkx as nx
import re
import os

# Carga el modelo de lenguaje en español de spaCy
# nlp = spacy.load("es_core_news_sm")

# Carga el modelo de lenguaje en inglés de spaCy
nlp = spacy.load("en_core_web_sm")

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding="utf8") as archivo:
        contenido = archivo.read()
    return contenido

def separar_oraciones(texto):
    doc = nlp(texto)
    oraciones = [sent.text for sent in doc.sents]
    return oraciones

def procesar_oracion(oracion):
    oracion = oracion.lower()
    oracion = re.sub(r'-', '', oracion)
    oracion = re.sub(r'[^\w\s-]', '', oracion)
    return oracion

def obtener_palabras_relevantes(oracion):
    doc = nlp(oracion)
    palabras_relevantes = []
    for token in doc:
        if token.pos_ in ['NOUN', 'ADJ']:
            palabras_relevantes.append(token.lemma_)
    return palabras_relevantes

def escribir_grafo(G, filename):
    # Escribe el grafo en formato GML
    nx.write_gml(G, filename + ".gml")
    # Escribe el grafo en formato Pajek NET
    nx.write_pajek(G, filename + ".net")

if __name__ == "__main__":
    archivo_txt = "The_Alchemist.txt"
    contenido_txt = leer_archivo(archivo_txt)
    oraciones_txt = separar_oraciones(contenido_txt)
    
    #Auxiliar sacar todos los nodos que van a aparecer
    Gaux = nx.Graph()
    for oracion in oraciones_txt:
        oracion_procesada = procesar_oracion(oracion)
        palabras_relevantes = obtener_palabras_relevantes(oracion_procesada)
        for i, word in enumerate(palabras_relevantes):
            Gaux.add_node(word)
            
    #Inicio    
    todos_los_nodos = list(Gaux.nodes())
    G = nx.Graph()
    for nodo in todos_los_nodos:
        G.add_node(nodo)
    
    total_oraciones = len(oraciones_txt)
    oraciones_procesadas = 0
    acum=0
    for oracion in oraciones_txt:
        oracion_procesada = procesar_oracion(oracion)
        palabras_relevantes = obtener_palabras_relevantes(oracion_procesada)
        for i, word in enumerate(palabras_relevantes):
            G.add_node(word)
            for other_word in palabras_relevantes[i + 1:]:
                if G.has_edge(word, other_word):
                    # Incrementar el peso del borde si ya existe
                    G[word][other_word]['weight'] += 1
                else:
                    # Agregar el borde con peso 1 si no existe
                    G.add_edge(word, other_word, weight=1)
            # Incrementar la cuenta de apariciones de la palabra
            if 'count' in G.nodes[word]:
                G.nodes[word]['count'] += 1
            else:
                G.nodes[word]['count'] = 1
        
        oraciones_procesadas += 1
        if oraciones_procesadas / total_oraciones >= 0.05:
            acum=acum+5
            # Escribir el grafo cada vez que se procesa el 5% de las oraciones
            output_filename = f"Alchemist_{int(acum)}%"
            escribir_grafo(G, output_filename)
            print(f"Grafo guardado como {output_filename}.gml y {output_filename}.net")
            oraciones_procesadas = 0
            G.clear()
    
    # Escribir el último grafo
    escribir_grafo(G, "Alchemist_final")
    print("Grafo final guardado como Alchemist_final.gml y Alchemist_final.net")
    todos_los_nodos = list(G.nodes())
    print("Todos los nodos encontrados")
    