class Solution:
    def fractionAddition(self, expression):
        fractions = []
        temp_fraction = ''

        # split up the expression string into a list 
        for i in expression:
            # if there is a minus operation add the previous fraction to the list
            # start the next fraction with a negative value
            if temp_fraction and i == '-':
                fractions.append(temp_fraction)
                temp_fraction = '-'
            # if the expression is addition, add the fraction to the list, start a new one
            elif i == '+':
                fractions.append(temp_fraction)
                temp_fraction = ''
            # build the temp fraction
            else:
                temp_fraction += i
        # add the last fraction to the list
        fractions.append(temp_fraction)

        # Build the initial total
        # split the fraction by the numerator and denominator
        total = (fractions.pop(0)).split('/')
        # turn the string values to numbers
        total[0], total[1] = int(total[0]), int(total[1])

        # loop through the expressions
        for i in fractions:
            # split each expression into its numerator and denominator and turn them into numbers
            temp_frac = i.split('/')
            temp_frac[0], temp_frac[1] = int(temp_frac[0]), int(temp_frac[1])
            # if the denominators are the same only add the numerators for a new total
            if total[1] == temp_frac[1]:
                total[0] = total[0] + temp_frac[0]
            # find a common denominator and find the new total
            else:
                total[0] = (total[0] * temp_frac[1]) + (temp_frac[0] * total[1])
                total[1] = total[1] * temp_frac[1]

        # reduce the fraction, check prime factors
        while (total[0] % 2 == 0 and total[1] % 2 == 0) or (total[0] % 3 == 0 and total[1] % 3 == 0) or (total[0] % 5 == 0 and total[1] % 5 == 0) or (total[0] % 7 == 0 and total[1] % 7 == 0):
            if total[0] % 2 == 0 and total[1] % 2 == 0:
                total[0] //= 2
                total[1] //= 2
            elif total[0] % 3 == 0 and total[1] % 3 == 0:
                total[0] //= 3
                total[1] //= 3
            elif total[0] % 5 == 0 and total[1] % 5 == 0:
                total[0] //= 5
                total[1] //= 5
            elif total[0] % 7 == 0 and total[1] % 7 == 0:
                total[0] //= 7
                total[1] //= 7
        
        # rebuild the fraction and return it
        return str(total[0]) + '/' + str(total[1])