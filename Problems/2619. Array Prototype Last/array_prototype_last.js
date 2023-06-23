Array.prototype.last = function() {
    if (this.length === 0) { // check if arrays length is greater tahn 0
        return -1; // if arrays length is  0 return -1
    } else {
        return this[this.length - 1]; // return the last element in the array this at index length - 1 will give you the last element
    }
};