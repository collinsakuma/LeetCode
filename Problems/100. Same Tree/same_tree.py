class Solution:
    def isSameTree(self, p, q):
        # if both trees are empty then both trees are matching
        if not p and not q:
            return True

        # if p and q are non empty and have the same root value recursilvey call isSameTree() function on left and right subtrees
        # if all conditions are found to be the same return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
        return False