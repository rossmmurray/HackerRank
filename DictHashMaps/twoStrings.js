function twoStrings(s1, s2) {
    const a1 = s1.split("")
    const a2 = s2.split("")
    for (let i in a1) {
        if (a2.includes(a1[i])) {
            return 'YES'
        }
    }
    return 'NO'
}


// testings
const testStrings = [['hello', 'llot'], ['1', '2']]
for (i in testStrings) {
    const result = twoStrings(...testStrings[i])
    console.log(result)
}
