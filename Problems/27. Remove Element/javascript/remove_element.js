const removeElement = (nums, val) => {
    let i = 0;
    while (i < nums.length) {
        if (nums[i] === val) {
            nums.splice(i,1);
            // remove elements starting at the index i and remove 1 element.
        } else {
            i++;
        }
    }
    return nums.length
}