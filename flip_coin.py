import random

print('Welcome to flip \'a coin')
print('Type \'help\'')
flip = ""


class Coin:
    """ Welcome, this program was made in 2020 and it's a coin
    flipping simulator, run the program and see what happens """

    def __init__(self):
        self.items = []

    def ask_flip(self):
        while True:
            flip = input('Command> ')
            if flip.lower() == 'yes':
                return self.flip_coin()
            elif flip.lower() == 'help':
                print("""
This is a coin flipping game,
type 'yes' to flip. You can also type
'get' to see the results of the flips.
Type 'no' to quit the game
""")
                return self.ask_flip()
            elif flip.lower() == 'get':
                return self.get_flips()
            elif flip.lower() == 'no':
                return 'See you later'
            else:
                return 'Invalid'

    def flip_coin(self):
        num = random.randint(1, 2)
        if num == 1:
            num = 'heads'
            self.items.append(num)
            print('Coin was flipped')
            return self.ask_flip()

        else:
            num = 'tails'
            self.items.append(num)
            print('Coin was flipped')
            return self.ask_flip()

    def is_empty(self):
        return self.items == []

    def get_flips(self):
        for item in self.items:
            print(item)
        return self.ask_flip()
    """ Created by: Pedro Bento """


c = Coin()
print(c.ask_flip())



