import random
""" import random module generator
"""
from collections import Counter
""" Counters store elements as dictionary keys, and their counts are stored
as dictionary values
"""

someWords = '''audi jeep cadillac chevrolet chrysler dodge ford kia
lexus nissan porche subaru skoda volvo'''

someWords = someWords.split(' ')
word = random.choice(someWords)
""" let randomness choose word from the someWords list"""

if __name__ == '__main__':
    """by using an import block,
    we can allow or prevent certain parts of the code from being run"""
    print('Hello and Welcome to hang man Game')
    print('The Computer will Choose a random Word and you have to guess')
    print('Hint! Car brands')
    print('==================================')
    for i in word:
        print('_', end =' ')
    print()

    playing = True
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        while (chances != 0) and flag == 0:
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter')
                continue

            if not guess.isalpha():
                print('Enter only a letter')
                continue
            elif len(guess) > 1:
                print('Enter only single letter')
            elif guess in letterGuessed:
                print('You have already guessed that')
                continue

            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) 
                != Counter(word)):
                    print(char, end = ' ')
                    correct += 1
                elif (Counter(letterGuessed) == Counter(word)):

                    print("The word is: ", end=' ')
                    print(word)
                    flag = 1
                    print('You Won!!')
                    break
                    break
                else:
                    print('_', end = ' ')
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You loose!! Try Again.')
            print('The word was {}'.format(word))          
    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()