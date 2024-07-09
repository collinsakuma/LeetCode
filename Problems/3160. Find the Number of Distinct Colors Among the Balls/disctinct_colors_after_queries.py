class Solution:
    def queryResults(self, limit, queries):
        # initalize an empty list to hold the amount of distinct colors after
        # each query
        distinct_colors = []
        # initalize two empty dictionaries to hold each ball and its colors 
        # and a dict to keep track of the colors of all the balls 
        balls = {}
        colors = {}

        for ball, color in queries:
            # if the ball in the queries is changing color for the first time
            if ball not in balls:
                # create an item in balls with the ball number as the key and its color as the value
                balls[ball] = color
                # if the color is not currently not on any balls
                if colors[color] not in colors:
                    # add the color to the colors dict and start a count of balls
                    # with that color
                    colors[color] = 1
                else:
                    # if that color is present in the balls, increment the count of balls with
                    # that color
                    colors[color] += 1
            # if the ball in the query already has a color and is being reassigned
            else:
                # if the color being switched to is already present increment the count
                # of balls with that color in the colors dict
                if color in colors:
                    colors[color] += 1
                # if no ball is painted this color create a new color item in colors
                else:
                    colors[color] = 1
                
                # because the ball is being assigned a new color the previous color that 
                # the ball was count needs to be reduced in the colors dict
                colors[balls[ball]] -= 1

                # if the previous color that the balls was count is now 0 remove that color
                # from the colors dict
                if colors[balls[ball]] == 0:
                    colors.pop(balls[ball])

                # set the new color of the ball
                balls[ball] = color

            # after the query add the count of colors that are present among all the balls
            distinct_colors.append(len(colors))
        
        return distinct_colors