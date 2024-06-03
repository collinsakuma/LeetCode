class Solution:
    def appendCharacters(self, s, t):
        # set two pointers
        index_s, index_t = 0, 0

        # while both strings havnt been fully traversed
        while index_s <= len(s) and index_t <= len(t):
            # if s and t are the same character increment pointers in both strings
            if s[index_s] == t[index_t]:
                index_s += 1
                index_t += 1
            # if s not in t move s pointer
            else:
                index_s += 1
        
        # return the length of t not in s that needs to be added to s
        return len(t) - index_t