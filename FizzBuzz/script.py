from FizzBuzz import FizzBuzz

def main():
    
    # x % 3 == 0 -> Fizz
    # x % 5 == 0 -> Buzz
    # x % 5 == 0 && x % 3 == 0 -> FizzBuzz
    game = FizzBuzz()
    print(game.translateNumberToWord(0))
    print(game.translateNumberToWord(9))

    pass

if __name__ == '__main__':
    main()