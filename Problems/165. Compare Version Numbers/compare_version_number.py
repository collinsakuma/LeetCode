class Solution:
    def compareVersion(self, version1, version2):
        # split the two version strings into list split between the number versions
        levels_1 = version1.split('.')
        levels_2 = version2.split('.')
        # set length to the longer of the two strings
        length = max(len(levels_1), len(levels_2))

        # loop though range of length
        for i in range(length):
            # set a version value if no version exist set version value to 0
            v1 = int(levels_1[i]) if i < len(levels_1) else 0
            v2 = int(levels_2[i]) if i < len(levels_2) else 0

            # check if version are equal of less than
            if v1 < v2:
                return -1
            if v1 > v2:
                return 1
        
        return 0