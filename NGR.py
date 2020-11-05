arr = [1,5,3,7,4]
n = len(arr)

stack1 = []

NGR = []
NSL = []

for i in range(n-1, -1, -1):

	if i == n-1:
		NGR.append(-1)

	elif(arr[i]<stack1[-1] and len(stack1)>0):
		NGR.append(stack1[-1])

	elif (arr[i]>=stack1[-1] and len(stack1)>0):
		while (len(stack1)>0 and arr[i]>=stack1[-1]):
			stack1.pop()
		if len(stack1) == 0:
			NGR.append(-1)
		else:
			NGR.append(stack1[-1])


	stack1.append(arr[i])

print(NGR[::-1])
print(stack1)

NGL = []
stack2 = []

for i in range(0, n, 1):

	if i == 0:
		NGL.append(-1)

	elif(arr[i]<stack2[-1] and len(stack2)>0):
		NGL.append(stack2[-1])

	elif (arr[i]>=stack2[-1] and len(stack2)>0):
		while (len(stack2)>0 and arr[i]>=stack2[-1]):
			stack2.pop()
		if len(stack2) == 0:
			NGL.append(-1)
		else:
			NGL.append(stack2[-1])


	stack2.append(arr[i])

print(NGL)
print(stack2)

NSL = []
stack3 = []

for i in range(0, n, 1):

	if i == 0:
		NSL.append(-1)

	elif(arr[i]>stack3[-1] and len(stack3)>0):
		NSL.append(stack3[-1])

	elif (arr[i]<=stack3[-1] and len(stack3)>0):
		while (len(stack3)>0 and arr[i]<=stack3[-1]):
			stack3.pop()
		if len(stack3) == 0:
			NSL.append(-1)
		else:
			NSL.append(stack3[-1])


	stack3.append(arr[i])

print(NSL)
print(stack3)

NSR = []
stack4 = []

for i in range(n-1, -1, -1):

	if i == n-1:
		NSR.append(-1)

	elif(arr[i]>stack4[-1] and len(stack4)>0):
		NSR.append(stack4[-1])

	elif (arr[i]<=stack4[-1] and len(stack4)>0):
		while (len(stack4)>0 and arr[i]<=stack4[-1]):
			stack4.pop()
		if len(stack4) == 0:
			NSR.append(-1)
		else:
			NSR.append(stack4[-1])

	#print(NSR)
	stack4.append(arr[i])

print(NSR[::-1])
print(stack4)

