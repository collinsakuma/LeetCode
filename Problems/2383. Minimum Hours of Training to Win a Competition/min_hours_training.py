class Solution:
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        training_hours = 0 # number of hours training needed to win

        # Solve for training hours needed for only energy first
        if initialEnergy <- sum(energy): # if you start with less energy needed to win all matches
            # train for the difference between the sum of energy and the energy you start with, plus 1 because you need STRICTLY GREATER energy
            training_hours += sum(energy) - initialEnergy + 1

        # Solve for training hours needed for expereince
        for exp in experience:
            # if you experience is less than the amount of the opponent
            if initialExperience <= exp:
                # find the amount of experince you need to defeat current opponent
                needed = exp - initialExperience + 1
                # add the needed hours of training to defeat current opponent
                training_hours += needed
                # increment initialExperience by needed, plus 1 ( STRICTLY GREATER )
                initialExperience += needed + 1
            else: # you have the experince needed to defeat the current opponent and no training is needed
                initialExperience += exp # exp gained from defeated the current oponent
        
        return training_hours