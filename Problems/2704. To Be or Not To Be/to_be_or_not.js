const expect = (val) => {
    return {
        toBe: (val2) => {
            if (val !== val2) throw Error("Not Equal"); // check if val is not equal to val2 if true throw an error
            else return true;
        },

        notToBe: (val2) => {
            if (val === val2) throw Error("Equal"); // check if val is equal to val 2 if true throw an error
            else return true;
        }
    }
}