
# Reverse the elements of a singly linked list

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def reverse(self):
		prev = None
		current = self.head
		while current is not None:
			next = current.next
			current.next = prev
			prev = current
			current = next
		self.head = prev

	def push(self,new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def printList(self):
		temp = self.head
		while (temp):
			print(temp.data)
			temp = temp.next

l = LinkedList()
for i in range(5,0,-1):
	l.push(i)

print(f"Given LinkedList:")
l.printList()
l.reverse()
print(f"Reversing it:")
l.printList()