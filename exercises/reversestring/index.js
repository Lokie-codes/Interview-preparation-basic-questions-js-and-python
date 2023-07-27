// --- Directions
// Given a string, return a new string with the reversed
// order of characters
// --- Examples
//   reverse('apple') === 'leppa'
//   reverse('hello') === 'olleh'
//   reverse('Greetings!') === '!sgniteerG'

function reverse(originalString) {
    let reverseString = '';
    for (let i=originalString.length; i>=0; i--) {
        reverseString += originalString.charAt(i);
    }
    return reverseString;
}

module.exports = reverse;
