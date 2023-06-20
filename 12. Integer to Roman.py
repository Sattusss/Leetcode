class Solution:
    def intToRoman(self, num: int) -> str:
        # Create lookup tables for the Roman symbols and their respective values
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        roman_numeral = ''
        index = 0

        while num > 0:
            # Check if the current symbol can be subtracted from the number
            if num >= values[index]:
                roman_numeral += symbols[index]
                num -= values[index]
            else:
                # Move to the next symbol if the current one cannot be subtracted
                index += 1

        return roman_numeral
