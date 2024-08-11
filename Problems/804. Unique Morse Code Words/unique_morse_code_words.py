class Solution:
    def uniqueMorseRepresentations(self, words):
        # create a dictionary of all alphabet with morse code as the value
        morse = {
            "a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".",
            "f":"..-.", "g":"--.", "h":"....", "i":"..", "j":".---",
            "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---",
            "p":".--.", "q":"--.-", "r":".-.", "s":"...", "t":"-",
            "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--",
            "z":"--.."
        }

        coded = [] # create an empty list to hold unique codes
        for word in words: # create a loop of words
            coded_word = [] # empty list to hold morse code of each letter of word
            for i in word: # loop though the letters of word
                coded_word.append(morse[i]) # add each morse code for each letter i
            coded_word = "".join(coded_word) # join code into a string

            if coded_word not in coded: # check if string is in the list of coded words
                coded.append(coded_word) # if string is not in list append it to the list

        return len(coded) # return the len of the list of unique coded words

        ##### lines 13 - 18 can also be written: #####
        # coded = [] 
        # for word in words: 
        #     coded_word = ""  <--- set as an empty string
        #     for i in word:  
        #         coded_word += morse[i]  <----- add to the empty string don't need to join the list into a string anymore

