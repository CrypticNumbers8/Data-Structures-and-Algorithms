#Kadane's Algorithm:
#Time Complexity: O(N)

def max_sum_subarray_not_all_negative(l1):

	current_sum = 0
	max_sum = 0

	for i in range(len(l1)):
		current_sum += l1[i]

		if current_sum>max_sum:
			max_sum = current_sum

		if current_sum<0:
			current_sum = 0

	return max_sum

def max_sum_subarray_all_negative(l2):

	current_sum = 0
	max_sum = l2[0]

	for i in range(len(l2)):
		current_sum += l2[i]

		if current_sum>max_sum:
			max_sum = current_sum

		if current_sum<0:
			current_sum = 0

	return max_sum



if __name__ == '__main__':

	a = [1,2,-4,5,12,-13,7,8]
	b = [-3,-1,-2,-7,-5,-4,-13,-2]

	w = max_sum_subarray_not_all_negative(a)
	x = max_sum_subarray_all_negative(b)

	print(w)
	print(x)