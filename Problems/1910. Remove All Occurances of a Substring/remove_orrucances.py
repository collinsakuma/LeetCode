class Solution:
    def removeOccurances(self, s, part):
        n = len(part)
        # while substring part exist in s continue to loop
        while part in s:
            # loop throught range of length s
            for i in range(len(s)):
                # when substring is found remove it from s
                if s[i:i+n] == part:
                    # set new s removing substring
                    s = s[:i] + s[i+n:]
                    break

        return s