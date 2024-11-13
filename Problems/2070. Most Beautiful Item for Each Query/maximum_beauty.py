class Solution:
    def maximumBeauty(self, items, queries):
        output = []

        # sort items in reverse order by beauty
        items.sort(key=lambda x:x[1], reverse=True)
        # add a default item if none meet standards
        items.append([0,0])
        
        # loop through queries
        for query in queries:
            # loop through items
            for item in items:
                # find the moust beautiful item in the price range
                if item[0] <= query:
                    # if no item in price range deault of 0 will be added
                    output.append(item[1])
                    # break from loop once a item has been found
                    break
        return output