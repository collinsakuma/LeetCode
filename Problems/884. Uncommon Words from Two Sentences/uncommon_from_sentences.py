from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1, s2):
        # split the strings into list 
        s1 = s1.split(' ')
        s2 = s2.split(' ')

        # create a dict using the Counter function and sort the items in asscending order
        counter1 = Counter(s1)
        counter1 = sorted(counter1.items(), key = lambda x:x[1])
        counter2 = Counter(s2)
        counter2 = sorted(counter2.items(), key = lambda x:x[1])
        output = []

        # loop through each list of tuples tracking word and count in each
        # if the count is more than one break out of the loop 
        # if the word is not in the other string add it to the list of uncommon words
        for word, count in counter1:
            if count > 1:
                break
            elif word not in s2:
                output.append(word)
        
        for word, count in counter2:
            if count > 1:
                break
            elif word not in s1:
                output.append(word)
        
        return output # return list of uncommon words