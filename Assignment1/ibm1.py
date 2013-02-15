# -*- coding: utf-8 -*-
# Assignment 1 for Machine Translation
# Steven Eardley s0934142

import re
from sys import argv, exit

if len(argv) == 3:
    to_file = argv[1]
    from_file = argv[2]
else:
    print "\nUse: ibm1.py to_language from_language\nWhere these files are an alligned corpus.\n"
    exit()

# Store the alligned sentences in a dictionary: { sentence_no : ([e], [f]) }
sentences = dict()

# Store translations in a dictionary: { f : ([[e , t_ef, count_ef]], total_f) }
translations = dict()

# Store the accumulated sentence probabilities
total_s = dict()

# Store sets of words
e_words = set([])
f_words = set([])

# Remove punctuation which is surrounded by spaces, and separate into a list of words
def list_words(sentence_string):
    nonpunc_string = re.sub(' \W ', ' ', sentence_string)
    
    # Get rid of the newline and full stop if present
    remove_newline = re.sub('\.*\n', '', nonpunc_string)
    return remove_newline.split(" ")

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

# Run IBM Model 1 until convergence. I tried to match the pseudo code here.
def ibm1():
    init_uniformly()
    
    converged = False
    n_iterations = 0
    while not converged:
        converged = True
        for (e_s, f_s) in sentences.values():
            
            
            # Compute normalisation
            for e in e_s:
                total_s[e] = 0.0
                for f in f_s:
                    
                    # Sum the t_ef probabilities when e is found in the translations
                    (E_list, total_f) = translations[f]
                    for [E, t_ef, count_ef] in E_list:
                        if E == e:
                            total_s[e] = total_s[e] + t_ef
            
            # Collect counts
            for e in e_s:
                for f in f_s:
                    (E_list, total_f)  = translations[f]
                    new_E_list = []
                    if total_s[e] != 0.0:
                        for [E, t_ef, count_ef] in E_list:
                            if E == e:
                                count_ef += t_ef / total_s[e]
                            new_E_list.append([E, t_ef, count_ef])
                        translations[f] = (new_E_list, total_f + t_ef / total_s[e])
            
            # Estimate probabilities
            for F in translations.keys():
                (E_list, total_f)  = translations[F]
                new_E_list = []
                for [E, t_ef, count_ef] in E_list:
                    new_t_ef = t_ef
                    try:
                        new_t_ef = count_ef / total_f
                        new_E_list.append([E, new_t_ef, 0.0])
                    except ZeroDivisionError:
                        new_E_list.append([E, new_t_ef, 0.0])
                    if int(new_t_ef * 1000) != int(t_ef * 1000):
                        converged = False
                translations[F] = (new_E_list, 0.0)
                    
        if n_iterations > 10:
           converged = True
           print "\nToo many iterations - forced convergence\n"
        n_iterations += 1
        
# Initialise with each foreign word with its available translations, with uniform probability.
def init_uniformly():
    global e_words, f_words
    uniform_prob = 1 / float(len(e_words))
    for f in f_words:
        translations[f] = ( [[ e, uniform_prob, 0.0] for e in e_words] , 0.0)
    
    for e in e_words:
        total_s[e] = 0.0

# Running the program
readpairs(to_file, from_file)
init_uniformly()
ibm1()
print sentences.items()[2]

# Print the foreign word and an ordered list of likely English translations
for f in translations.keys():
    print "\n" + f 
    sorted_list = sorted(translations[f][0], key=lambda x: x[1], reverse = True)
    for [a, b, c] in sorted_list:
        print "{0}\t\t{1}".format(a, b)