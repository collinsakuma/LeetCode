class Solution:
    def numberToWords(self, num):
        if num == 0: return 'Zero'

        # create a dict of the possible permutations
        num_dict = {
            1000000000: 'Billion', 1000000: 'Million', 1000: 'Thousand', 100: 'Hundred',
            90: 'Ninety', 80: 'Eighty', 70: 'Seventy', 60: 'Sixty', 50: 'Fifty', 40: 'Forty', 30: 'Thirty', 20: 'Twenty',
            19: 'Nineteen', 18: 'Eighteen', 17: 'Seventeen', 16: 'Sixteen', 15: 'Fifteen', 14: 'Fourteen', 13: 'Thirteen', 12: 'Twelve', 11: 'Eleven',
            10: 'Ten', 9: 'Nine', 8: 'Eight', 7: 'Seven', 6: 'Six', 5: 'Five', 4: 'Four', 3: 'Three', 2: 'Two', 1: 'One'
        }

        ans = ''

        # loop through key value pairs of the dict
        for key, value in num_dict.items():
            # if num is greater than key value 
            if num // key > 0:
                # set x equal to the num divide by key to get its smallest whole number form
                x = num // key
                # if the key is greater than 100 then there are more tripples that need to be broken down
                if key >= 100:
                    # recursively break down x 
                    ans += self.numberTowords(x) + ' '
                # add the English equivalent to the key
                ans += value + ' '
                # after then English word equivalent has been added reduce num by key
                num = num % key
        
        return ans.strip()