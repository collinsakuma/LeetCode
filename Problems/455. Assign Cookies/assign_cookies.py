class Solution:
    def findContentChildren(self, g, s):
        # sort the array of children and the array of cookies, reverse order by size, largest sizes at the front
        g.sort(reverse = True)
        s.sort(reverse = True)

        # set variables, total for children who can get cookies, and two pointers to traverse children list and cookies list
        total, i, j = 0, 0, 0

        # start loop
        while i < len(g) and j < len(s):
            if g[i] < s[j]: # check if the cookie can be given to the child
                # if cookie can be given increment total and move pointers
                total += 1
                i += 1
                j += 1
            else: # if cookie is too small for child move to the next child and check condition
                i += 1

        return total