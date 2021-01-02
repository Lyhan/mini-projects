"""
Braille is a writing system used to read by touch instead of by sight. Each character is composed of 6 dots in a 2x3 grid, where each dot can either be a bump or be flat (no bump). You plan to translate the signs around the space station to Braille so that the minions under Commander Lambda's command can feel the bumps on the signs and ""read"" the text with their touch. The special printer which can print the bumps onto the signs expects the dots in the following order:
1 4
2 5
3 6

So given the plain text word ""code"", you get the Braille dots:

11 10 11 10
00 01 01 01
00 10 00 00

where 1 represents a bump and 0 represents no bump.  Put together, ""code"" becomes the output string ""100100101010100110100010"".

Write a function solution(plaintext) that takes a string parameter and returns a string of 1's and 0's representing the bumps and absence of bumps in the input string. Your function should be able to encode the 26 lowercase letters, handle capital letters by adding a Braille capitalization mark before that character, and use a blank character (000000) for spaces. All signs on the space station are less than fifty characters long and use only letters and spaces.

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution("code")
Output:
    100100101010100110100010

Input:
solution.solution("Braille")
Output:
    000001110000111010100000010100111000111000100010

Input:
solution.solution("The quick brown fox jumps over the lazy dog")
Output:
    000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110
"""

CHARACTERS = {
    "a": "100000",
    "b": "101000",
    "c": "110000",
    "d": "110100",
    "e": "100100",
    "f": "111000",
    "g": "111100",
    "h": "101100",
    "i": "011000",
    "j": "011100",
    "k": "100010",
    "l": "101010",
    "m": "110010",
    "n": "110110",
    "o": "100110",
    "p": "111010",
    "q": "111110",
    "r": "101110",
    "s": "011010",
    "t": "011110",
    "u": "100011",
    "v": "101011",
    "w": "011101",
    "x": "110011",
    "y": "110111",
    "z": "100111",
    " ": "000000",
    "uppercase": "000001"
}

ORDER = [1, 4, 2, 5, 3, 6]


def convert(char):
    return CHARACTERS[char]


def order(brailleCode):
    value = [0, 0, 0, 0, 0, 0]
    counter = 0
    for char in ORDER:
        value[char - 1] = brailleCode[counter]
        counter += 1
    return "".join(value)


def solution(text):
    result = ""
    for char in text:
        if char.isupper():
            result += order(convert("uppercase"))
            char = char.lower()
        result += order(convert(char))
    return result