import random
import nltk

nltk.download('all')


when = ['A few decades ago', 'Tomorrow', 'Last evening', 'Recently','On the 30th of May']
who = ['the tiger', 'the skunk', 'the raccoon', 'the alligator','the wolverine']
residence = ['box','straw house', 'condo', 'farm', 'townhouse']
went = ['Theater', 'College','Kingdom', 'school', 'clean the toilet']
happened = ['made new friends','Eats pasta ', 'found a treasure chest', 'solved a mystery', 'wrote a comic']

noun = input('enter a noun ')
adjective = input('enter a adjective ')
pronoun = input('enter a pronoun ')
adverb = input('enter a adverb ')
verb = input('enter a verb ')
conjunction = input('enter a conjunction ')

print(f'{random.choice(when)}, {noun} {random.choice(who)} lived in a {adjective} {random.choice(residence)}, {pronoun} {adverb} {verb} to the {random.choice(went)}, {conjunction} {random.choice(happened)}')


