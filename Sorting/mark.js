'use strict';

function maximumToys(prices, k) {
    const sortedPrices = prices.sort((a, b) => a - b)
    let total = 0
    let toys = 0
    for (let price of prices) {
        if (total + price > k) {
            break
        }
        total += price
        toys += 1
    }
    return toys
}


// testing
const prices = [1, 12, 5, 111, 200, 1000, 10]
const k = 50
const result = maximumToys(prices, k)
console.log(result)

