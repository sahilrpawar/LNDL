# -*- coding: utf-8 -*-
"""JKL (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LYFedf2XobAkLr5yfIDLXOfteT55hHnU
"""

d=input("Enter corpus =")

def  preprocess(d):
  d=d.lower()
  d="eos " + d
  d=d.replace(".","eos")
  return d
d=preprocess(d)
print("Preprocessed Data corpus =\n",d)

import nltk
nltk.download('punkt')
from nltk import word_tokenize
def generate_tokens (d):
  tokens= word_tokenize(d)
  return tokens
tokens=generate_tokens (d)
distinct_tokens = list(set (sorted (tokens)))
print("Tokens in the corpus - \n",distinct_tokens)

def generate_tokens_freq(tokens):
  dct={}
  for i in tokens:
    dct[i]=0
  for i in tokens:
    dct[i]+=1

  return dct

dct=generate_tokens_freq(tokens)
print("Frequency of each tokens ")
for i in dct.items():
  print(i[0],"\t:", i[1])

def generate_ngrams (tokens,k):
   l=[]
   i=0
   while(i<len (tokens)):
      l.append(tokens[i:i+k])
      i=i+1
   l=l[:-1]
   return l
bigram = generate_ngrams (tokens, 2)
print("N-grams generated (Here n is 2) = ")
for i in bigram:
   print(i)

def generate_ngram_freq(bigram):
  dct1={}
  for i in bigram:
    st=" ".join(i)
    dct1[st]=0
  for i in bigram:
    st=" ".join(i)
    dct1[st]+=1
    return dct1
dct1=generate_ngram_freq(bigram)
print("Frequency of n-grams ")
for i in dct1.items():
   print(i[0], ":", i[1])

def find1(s,dct1):
  try:
      return dct1[s]
  except:
      return 0
def print_probability_table(distinct_tokens, dct,dct1):
   n=len(distinct_tokens)
   l=[[]*n for i in range(n)]
   for i in range(n):
           denominator=dct[distinct_tokens[i]]
   for j in range(n):
           numerator=find1 (distinct_tokens[i]+" "+distinct_tokens[j],dct1)
           l[i].append(float("{:.3f}".format(numerator/denominator)))
   return l

print('Probability table = \n')
probability_table = print_probability_table(distinct_tokens,dct,dct1)
n = len(distinct_tokens)
print('\t',end = '')
for i in range(n):
  print(distinct_tokens[i],end='\t')
print('\n')
for i in range(n):
    print(distinct_tokens[i],end='\t')
    for j in range(n):
       print(probability_table[i][j],end='\t')
    print('\n')