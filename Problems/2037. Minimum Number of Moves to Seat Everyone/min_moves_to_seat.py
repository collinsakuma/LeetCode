class Solution:
    def minMovesToSeat(self, seats, students):
        # sort both the list of seats and students in ascending order
        seats = sorted(seats)
        students = sorted(students)

        # initialize a count for the number of moves needed
        moves = 0

        # loop through range of seats
        for i in range(len(seats)):
            # match the lowest seat with the lowest student and add the number of moves required to seat the student
            moves += abs(seats[i] - students[i])

        # return the number of moves needed
        return moves