function maximumToys(s1, s2) {
    const sorted1 = s1.split("").sort()
    const sorted2 = s2.split("").sort()
    let i = 0
    while (i < sorted1.length && i < sorted2.length) {
        if (sorted1[i] !== sorted2[i]) {

            // check which value is alphabetically lower
            if (sorted1[i] < sorted2[i]) {
                sorted1.splice(i, 1)
            } else {
                sorted2.splice(i, 1)
            }

        } else {
            i += 1
        }
    }
    return sorted1
}


// testings
const testStrings = [['zazhello', 'llot'], ['1', '2']]
for (i in testStrings) {
    const result = maximumToys(...testStrings[i])
    console.log(result)
}
