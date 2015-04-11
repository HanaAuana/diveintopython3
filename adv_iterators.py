#Using regex to find words in a string
import re
words = re.findall('[A-Z]+', 'SEND + MORE == MONEY')
print(words)

#Using sets to find unique items
combined = ''.join(words)
print(combined)
unique_chars = set(combined)
print(unique_chars)

#Generator expression
char_values = tuple(ord(c) for c in unique_chars)
print(char_values)

#Permutations using itertools
import itertools
perms = itertools.permutations([1, 2, 3], 2)
for p in perms:
    print(p)

perms = itertools.permutations('ABC', 3)
for p in perms:
    print(p)
perms = itertools.permutations('ABC', 3)
print(list(perms))

#Computing Cartesian (cross) product with itertools
print(list(itertools.product('ABC', '123')))

#Finding combinations with itertools
print(list(itertools.combinations('ABC', 2)))

#Iterate over each line in a file, build a list
names = list(open('people.txt', encoding='utf-8'))
print(names)
#Use rstrip() to remove trailing whitespace
names = [name.rstrip() for name in names]
print(names)
#sorted() sorts alphabetically by default
names = sorted(names)
print(names)
#Can pass a function as the key parameter
names = sorted(names, key=len)
print(names)

#Group items from a sequence using a key function, returns iterator that generates pairs
#groupby() only works if the items are already sorted by the grouping function
groups = itertools.groupby(names, len)
print(groups)
print(list(groups))
groups = itertools.groupby(names, len)
for name_length, name_iter in groups:
    print('Names with {0:d} letters:'.format(name_length))
    for name in name_iter:
        print(name)

#chain() joins iterators returns a singl eiterator containing all of the items from each
print(list(itertools.chain(range(0,3), range(10,13))))

#zip() returns an iterator that joins sequences in a tuple
print(list(zip(range(0,3), range(10,14))))
#Though zip() stops with the shorter sequence, zip_longest() inserts None for the rest
print(list(itertools.zip_longest(range(0,3), range(10,14))))

characters = ('S', 'M', 'E', 'D', 'O', 'N', 'R', 'Y')
guess = ('1', '2', '0', '3', '4', '5', '6', '7')

print(tuple(zip(characters, guess)))
print(dict(zip(characters, guess)))

characters = tuple(ord(c) for c in 'SMEDONRY')
print(characters)
guess = tuple(ord(c) for c in '91570682')
print(guess)
translation_table = dict(zip(characters, guess))
print(translation_table)
test = 'SEND + MORE == MONEY'.translate(translation_table)
print('SEND + MORE == MONEY')
print(test)

print(eval(test))
print(eval('"MARK".translate({65: 79})'))
print(eval('["*"] * 5'))
x = 5
print(eval("x * 5"))