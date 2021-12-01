import random
""" import random module
"""
def welcome():
    """Welcome function"""
    name = input(""">Welcome to Hangman Game! Enter your game name: <""").capitalize()
    
    if name.isalpha() == true:
        """Only alphapets in name"""
        print(""">> Hi""",name,"""<<<
        The computer will randomly choose a word and you will try to guess the word.
        Good luck""")

    else:
        print('please enter letter only for name')
        name = input('Enter game name here: ')
        print('Hi!',name,)


