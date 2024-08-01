class Solution:
    def minHeightShelves(self, books, shelfWidth):
        n = len(books)

        # create a dp the length of how many books there are
        dp = [0] * (n + 1)

        # loop through the books usinger enumerate() to track the current index of the loop
        for i, (width, height) in enumerate(books, 1):
            # add the height of the previous book to the total height at curr index
            dp[i] = dp[i - 1] + height

            # loop through the previous books in reverse order
            for j in range(i - 1, 0, -1):
                # add the width of the book to the current books width
                width += books[j - 1][0]
                # if the combined width is greater than the max shelf width break the loop
                # as the width of multiple books cannot exceed the shelf width
                if width > shelfWidth:
                    break
                
                # if the previous book can fit on the same shelf set the height to the max height
                # of eighter of the two books
                height = max(height, books[j - 1][1])

                dp[i] = min(dp[i], dp[j - i] + height)

        return dp[n]