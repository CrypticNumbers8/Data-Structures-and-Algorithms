from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

def reversing(w):
	s2 = Stack()
	res = ''

	for i in w:
		s2.push(i)

	while s2.size()!= 0 :
		res += s2.pop()

	return res

if __name__ == '__main__':

	s1 = Stack()
	lin = [1,5,3,7,4]
	NGR(lin)
	NGL(lin)
	NSR(lin)
	NSL(lin)