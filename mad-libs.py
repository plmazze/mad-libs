import random
# import nltk

# print(nltk.__version__)

# nltk.download('all')


when = ['A few decades ago', 'Tomorrow', 'Last evening', 'Recently','On the 30th of May']
who = ['a tiger', 'an skunk', 'a raccoon', 'a alligator','a wolverine']
name = ['Morgan', 'Mordecai','Jacob', 'Salvador', 'Cal']
residence = ['Manchester','Parma', 'Germany', 'Greece', 'France']
went = ['Theater', 'College','Kingdom', 'school', 'clean the toilet']
happened = ['made new friends','Eats pasta ', 'found a treasure chest', 'solved a mistery', 'wrote a comic']

print(f'{random.choice(when)}, {random.choice(who)} that lived in {random.choice(residence)} went to the {random.choice(went)}, {random.choice(happened)}')

# noun = input('enter a noun')
# pronoun = input('enter a noun')
# adjective = input('enter a noun')
# preposition = input('enter a noun')
# interjection = input('enter a noun')
# conjunction = input('enter a noun')
# verb = input('enter a noun')
# adverb = input('enter a noun')

# if !noun:
#   print('please type a noun')