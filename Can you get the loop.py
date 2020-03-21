"""
You are given a node that is the beginning of a linked list. This list always contains a tail and a loop.

Your objective is to determine the length of the loop.
"""

def loop_size(node):
	nodeCount = {}
	currentNode = node
	count = 1

	while currentNode not in nodeCount:
		nodeCount[currentNode] = count

		currentNode = currentNode.next

		count += 1

	return count - nodeCount[currentNode]