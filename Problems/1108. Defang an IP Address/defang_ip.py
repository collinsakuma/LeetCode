class Solution:
    def defangIPaddr(self, address):
        return address.replace(".","[.]") # use .replace() method to replace "." with "[.]"