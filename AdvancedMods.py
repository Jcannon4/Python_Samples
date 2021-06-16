from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple


list = [1,1,1,1,12,2,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5]

print(Counter(list)) #Easy and fast way to count lists

s = 'aasdddfffddsstttreyshffhhjpokemonpokemon'

print(Counter(s))

t = 'Each word is unique and the word will show up each time in the word counter for the counter program'
words = t.split()
print(Counter(words))

c = Counter(words)
print(c.most_common(2))

print(sum(c.values()))

#defaultdict

d = defaultdict(lambda: 0)
d['one']
d['two'] = 2
print(d)
for item in d:
    print(item)


#Ordered Dictionary

d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5
for k,v in d.items():
    print(k,v)
    
#Namedtuple

dog = namedtuple('dog','age breed name')
sam = dog(age = 2, breed = 'Lab', name = 'Sammy')
print('{} the {} is {} years old!' .format(sam.name, sam.breed, sam.age))

