class Solution:
    def isLongPressedName(self, name, typed):
        index_name = 0 # keep track of index of name
        index_typed = 0 # keep track of index of typed

        while index_name <= len(name) and index_typed < len(typed): # while the two pointers ( index_name and index_typed ) are in range continue loop
            # if the current value of index_name is still in range of len(name) 
            # and if the value of typed at index_typed is equal to the value of name at index_name
            # meaning both name and typed are tracking eachother with the same letters in the name
            if index_name < len(name) and typed[index_typed] == name[index_name]:
                # increment both indexes
                index_typed += 1
                index_name += 1
            # if previous if statement not fulfilled, check if value at typed[index_typed] is equal to name[index_name - 1] ( minus 1 to check previous index letter )
            # if this this resolves true that means that typed at index_typed is a long pressed key stroke of name[index_name - 1]
            elif typed[index_typed] == name[index_name - 1] and index_name != 0:
                index_typed += 1 # only increment index_typed by 1 to check if it is a continuation of a long press or to check if next value in typed equals the curr index_typed letter
            else: # if neither resolve true then typed is not a long pressed version of name, return False
                return False
        
        return index_name == len(name) and index_typed == len(typed)