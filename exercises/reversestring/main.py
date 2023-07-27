# --- Directions
# Given a string, return a new string with the reversed
# order of characters
# --- Examples
#   reverse('apple') === 'leppa'
#   reverse('hello') === 'olleh'
#   reverse('Greetings!') === '!sgniteerG'

def reverse(original_str):
    # reverse_str = original_str[::-1]
    reverse_str = ''
    for i in original_str:
        reverse_str = i + reverse_str
    return reverse_str

