import re
import spacy

nlp = spacy.load("en_core_web_sm")

text = ("Abdomen  n. 1 the belly, including the stomach, bowels, etc. 2 adj. the hinder part of an insect etc."
        "  abdominal adj. [latin]")

oracion = text.lower()
words = oracion.split("  ")
print(words[0])

oracion = re.sub("[\(\[].*?[\)\]]", " ", words[1])
oracion = re.sub("(\ n.\ )|(\ adj.\ )", " ", oracion)
print(oracion)


oracion = re.sub("\d+", "", oracion)

print(oracion)
doc = nlp(oracion)
palabras_relevantes = []

for token in doc:
        if token.pos_ in ['NOUN', 'ADJ']:
                palabras_relevantes.append(token.lemma_)
print([words[0]] + palabras_relevantes)
