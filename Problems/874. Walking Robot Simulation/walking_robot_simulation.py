class Solution:
    # First solution results in TLE
    def robotSim(self, commands, obstacles):
        # track the direction, the max_distance from the start, and the current location
        direction = 'n'
        max_distance = 0
        location = [0, 0]

        # loop through the commands
        while commands:
            # pop the next command from the list
            command = commands.pop(0)
            # check for direction changes, -2, or -1
            if command == -2:
                if direction == 'n': direction = 'w'
                elif direction =='e': direction = 'n'
                elif direction == 's': direction = 'e'
                else: direction = 's'
            elif command == -1:
                if direction == 'n': direction = 'e'
                elif direction == 'e': direction = 's'
                elif direction == 's': direction = 'w'
                else: direction = 'n'
            else:
                # while the command is to move loop
                while command:
                    # move in the direction
                    if direction == 'n':
                        location[1] += 1
                    elif direction == 'e':
                        location[0] += 1
                    elif direction == 's':
                        location[1] -= 1
                    else:
                        location[0] -= 1
                    # if the location moved too is an obstacle, move a step back in the direction
                    if location in obstacles:
                        if direction == 'n':
                            location[1] -= 1
                        elif direction == 'e':
                            location[0] -= 1
                        elif direction == 's':
                            location[1] += 1
                        else:
                            location[0] += 1
                        # break out the loop
                        break
                    # reduce the steps to take by 1
                    command -= 1
            # check for a new max distance
            max_distance = max(max_distance, (location[0]**2) + (location[1]**2)) 
            
        return max_distance
    
    def robotSimTwo(self, commands, obstacles):
        x, y, d = 0, 0, 0
        # directions for north, south, east west
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        max_distance = 0 # track max distance
        obstacles = set(map(tuple, obstacles)) # create a set of the obstacles

        # loop through the commands
        for command in commands:
            # if the command is to change direction set a new direction
            if command == -1:
                d = (d + 1) % 4
            elif command == -2:
                d = (d - 1) % 4
            else:
                # loop through the command distance
                for _ in range(command):
                    # set new x or y position
                    nx, ny = x + direction[d][0], y + direction[d][1]
                    if (nx, ny) in obstacles:
                        # if an obstacle is reached break from the command
                        break
                    x, y = nx, ny
                    # find the max distance
                    max_distance = max(max_distance, x**2 + y**2)
        
        return max_distance # return the max distance
