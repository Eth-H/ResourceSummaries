//Challenge
//Return a filtered version of the passed array such that any array nested in arr containing elem is removed

function filteredArray(arr, elem) {
    let newArr = arr;
    let elemDetected = false;
    // change code below this line
    for (let i=0; i < arr.length; i++) {
        elemDetected = false;
        for (let j=0; j < arr[i].length; j++) {
            if(arr[i][j] == elem){
                console.log(arr[i][j]);
                elemDetected = true;

            }
        }
        if (elemDetected==true){
            newArr.splice(i, 1)
        }
    }
    // change code above this line
    return newArr;
}

let x = filteredArray([[3, 2, 3], [1, 6, 3], [3, 13, 26], [19, 3, 9]], 3)
console.log("Finished arr:");
console.log(x);