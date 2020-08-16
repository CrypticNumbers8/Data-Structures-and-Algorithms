class Node:
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None


	def insert_at_begin(self, data):
		node = Node(data, self.head)
		self.head = node

	def print(self):
		if self.head is None:
			print("LL is empty")
			return

		itr = self.head
		llstr = " "
		while itr:
			llstr += str(itr.data) + '--->'
			itr = itr.next
		print(llstr)

	def insert_at_end(self,data):
		node = Node(data, None)
		if self.head is None:
			self.head = Node(data, None)
			return

		i1 = self.head
		while i1.next:
			i1 = i1.next

		i1.next = node

	def insert_values_list(self, data_list):
			self.head = None
			for i in data_list:
				self.insert_at_end(i)

	def get_length(self):
		i2 = self.head
		count = 0
		while i2:
			count += 1
			i2 = i2.next
		return count

	def remove_at(self, index):
		if index<0 or index>self.get_length():
			raise Exception("invaldi bro")

		if index==0:
			self.head = self.head.next

		count1 = 0
		i3 = self.head
		while i3:
			count1 += 1
			i3 = i3.next
			if count1 == index - 1:
				i3.next = i3.next.next
				break

	def insert_after(self, data, index):
		if index<0 or index>self.get_length():
			raise Exception("Offo")

		if index == 0:
			self.insert_at_begin(data)
			return

		count2 = 0
		i4 = self.head
		while i4:
			if count2 == index-1:
				node = Node(data, i4.next)
				i4.next = node
				break

			count2 += 1
			i4 = i4.next

	def insert_after_value(self, data_after, data_to_insert):
		count3 = 0
		i5 = self.head
		while i5:
			if i5.data == data_after:
				node = Node(data_to_insert, i5.next)
				i5.next = node
				return

			i5 = i5.next
			count3+= 1
		return

	def remove_by_value(self, data):
		if self.head is None:
			return
		if self.head.data == data:
			self.head = self.head.next

		i6= self.head
		while i6.next:
			if i6.next.data == data:
				i6.next = i6.next.next
				return
			i6 = i6.next
		return



if __name__ == '__main__':
	ll1 = LinkedList()
	
	ll1.insert_at_begin(5)
	ll1.insert_at_begin(12)
	ll1.insert_at_begin(33)		
	ll1.insert_at_end(22)
	ll1.print()
	ll1.get_length()
	
	ll2 = LinkedList()
	ll2.insert_values_list(["hp","kp","sc","ppy","terr","Kno"])
	ll2.print()
	ll2.get_length()
	ll2.remove_at(4)
	ll2.print()
	ll2.insert_after("errr",2)
	ll2.print()
	ll2.insert_after("popp",4)
	ll2.print()
	ll2.insert_after_value("popp","rell")
	ll2.print()
	ll2.remove_by_value("kp")
	ll2.print()