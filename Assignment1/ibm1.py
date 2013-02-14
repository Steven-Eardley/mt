# -*- coding: utf-8 -*-
# Assignment 1 for Machine Translation
# Steven Eardley s0934142

import re
from sys import argv

if len(argv) == 3:
    to_file = argv[1]
    from_file = argv[2]
else:
    print "\nUse: ibm1.py to_language from_language\nWhere these files are an alligned corpus.\n"

# punctuation tends to be surrounded by spaces.

 #initialize t(e|f) uniformly
 #do until convergence
   #set count(e|f) to 0 for all e,f
   #set total(f) to 0 for all f
   #for all sentence pairs (e_s,f_s)
     #set total_s(e) = 0 for all e
     #for all words e in e_s
       #for all words f in f_s
         #total_s(e) += t(e|f)
     #for all words e in e_s
       #for all words f in f_s
         #count(e|f) += t(e|f) / total_s(e)
         #total(f)   += t(e|f) / total_s(e)
   #for all f
     #for all e
       #t(e|f) = count(e|f) / total(f)

# Store the alligned sentences in a dictionary: { sentence_no : ([e], [f]) }
sentences = dict()

# Store translations in a dictionary: { f : ([[e , t_ef, count_ef]], total_f) }
translations = dict()

# Store sets of words
e_words = set([])
f_words = set([])

# Remove punctuation which is surrounded by spaces, and separate into a list of words
def list_words(sentence_string):
    nonpunc_string = re.sub(' \W ', ' ', sentence_string)
    tokens = nonpunc_string.split(" ")
    
    # Get rid of the newline
    return tokens[:len(tokens)-1]

# Read sentence pairs from two alligned files.
def readpairs(to_file, from_file):
    f1 = open(to_file, 'r')
    f2 = open(from_file, 'r')
    try:
        to_sentences = f1.readlines()
        from_sentences = f2.readlines()
    finally:
        f1.close()
        f2.close()
    
    if len(to_sentences) != len(from_sentences):
        print "Mismatched document lengths!"
    
    for i in range(0, len(to_sentences)):
        # Seperate the sentence into words and store in dictionary
        to_words = list_words(to_sentences[i])
        from_words = list_words(from_sentences[i])
        sentences[i] = (to_words, from_words)
        
        # Store the unique words
        global e_words, f_words
        e_words = e_words | set(to_words)
        f_words = f_words | set(from_words)
        

def train():
    converged = False
    
    while not converged:
        intialise()
        for (e_s, f_s) in sentences.values():
            for e in e_s:
                total_e = 0
    
    return 0

def initialise():
    for (f, ([[e , t_ef, count_ef]], total_f)) in translations.items():
        translations[f] = ([[e, t_ef, 0]], 0)

def translate():
    return 0
    
readpairs(to_file, from_file)
print sentences.items()[:4]

print e_words
print f_words