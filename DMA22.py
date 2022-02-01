import copy
import sys
import math
import pandas as pd
from collections import Counter
import numpy
import random

import time

#goto - studymachinelearning.cm/jaccard-similarity-text-similarity-metric-in-nlp/

word_list = []
char_list = []

with open('D1.txt','r') as f:
	for line in f:
		for word in line.split():
			word_list.append(word)

with open('D1.txt','r') as f1:
	for line in f1:
		for ch in line:
			#print(ch)
			char_list.append(ch)

#print(char_list)

print("Total Words:",len(word_list))
set0 = set(word_list)
print("Total Unique words:",len(set0))


pairs_2g = [word_list[i]+'@'+word_list[i+1] for i in range(len(word_list)-1)]
#print("Total 2 gram Words:",len(pairs_2g))
set1 = set(pairs_2g)
print("THIS: Total 2gram Unique words:",len(set1))

pairs_3g = [word_list[i]+'@'+word_list[i+1]+'#'+word_list[i+2] for i in range(len(word_list)-2)]
#print("Total 3 gram Words:",len(pairs_3g))
set2 = set(pairs_3g)
print("THIS: Total 3gram Unique words:",len(set2))

print("Total characters:",len(char_list))
set_char = set(char_list)
print("Total unique chars:", len(set_char))

pairs_c3g = [char_list[i]+char_list[i+1]+char_list[i+2] for i in range(len(char_list)-2)]
print("Total 3 gram chars:",len(pairs_c3g))
set3 = set(pairs_c3g)
print("THIS: Total 3gram Unique chars:",len(set3))

###########################################################

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
word_list2 = []
char_list2 = []


with open('D2.txt','r') as f2:
	for line in f2:
		for word in line.split():
			word_list2.append(word)

with open('D2.txt','r') as f3:
	for line in f3:
		for ch in line:
			#print(ch)
			char_list2.append(ch)

#print(char_list)

print("Total Words:",len(word_list2))
set02 = set(word_list2)
print("Total Unique words:",len(set02))


pairs_2g2 = [word_list2[i]+'@'+word_list2[i+1] for i in range(len(word_list2)-1)]
#print("Total 2 gram Words:",len(pairs_2g))
set12 = set(pairs_2g2)
print("THIS: Total 2gram Unique words:",len(set12))

pairs_3g2 = [word_list2[i]+'@'+word_list2[i+1]+'#'+word_list2[i+2] for i in range(len(word_list2)-2)]
#print("Total 3 gram Words:",len(pairs_3g))
set22 = set(pairs_3g2)
print("THIS: Total 3gram Unique words:",len(set22))

print("Total characters:",len(char_list2))
set_char2 = set(char_list2)
print("Total unique chars:", len(set_char2))

pairs_c3g2 = [char_list2[i]+char_list2[i+1]+char_list2[i+2] for i in range(len(char_list2)-2)]
print("Total 3 gram chars:",len(pairs_c3g2))
set32 = set(pairs_c3g2)
print("THIS: Total 3gram Unique chars:",len(set32))

# Find the intersection of words list of doc1 & doc2
intersection = set3.intersection(set32)

# Find the union of words list of doc1 & doc2
union = set3.union(set32)


J = float(len(intersection) / len(union))

print("JACCARD:", J)

#print(pairs_c3g2)

union_list= list(union)

print(len(pairs_c3g))
print(len(pairs_c3g2))

list_new1 = list(set3)
list_new2 = list(set32)

print(len(list_new1))
print(len(list_new2))
print(len(union_list))

# t = 1
# while(t!=0):
# 	t 

start_time = time.time()

vector1 = [1]*637
vector2 = []

for i in range(len(list_new1)):
	if list_new1[i] in list_new2:
		vector2.append(1)
	else:
		vector2.append(0)


m1_list = []
m2_list = []

t = 2400
while(t!=0):
	t = t - 1
	random.shuffle(vector2)

	m1 = 0
	m2 = vector2.index(1)

	m1_list.append(m1)
	m2_list.append(m2)

sum1 = 0

t = 2400
for i in range(t):
	if m1_list[i] == m2_list[i]:
		sum1 += 1


final_ans = sum1/t

print("JACCARD:", format(final_ans, ".4f"))

print("JACCARD:", format(final_ans, ".3f"))

end_time = time.time()

print("--- %s seconds ---" % (end_time - start_time))