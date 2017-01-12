#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 00:50:18 2017

@author: Sana
"""
"""
print("hi")
from pattern.fr import conjugate
from pattern.fr import INFINITIVE
print conjugate('suis', INFINITIVE)
from pattern.fr import sentiment
print sentiment('Un livre horrible!')
print "---------------------"
from pattern.fr import parse, split
s = parse("Le chat noir s'était assis sur le tapis.")
for sentence in s.split():
    print sentence
print "---------------------" """
from pattern.fr import parse
from pattern.fr import pprint 
#pprint(parse('je suis venue.', relations=True, lemmata=True))
ob=parse("j'aime le nouveau iPhone.", relations=True, lemmata=True)
pprint(ob)
l=parse("j'aime trop l'iPhone.", relations=True, lemmata=True).split()
print(l)
#chunk=l[0].split("/")
print "---------------------" 
#print(chunk)
