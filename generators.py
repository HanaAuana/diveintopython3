import re

print("Start generators.py")


def match_sxz(noun):
    return re.search('[sxz]$', noun)

def apply_sxc(noun):
    return re.sub('$', 'es', noun)

def match_h(noun):
    return re.search('[^aeioudgkprt]h$', noun)

def apply_h(noun):
    return re.sub('$', 'es', noun)

def match_y(noun):
    return re.search('[^aeiou]y$', noun)

def apply_y(noun):
    return re.sub('y$', 'ies', noun)

def match_default(noun):
    return True

def apply_default(noun):
    return noun + 's'

rules = ((match_sxz, apply_sxc),
         (match_h, apply_h),
         (match_y, apply_y),
         (match_default, apply_default)
        )

def plural_1(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)

def plural_2(noun):
    if match_sxz(noun):
        return apply_sxz(noun)
    if match_h(noun):
        return apply_h(noun)
    if match_y(noun):
        return apply_y(noun)
    if match_default(noun):
        return apply_default(noun)

def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)

    return (matches_rule, apply_rule)

patterns = \
  (
    ('[sxz]$',           '$',  'es'),
    ('[^aeioudgkprt]h$', '$',  'es'),
    ('(qu|[^aeiou])y$',  'y$', 'ies'),
    ('$',                '$',  's')
  )

#This list of tuples should contain the same values (functions) as the previous rules
rules = [build_match_and_apply_functions(pattern, search, replace)
         for (pattern, search, replace) in patterns]

rules = []
#read in the replacement rules from a file this time
with open('plural-rules.txt', encoding='utf-8') as pattern_file:
    for line in pattern_file:
        #for each line, split on whitespace 3 times, leave the rest alone
        pattern, search, replace = line.split(None, 3)
        #build a set of match/apply functions from the strings for this line
        rules.append(build_match_and_apply_functions(pattern, search, replace))

def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b
#for loop will automatically call next on our generator
for n in fib(200):
    print(n, end = ' ')

print('')
print([n for n in fib(200)])
print(list(fib(200)))

def rules(pattern_filename):
    with open(pattern_filename, encoding='utf-8') as pattern_file:
        for line in pattern_file:
            pattern, search, replace = line.split(None, 3)
            #generate and apply match/apply functions on demand
            yield build_match_and_apply_functions(pattern, search, replace)

def plural(noun, pattern_filename='plural-rules.txt'):
    #since rules() is a generator, we can use it directly in the for loop
    for matches_rule, apply_rule in rules(pattern_filename):
        if matches_rule(noun):
            return apply_rule(noun)
    raise ValueError('no matching rule for {0}'.format(noun))

print("End generators.py")
