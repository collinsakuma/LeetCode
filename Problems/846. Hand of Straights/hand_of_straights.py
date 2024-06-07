from collections import Counter

class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False
        
        counter = Counter(hand)

        sorted_keys = sorted(counter.keys())

        for key in sorted_keys:
            if counter[key] > 0:
                start_count = counter[key]
                for i in range(key, key + groupSize):
                    if counter[i] < start_count:
                        return False
                    counter[i] -= start_count

        return True