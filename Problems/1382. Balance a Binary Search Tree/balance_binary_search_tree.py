class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root):
    
        node_list = [root.val] # list to store the node values

        # traverese the binary tree and put the values into the node list
        def traverse_nodes(node):
            if node.left: # if node has a left branch
                # add the left branch value to the list
                node_list.append(node.left.val)
                # recursively traverse the branch to add its nodes
                traverse_nodes(node.left)
            if node.right: # if node has a right branch
                # add the right branch value to the list
                node_list.append(node.right.val)
                # recursively traverse the branch to add its nodes
                traverse_nodes(node.right)

        # create the node list
        traverse_nodes(root)

        # sort the list of node values in ascending order
        node_list.sort()

        # created the balanced node tree
        def sorted_array_to_bst(nums):
            # if no remaining numbers to traverse return none
            if not nums:
                return None
            # find the mid index in the list of numbers
            mid = len(nums) // 2
            # initalize a node tree with the middle number as the root
            root = TreeNode(nums[mid])
            # for the right side of the tree traverse the first half of the sorted 
            # list of nodes and add them into the tree recursively
            root.left = sorted_array_to_bst(nums[:mid])
            # do the same for the ladder half of the sorted list
            root.right = sorted_array_to_bst(nums[mid + 1:])
            # return the balanced node tree
            return root
        
        return sorted_array_to_bst(node_list)