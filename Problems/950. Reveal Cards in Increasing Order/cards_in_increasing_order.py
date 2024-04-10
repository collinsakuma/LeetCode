from collections import deque

class Solution:
    def deckRevealIncreasing(self, deck):
        n = len(deck)
        # set an empty output list of equal length to the deck
        output = [0] * n
        # sort the deck in reverse order
        deck.sort(reverse=True)
        # set a que using deque
        queue = deque(range(n))

        for _ in range(n):
            # from the deck append the element from the front of the que
            output[queue.popleft()] = deck.pop()
            # if there are elements in the queue take the next element in the queue and move it to the end
            if queue:
                queue.append(queue.popleft())

        return output