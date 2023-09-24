class Solution:
    def furthestDistanceFromOrigin(self, moves):
        # take the abs of the count of "R" - the count of "L"  as that will determine the direction that the blank spaces should be used for
        # add the blalk spaces to find the furthest distance away from 0 that can be achieved
        return moves.count("_") + abs(moves.count("R") - moves.count("L"))