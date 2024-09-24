class Solution:
    def longestWord(self, words):
        # sort the words
        words.sort()

        # create a set of the prefixes to check if an icrement of 1 letter is in the set
        st, res = set(), ''
        st.add('')

        # loop through the words
        for word in words:
            # check of the prefix of the word is in the set of prefixes
            if word[:-1] in st:
                # if a new longest word found set a new longest word
                if len(word) > len(res):
                    res = word
                # add the prefix to the set
                st.add(word)

        return res