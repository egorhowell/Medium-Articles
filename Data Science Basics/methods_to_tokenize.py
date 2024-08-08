#!/usr/bin/env python

# 4 easy ways to tokenize your data


# ------- python method ---------
string = "Hello, I'm Egor. What's your name?"
string.split()

# ------ NLTK -------------
import nltk

# download the language models
nltk.download()

# use tokenizer
from nltk.tokenize import word_tokenize

word_tokenize(string)

# ---------- spaCy ----------

# download spacy model
get_ipython().system("python -m spacy download en_core_web_sm")

# tokenize
import spacy

model = spacy.load("en_core_web_sm")
doc = model(string)
tokens = []
for token in doc:
    tokens.append(token.text)

tokens

# -------- gensim ------------

from gensim.utils import tokenize

list(tokenize(string))
