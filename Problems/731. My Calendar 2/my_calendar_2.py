from sortedcontainers import SortedList

class MyCalendarTwo:

    def __init__(self):
        # create a calendar
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        # add the dates to the calendar sorted list
        self.calendar.add((start, 1))
        self.calendar.add((end, -1))

        total = 0 # set a total

        # loop through the calendar
        for i, j in self.calendar:
            # add to the total
            total += j

            if total == 3: # if the total is 3 remove the calendar
                self.calendar.remove((start, 1))
                self.calendar.remove((end, -1))
                return False

        return True