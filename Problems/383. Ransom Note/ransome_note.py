class Solution:
    def canConstruct(self, ransomNote, magazine):
        for i in set(ransomNote): # create a list of unqiue letters in ransomNote string
            if magazine.count(i) < ransomNote.count(i):
            # - .count() method counts the amount of times a letter / i appears in each string
            # - if magazine has less of a particular letter than the ransomNote then it doesnt
            #   the letters necessary to reproduce the note.
                return False
        return True