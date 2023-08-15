class Solution:
    def countStudents(self, students, sandwiches):
        while sandwiches: # while there are sandwiches in sandwiches continue loop
            if sandwiches[0] in students: # if the first sandwich matches any student in student
                students.remove(sandwiches[0]) # remove a student with the same sandwich type ( number )
                sandwiches.pop(0) # remove the first sandwich in sandwiches
            else: # if there are no more students who will take the first sandwich break from the loop
                break 
        return len(sandwiches) # return the number of students left in line 