class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount):
        if purchaseAmount < 5:
            return 100
        elif purchaseAmount <= 10:
            return 90
        elif purchaseAmount == 100:
            return 0
        
        else:
            str_amount = str(purchaseAmount)
            if int(str_amount[1]) < 5:
                str_amount = int(str_amount[0]) * 10
            else:
                str_amount = (int(str_amount[0]) + 1) * 10

        return 100 - str_amount