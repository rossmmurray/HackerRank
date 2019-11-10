function maximumToys(s1, s2) {
    var map = {}
    for (let letter of s1) {
        map[letter] = 1;
    }
    
    for (let letter of s2) {
        if (map[letter]) {
            return 'YES'
        }
    }
    return 'NO'
}


// testings
const testStrings = [['hello', 'llot'], ['1', '2']]
for (i in testStrings) {
    const result = maximumToys(...testStrings[i])
    console.log(result)
}
