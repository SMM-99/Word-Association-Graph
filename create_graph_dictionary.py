import spacy
import networkx as nx
import re


def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding="utf8") as archivo:
        contenido = archivo.read()
    return contenido


def separar_oraciones(texto):
    return [nlp(line) for line in texto.splitlines()]


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


#def procesar_linea(linea):


def obtener_palabras_relevantes(oracion):
    oracion = oracion.lower()
    oracion = re.sub("[\(\[].*?[\)\]]", "", oracion)
    doc = nlp(oracion)
    palabras_relevantes = []
    for token in doc:
        if token.pos_ in ['NOUN', 'ADJ']:
            palabras_relevantes.append(token.lemma_)
    return palabras_relevantes


if __name__ == "__main__":
    # Carga el modelo de lenguaje en inglés de spaCy
    nlp = spacy.load("en_core_web_sm")

    archivo_txt = "Oxford English Dictionary.txt"
    contenido_txt = leer_archivo(archivo_txt)
    contenido_txt_1 = contenido_txt[0:1000]
    #oraciones = separar_oraciones(contenido_txt[0:100])

    for oracion in  contenido_txt_1.splitlines():
        print(obtener_palabras_relevantes(oracion))

    #print(oraciones_txt[0:5])
