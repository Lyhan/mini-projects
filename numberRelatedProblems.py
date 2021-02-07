"""
# Integer to Roman number system conversion up to 1999
numbers = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
"""


def romanNumberConversionSolution1(value):
    lookupTable = [
        ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
        ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
        ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
        ['M']
    ]
    number_list = list(str(value))
    result = ''
    for i in range(0, len(number_list)):
        number = int(number_list.pop())
        if number != 0:
            character = lookupTable[i][int(number) - 1]
            result = character + result

    return result


def romanNumberConversionSolution2(value):
    romanSymbols = [
        ['I', 'V'],
        ['X', 'L'],
        ['C', 'D'],
        ['M']
    ]
    number_list = list(str(value))
    result = ''
    for i in range(0, len(number_list)):
        number = int(number_list.pop())
        # Numeric system rules up to 1999
        if 0 < number <= 3:
            current = romanSymbols[i][0] * number
        elif number == 4:
            current = romanSymbols[i][0] + romanSymbols[i][1]
        elif number == 5:
            current = romanSymbols[i][1]
        elif 5 < number <= 8:
            current = romanSymbols[i][1] + romanSymbols[i][0] * number
        elif number == 9:
            current = romanSymbols[i][0] + romanSymbols[i + 1][0]
        result = current + result

    return result


""" 
A factorial is a function that multiplies a number by every number below it.
Example 5!= 5*4*3*2*1=120.
"""
def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number - 1)

"""
The next number is found by adding up the two numbers before it
Example: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
"""
def fibonacci(number):
    current = prev = 0
    result = list()
    while current < number:
        result.append(current)
        if current < 1:
            current += 1
        else:
            prev, current = current, current + prev
    return result
