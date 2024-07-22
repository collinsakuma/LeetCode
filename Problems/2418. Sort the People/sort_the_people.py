class Solution:
    def sortPeople(self, names, heights):
        # matrix to hold the [name , height] of each person
        name_height = []

        # loop through range of length names
        for i in range(len(names)):
            # add the name and height of each person to the 2D array
            name_height.append([names[i], heights[i]])

        # sort the list of names by height in reverse order
        name_height = sorted(name_height, key=lambda x:x[1], reverse=True)

        # return a list of only the names
        return [name[0] for name in name_height]