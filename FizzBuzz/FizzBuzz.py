from GetSetStartingAt import GetSetStartingAt as setBuilder
import math

class FizzBuzz:
    def translateNumberToWord(self, number):
        remainder = (number % 15)
        number_of_sets = math.floor((number / 15)) + 1

        results = []
        for x in range(number_of_sets - 1):
            y = setBuilder.generateSetStartingAt(x)
            results.append(y)
        results.append(setBuilder.generateSetStartingAt(x + 15, remainder))
        return results
