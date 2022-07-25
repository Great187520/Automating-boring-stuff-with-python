import random
from random import randint

messages = ['oranges',
            'balls',
            'corns',
            'yam']
print(messages[randint(0, len(messages) - 1)])
