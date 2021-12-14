#Power of two choices
from collections import Counter
import random
# n = 10**(7)
import matplotlib.pyplot as plt
import numpy

n = 10000
servers = []
requests = []
for i in range(1,n+1):
	temp1 = "server_" + str(i)
	temp2 = "request_" +str(i)
	servers.append(temp1)
	requests.append(temp2)

dict2 = {}
for i in servers:
	dict2[i] = 0

for i in requests:
	rand_server = "server_"+str(random.randint(1,n))
	if rand_server in servers:
		dict2[rand_server]+=1

final_list = []
for key in dict2:
	final_list.append(dict2[key])

#print(final_list)


plt.hist(final_list, bins = [0,1,2,3,4,5,6,7], histtype = "bar", color = "red", rwidth= 0.7)
plt.xlabel("Load")
plt.ylabel("No_of_servers")
plt.title('(a) random assignment histogram')


plt.show()
#print(dict2)

#print(servers)
#print(requests)