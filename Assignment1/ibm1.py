# -*- coding: utf-8 -*-
# Assignment 1 for Machine Translation
# Steven Eardley s0934142

from sys import argv

if len(argv) == 3:
    to_file = argv[1]
    from_file = argv[2]
else:
    print "\nUse: ibm1.py to_language from_language\nWhere these files are an alligned corpus.\n"

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

def readpairs(to_file, from_file):
        f1 = open(to_file, 'r')
        f2 = open(from_file, 'r')
    try:
        to_sentences = f1.readlines()
        from_sentences = f2.readlines()
    finally:
        f1.close()
        f2.close()
        
    
    return prob

def train():
    return 0

def translate():
    return 0