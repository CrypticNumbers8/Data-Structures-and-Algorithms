import random

n = 10^6

sample = ['A']*5200000 + ['B']*4800000

result_count = []

for i in range(100):

	temp_list = []
	count_A_is_majority = 0
	random.shuffle(sample)

	for i in range(20):
		temp_list.append(sample[i])
	
	if temp_list.count("A")>temp_list.count("B"):
		count_A_is_majority+=1

	result_count.append(count_A_is_majority)

print(result_count)

#probability that A is majority = # of "1"/ 100

prob_A_is_majority = 