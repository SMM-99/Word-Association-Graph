import spacy
import networkx as nx
import re


def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding="utf8") as archivo:
        contenido = archivo.read()
    return contenido


def separar_oraciones(texto):
    return [nlp(line) for line in texto.splitlines()]


def obtener_palabras_relevantes(linea):
    linea = linea.lower()
    linea_sep = linea.split("  ")  # La primera palabra está separada por dos espacios
    palabra_1 = linea_sep[0]  # Primera palabra

    if len(linea_sep) == 1:
        return []

    # Procesamiento línea
    linea_pro = re.sub("[\(\[].*?[\)\]]", " ", linea_sep[1])
    linea_pro = re.sub("(\ n.\ )|(\ adj.\ )|(\ v. \ )", " ", linea_pro)
    linea_pro = re.sub("\d+", "", linea_pro)

    doc = nlp(linea_pro)
    palabras_relevantes = []

    for token in doc:
        if token.pos_ in ['NOUN', 'ADJ']:
            palabras_relevantes.append(token.lemma_)

    return [palabra_1] + palabras_relevantes


def escribir_grafo(G, filename):
    # Escribe el grafo en formato GML
    nx.write_gml(G, filename + ".gml")
    # Escribe el grafo en formato Pajek NET
    nx.write_pajek(G, filename + ".net")

if __name__ == "__main__":
    # Carga el modelo de lenguaje en inglés de spaCy
    nlp = spacy.load("en_core_web_sm")

    archivo_txt = "Oxford English Dictionary.txt"
    contenido_txt = leer_archivo(archivo_txt)

    G = nx.Graph()

    for linea in contenido_txt.splitlines():
        palabras_relevantes = obtener_palabras_relevantes(linea)
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

    escribir_grafo(G, "Oxford_Dict_Graph")

