#Power of two choices

import random
# n = 10**(7)
import matplotlib.pyplot as plt

n = 100000
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
	rand_server_1 = "server_"+str(random.randint(1,n))
	rand_server_2 = "server_"+str(random.randint(1,n))

	if dict2[rand_server_1] <= dict2[rand_server_2]:
		dict2[rand_server_1] += 1
	else:
		dict2[rand_server_2] += 1


final_list = []
for key in dict2:
	final_list.append(dict2[key])

#print(final_list)


plt.hist(final_list, bins = [0,1,2,3,4,5,6,7], histtype = "bar", color = "green", rwidth= 0.7)
plt.xlabel("Load")
plt.ylabel("No_of_servers")
plt.title('(b) smarter assignment histogram')

plt.show()
#print(servers)
#print(requests)