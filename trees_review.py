class Node(object):
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

node15 = Node(15)
node0 = Node(0)
node35 = Node(35)
node20 = Node(20, node15,node0)
node40 = Node(40,None,node35)
node19 = Node(19, node20, node40)




def find_value(anode, avalue):
	print "\n ADDING LAYER TO STACK FRAME"
	if anode.data == avalue:
		return True
	if anode.left == None and anode.right == None:
		print "this node %d has no children" % (anode.data)
		return

	found_it_left = False
	found_it_right = False

	print "here is parent %d, and we are look at children" % (anode.data)
	if anode.left != None:
		found_it_left = find_value(anode.left, avalue)
	if anode.right != None:
		found_it_right = find_value(anode.right, avalue)

	if found_it_left == True or found_it_right == True:
		return True

	return False


print find_value(node19, 35)
print node19.data





