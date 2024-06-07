class Solution:
    def replaceWords(self, dictionary, sentence):
        # sort the root words by length
        dictionary = sorted(dictionary, key=len)
        # split the sentence string into a list of words
        sentence = sentence.split(' ')

        # loop through root words
        for root in dictionary:
            # loop through word in the sentence keeping track of their position using enumerate()
            for idx, word in enumerate(sentence):
                # if the first part of the word is the root
                if word[:len(root)] == root:
                    # replace that word in the list with the root word
                    sentence[idx] = root
        # join back the list into a string and return it
        return ' '.join(sentence)