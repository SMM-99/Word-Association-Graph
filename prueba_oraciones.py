import re
import spacy

nlp = spacy.load("en_core_web_sm")

linea = ("Hateful  adj. (often foll. By to) disgusting or hateful.")

linea = linea.lower()
linea_sep = linea.split("  ")  # La primera palabra está separada por dos espacios
palabra_1 = linea_sep[0]  # Primera palabra

if len(linea_sep) > 1:

        # Procesamiento línea
        linea_pro = re.sub("[\(\[].*?[\)\]]", " ", linea_sep[1])
        linea_pro = re.sub("(\ n.\ )|(\ adj.\ )|(\ v. \ )", " ", linea_pro)
        linea_pro = re.sub("\d+", "", linea_pro)

        doc = nlp(linea_pro)
        palabras_relevantes = []

        for token in doc:
                print(token.lemma_, token.pos_)
                if token.pos_ in ['ADJ']:
                    palabras_relevantes.append(token.lemma_)

        token_palabra_1 = nlp(palabra_1)[0]
        print(token_palabra_1.lemma_, token_palabra_1.pos_)
        if token_palabra_1.pos_ == 'ADJ':
                palabras_relevantes.append(token_palabra_1.lemma_)

        print(palabras_relevantes)