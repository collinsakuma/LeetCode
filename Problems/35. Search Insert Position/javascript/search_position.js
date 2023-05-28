const searchInsert = (nums, target) => {
    if (nums.includes(target)) {
        // if nums array has target in it. return the index of the target
        return nums.indexOf(target);
    } else {
        // if target is not in nums array push the number into the array
        nums.push(target);
        // sort the array with the target number added
        nums.sort((a,b) => a-b);
        // return the index of the target in the newly sorted array
        return nums.indexOf(target);
    }
}