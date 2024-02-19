import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
#nltk.download("wordnet")
#nltk.download('averaged_perceptron_tagger')
from nltk.corpus import wordnet
import time

porter = PorterStemmer()
lemm = WordNetLemmatizer()
sentence = "If you are a software engineer, deep learning is the most important technology for you to learn now. Why? Because deep learning is powering all of the latest advances in AI and machine learning. If you want to stay ahead of the curve, deep learning is essential. But don’t worry – it’s not too late to start. In this blog post, we will provide an introduction to deep learning and outline some resources for learning more. So what are you waiting for? Start learning today!"
tokens = sentence.split()
print([(x + (12-len(x))*" ") for x in tokens])
startporter = time.time()
print([(porter.stem(x) + (12-len(porter.stem(x)))*" ") for x in tokens])
endporter = time.time()
startlemm = time.time()
print([(lemm.lemmatize(x) + (12-len(lemm.lemmatize(x)))*" ") for x in tokens])
endlemm = time.time()

print(endporter-startporter)
print(endlemm-startlemm)

print([(lemm.lemmatize(x, pos=wordnet.VERB) + (12-len(lemm.lemmatize(x, pos=wordnet.VERB)))*" ") for x in tokens])
#basic word     Describes an action or state of being
print([(lemm.lemmatize(x, pos=wordnet.ADJ) + (12-len(lemm.lemmatize(x, pos=wordnet.ADJ)))*" ") for x in tokens])
#non graduate   Describes or modifies a noun or pronoun
print([(lemm.lemmatize(x, pos=wordnet.NOUN) + (12-len(lemm.lemmatize(x, pos=wordnet.NOUN)))*" ") for x in tokens])
#non plural     Refers to a person, place, thing, or idea
print([(lemm.lemmatize(x, pos=wordnet.ADV) + (12-len(lemm.lemmatize(x, pos=wordnet.ADV)))*" ") for x in tokens])
#               Describes or modifies a verb, adjective, or other adverb

def get_wordnet_pos(treebank_tag):
  if treebank_tag.startswith('J'):
    return wordnet.ADJ
  elif treebank_tag.startswith('V'):
    return wordnet.VERB
  elif treebank_tag.startswith('N'):
    return wordnet.NOUN
  elif treebank_tag.startswith('R'):
    return wordnet.ADV
  else:
    return wordnet.NOUN

tagged = nltk.pos_tag(tokens)
converted = []
for word, tag in tagged:
    lem = lemm.lemmatize(word, pos=get_wordnet_pos(tag))
    converted.append(lem)
print([(x + (12-len(x))*" ") for x in converted])