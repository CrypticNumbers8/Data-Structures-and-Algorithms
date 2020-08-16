class Node:
	def __init__(self, data=None, right=None, left=None):
		self.data = data
		self.right = right
		self.left = left

class DoublyLinkedList:
	def __init__(self):
		self.head = None

	def insert_at_begin(self,data):
		node = Node(data, self.head, None)
		if self.head is None:
			self.head = node
		else:
			self.head.left = node
			self.head = node

	def insert_at_end(self, data):
		node = Node(data)
		i2 = self.head
		while i2.right:
			i2 = i2.right

		i2.right = node
		node.left = i2	

	def printF(self):
		if self.head is None:
			print("DLL is empty")
			return

		dllstr = " "
		i1 = self.head
		while i1:
			dllstr += str(i1.data) + "--->"
			i1 = i1.right
		print(dllstr)

	def printB(self):
		if self.head is None:
			print("DLL is empty")
		
		i2 = self.head
		while i2.right:
			i2=i2.right

		dllstrBack = " "
		while i2:
			dllstrBack += str(i2.data) + "--->"
			i2 = i2.left

		print(dllstrBack)

	def get_length(self):
		if self.head is None:
			return 0 

		i3 = self.head
		lent = 0
		while i3:
			lent+=1
			i3= i3.right

		return lent

	def insert_values(self, data_list):
		self.head = None
		for i in data_list:
			self.insert_at_end(i)



if __name__ == '__main__':
	ll1 = DoublyLinkedList()
	ll2 = DoublyLinkedList()

	ll1.insert_at_begin(23)
	ll1.insert_at_begin(11)
	ll1.insert_at_end(44)
	ll1.insert_at_end(133)
	ll1.printF()
	ll1.printB()
	print(ll1.get_length())

	ll2.insert_values(["buf","kfd","fff","ere","fds"])
	ll2.printF()