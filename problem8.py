

'''Merge a linked list into another linked list at alternate positions

Input: 5->7->17->13->11 	12->10->2->4->6

Output: 5->12->7->10->17->2->13->4->11->6
'''

class LinkedList(object):
	def __init__(self):
		self.head = None

	class Node(object):
		def __init__(self,d):
			self.data = d
			self.next = None

	def push(self,new_data):
		new_node = self.Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def merge(self,q):
		p_curr = self.head
		q_curr = q.head

		while p_curr != None and q_curr != None:
			p_next = p_curr.next
			q_next = q_curr.next

			q_curr.next = p_next
			p_curr.next = q_curr

			p_curr = p_next
			q_curr = q_next
		q.head = q_curr

	def printList(self):
		temp = self.head
		while temp != None:
			print(str(temp.data))
			temp = temp.next
		print('')

l1 = LinkedList()
l1.push(3)
l1.push(2)
l1.push(1)
print("First LL")
l1.printList()

l2 = LinkedList()
l2.push(8)
l2.push(7)
l2.push(6)
l2.push(5)
l2.push(4)
print("Second LL")
l2.printList()

l1.merge(l2)

print("Modified First LL")
l1.printList()

print("Modified Second LL")
l2.printList()