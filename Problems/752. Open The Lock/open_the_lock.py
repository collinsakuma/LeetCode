from collections import deque   

class Solution:
    def openLock(self, deadends, target) -> int:
        deadend_set = set(deadends)
        queue = deque()
        queue.append(('0000', 0))
        visited = set('0000')

        while queue:
            curr_str, curr_steps = queue.popleft()

            if curr_str == target:
                return curr_steps

            if curr_str in deadend_set:
                continue

            for i in range(4):
                digit = int(curr_str[i])
                for dir in [1, -1]:
                    new_digit = (digit + dir) % 10

                    new_str = curr_str[:i] + str(new_digit) + curr_str[i+1:]

                    if new_str not in visited:
                        visited.add(new_str)
                        queue.append((new_str, curr_steps + 1))

        return -1