class Solution:
    def countSeniors(self, details):
        count = 0

        # loop through each persons info
        for i in details:
            # extrat the persons age from the information index 11 & 12
            # compare if it is greater than string 60
            # string can be used because strings have value assocated to them 
            if i[11:13] > "60":
                # if passanger is over 60 increase thec ount of senior citizens
                count += 1

        return count