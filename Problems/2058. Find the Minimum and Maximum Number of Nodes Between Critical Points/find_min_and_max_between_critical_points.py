import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head):
        # if node list is not at least three long return default answer
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        crit_points = [] # empty list to hold position of critical points
        # set variable for previous point and current point
        prev = head
        curr = head.next
        position = 1 # keep count of position of current node

        while curr.next:
            # check if the current point is a critical point
            if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
                # if critical point add its position to the list of cirital points
                crit_points.append(position)
            
            # increment points to the next node over
            prev = curr
            curr = curr.next
            position += 1

        # if there are less than two critial points return 
        if len(crit_points) < 2:
            return [-1, -1]
        
        # set min and max distinace between crit points
        min_distance = math.inf
        max_distance = crit_points[-1] = crit_points[0]

        # loop through range of the crit points
        for i in range(1, len(crit_points)):
            # check for a new minimum distance between critical points
            min_distance = min(min_distance, crit_points[i] - crit_points[i - 1])

        return [min_distance, max_distance]