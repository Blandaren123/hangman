import random
""" import random module generator
"""
from collections import Counter
""" Counters store elements as dictionary keys, and their counts are stored as dictionary values
"""

someWords = '''audi jeep cadillac chevrolet chrysler dodge ford kia
lexus nissan porche subaru skoda volvo''' 
""" add som car brands to the list """

someWords = someWords.split('')
word = random.choice(someWords)
""" let randomness choose word from the someWords list"""

if __name__ == '__main__':
    """by using an import block, we can allow or prevent certain parts of the code from being run"""
    print('Guess Car brands')
    
    for i in word:
        print('_', end =' ')
    print()

    playing = True
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        