import random
words = ['cat', 'apple', 'baboons', 'dog', 'mouse', 'mice']

ran_word = random.choice(words)
num_word = len(ran_word)

dash_blank = num_word * '_'

print(f'{ran_word} {num_word} {dash_blank}')

user_guess = input('Guess a letter: ')

if user_guess == 