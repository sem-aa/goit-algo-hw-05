const arr = [1,2,3,4,5,6,7,8,9,10,11, 12, 13, 14, 15, 16]
const x = 5

const binarySearch = (arr, x) => {
    let lowIndex = 0
    let highIndex = arr.length - 1
    let mid = 0
    let count = 0

    while (lowIndex <= highIndex) {
         count++

        mid = Math.floor((lowIndex + highIndex) / 2) 
        console.log("mid index:", mid, "item:", arr[mid]);
        
        if (arr[mid] === x) {
            console.log("count", count);
            
            return arr[mid]
        }

        if (arr[mid] > x) {
            highIndex = mid - 1
        } else {
            lowIndex = mid + 1     
        }
       
    }
    return -1 


}

console.log(binarySearch(arr, 8));
 