class Solution:
    def hasCycle(self, head):
        # create a set to keep track of the nodes that have been visisted and their values
        visited_nodes = set()
        current_node = head # set to the current node

        while current_node: # while there are still nodes in the linked list continue to loop
            # if the current node is in visisted_nodes than a cycle has been found return true
            if current_node in visited_nodes:
                return True
            # add node to the visisted_nodes
            visited_nodes.add(current_node)
            # set current_node to the next node in the linked list
            current_node = current_node.next
        # once all nodes have been visited and none where visited twice return False, a cycle has not been found
        return False