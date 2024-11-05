class Solution:
    def compressedString(self, word):
        comp = '' # compressed string
        prefix = '' # current prefix 

        # loop through characters in the string
        for ch in word:
            # if no current prefix start a prefix string
            if not prefix:
                prefix += ch
            # if current characters is not the same as the current prefix characters
            # add prefix to the compressed string
            elif prefix[-1] != ch:
                # add to the compressed string, the length of the prefix and the letter of the prefix
                comp += f'{str(len(prefix))}{prefix[0]}'
            else:
                # max length of prefix is 9 if prefix reaches 9 characters add it to the compressed string
                if len(prefix) == 9:
                    comp += f'{str(len(prefix))}{prefix[0]}'
                    # start a new prefix
                    prefix = ch
                else:
                    # add character to prefix
                    prefix += ch
        
        # if prefix after loop add the last prefix to the comp
        if prefix:
            comp += f'{str(len(prefix))}{prefix[0]}'

        return comp

