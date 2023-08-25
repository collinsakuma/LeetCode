class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        return "".join(word1) == "".join(word2)
    


# second solution Using Generators and Yield Statements #

# - Generators are a kind of iterators which do not store all the values in memory, 
#   they simply generate the values on the fly (thus you cannot go back and perform 
#   operations on previously seen indices).

    def arrayStringsAreEqualTwo(self, word1, word2):
        for wordOne, wordTwo in zip(self.generate(word1), self.generate(word2)):
            if wordOne != wordTwo:
                return False
        return True
    
    def generate(self, wordlist):
        for word in wordlist:
            for char in word:
                yield char
        yield None # yield None signifies that the given input has been exhausted
    

