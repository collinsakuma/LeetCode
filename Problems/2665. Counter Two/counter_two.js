var createCounter = function(init) {
    let currentCount = init; // set initial value of currentCount to value of initial

    const increment = () => {
        return ++currentCount; // increment currentCount by 1 a return the new value
    }

    const reset = () => {
        return (currentCount = init); // reset the currentCount value to the init value
    }

    const decrement = () => {
        return --currentCount; // decrease the value of currentCount by 1 and return the value
    }

    return { increment, decrement, reset} // return the 3 different functions availiable in the createCounter object
};