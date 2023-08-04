class Solution:
    def reversePrefix(self, word, ch):
        index = word.find(ch) # find the what index ch is at in word
        return (word[index + 1][::-1] + word[index + 1:])
        # word[index + 1][::-1] takes the prefix (letter up to and including ch) and reverses them
        # word[index + 1:] adds the remaining letters in word after index of ch in word