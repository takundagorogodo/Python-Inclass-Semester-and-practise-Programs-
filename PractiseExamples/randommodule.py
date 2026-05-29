import random
print(random.randint(10, 29))
print(random.randrange(2, 5))
print(random.random())
print(random.uniform(5, 10))
print(random.choice(['red', 'green', 'blue']))
cards = ['Ace', 'King', 'Queen', 'Jack']
random.shuffle(cards)
print(cards)
