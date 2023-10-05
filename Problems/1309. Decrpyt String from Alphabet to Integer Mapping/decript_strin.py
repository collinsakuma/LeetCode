class Solution:
    def freqAlphabets(self, s: str) -> str:
        output = "" # set an empty string for the output
        i = 0 # set start of while loop to 0
        while i < len(s): # countinue to loop while i is less than the length of string s
            # check if i is at the 3rd to last index of the loop and if the last index of the string is a "#"
            if i + 2 < len(s) and s[i + 2] == "#":
                # if so the the indexs -2, -3 represent a letter indexed greater than 10
                c = chr(int(s[i:i + 2]) + ord("a") - 1)
                i += 3 # increase the i count by 3, three indicies have been accounted for xxx, double number letter and the # indicating that its a double letter
            else:
                # else add the character represented by index i
                c = chr(int(s[i]) + ord("a") - 1)
                i += 1 # increase i count by 1 as only one index has been traversed
            output += c # add c string to the output string
        return output