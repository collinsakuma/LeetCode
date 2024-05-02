class Solution:
    def reversePrefix(self, word, ch):
        index = word.find(ch) # find the what index ch is at in word
        return (word[index + 1][::-1] + word[index + 1:])
        # word[index + 1][::-1] takes the prefix (letter up to and including ch) and reverses them
        # word[index + 1:] adds the remaining letters in word after index of ch in word
    
    def reversePrefixTwo(self, word, ch):
        # loop through using enumerate() to track index as well
        for index, letter in enumerate(word):
            # if we encounter the target index
            if letter == ch:
                # reverse the prefix and add the rest of the word to the string
                return word[index::-1] + word[index + 1:]
        return word