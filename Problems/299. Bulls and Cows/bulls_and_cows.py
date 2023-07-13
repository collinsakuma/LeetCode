class Solution:
    def getHint(self, secret, guess):
        bull, cow = 0, 0 # set variables to keep track of instances of bull and cow hints

        for i in range(0, len(secret)): # loop though range of secret
            if secret[i] == guess[i]: # compare number at same index of secret and guess and if they are the same number increase bull count by one and reduce cow count by 1
                bull += 1
                cow -= 1
        
        for i in set(secret): # loop though a set of unique numbers from secret
            cow += min(secret.count(i), guess.count(i)) # find the min() occurance of i in both secret and guess and add the minimum to cow
        
        return f'{bull}A{cow}B' # use string interpolation to return bull and cow occurances in the guess