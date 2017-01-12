# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 16:00:33 2017

@author: Sana
"""

raw_data="mais j'aime trop l'iPhone 7 !!! , j'ai l'impression de voir le monde en grand "
data=", j'ai l'impression de voir le monde en grand \n @hugevans_ tqqqt, deja mon sony il est mort au bout de 2/3 ans donc bon au moins avec un iphone ca durera moins mais ca sera mieux mdr\njaime pas les nveaux emoji iPhone srx\n Putain \u00e7a marche plus les conf\u00e9rences sur iPhone\n @manonakc mdrrr ton iphone dans 1,5 ans max il est mort jveux pas t'entendre pleurer\n MARRE de l\'autocorrect de l'iPhone qui me fait passer pour une illettr\u00e9e bordel\n@macmanu33 ben oui parce que sur son iphone, elle a je ne sais combien de bugs lol"

import nltk
#import nltk.data
#nltk.download()

# tokenization (Phrase)
tokenizer = nltk.data.load('tokenizers/punkt/PY3/french.pickle')

tokens = tokenizer.tokenize(raw_data)
print(tokens) 

from nltk.tokenize import WordPunctTokenizer
# tokenization (Mots)
wtokenizer = WordPunctTokenizer()

Corpus=[]
len(tokens)
for s in range(len(tokens)):
    temp=wtokenizer.tokenize(tokens[s])
    Corpus.append(temp)
print(Corpus)

# suppression des stopwords français

from nltk.corpus import stopwords
french_stopwords = set(stopwords.words('french'))
CorpuST=[]
for s in range(len(tokens)):
    temp = [token for token in Corpus[s] if token.lower() not in french_stopwords]
    CorpuST.append(temp)

    
print(CorpuST)  


