var map = {};
var result = ''
var array = [111, 3, 4, 45 , 67, 34]

array.forEach(element => {
    const digitArray = Array.from(String(element));
    digitArray.forEach(digit => {
        if (map[digit]) {
            map[digit] += String(digit);
        }else{
            map[digit] = String(digit);
        }
    })
});

for(var i = 9; i > -1; i--){
    if(map[i]) result += map[i];
}

console.log(result)


//output 76544433111