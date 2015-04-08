import re
s = '100 NORTH BROAD ROAD'
print(s.replace('ROAD', 'RD.'))
print(re.sub('ROAD$', 'RD.', s))
s = '100 BROAD ROAD APT. 3'
# prefix strings with r to use raw strings, avoiding the need to escape a '\'
# \b denotes a word boundry
print(re.sub(r'\bROAD\b', 'RD.', s))
#pattern to match roman numeral 'thousands'
pattern = '^M?M?M?$'
#re.search() returns an object if a match is found, else returns None
print(re.search(pattern, 'M'))
print(re.search(pattern, 'MMM'))
#pattern denotes a complete string of up to three optional 'M's with, so 4 is not a match
print(re.search(pattern, 'MMMM'))
#The 'M's are all optional, so an empty string is a match
print(re.search(pattern, ''))
#pattern to match roman numeral 'hundreds'
#groups in parentheses separated by bars are mutually exclusive patterns
#parser goes left to right, and takes the first match
pattern = '^M?M?M?(CM|CD|D?C?C?C?)$'
print(re.search(pattern, 'MCM'))
print(re.search(pattern, 'MD'))
print(re.search(pattern, 'MMMCCC'))
print(re.search(pattern, 'MCMC'))
print(re.search(pattern, ''))
#alternate method of defining repeated characters
pattern = '^M{0,3}$'
print(re.search(pattern, 'M'))
#expand roman numeral pattern to match tens as well
pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})$'
print(re.search(pattern, 'MCMXL'))
print(re.search(pattern, 'MCML'))
print(re.search(pattern, 'MCMLX'))
print(re.search(pattern, 'MCMLXXX'))
print(re.search(pattern, 'MCMLXXXX'))
#pattern to include ones as well
pattern = '^M{0.2}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
#example of verbose regular expression
pattern = '''
    ^                   # beginning of string
    M{0,3}              # thousands - 0 to 3 Ms
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                        #            or 500-800 (D, followed by 0 to 3 Cs)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                        #        or 50-80 (L, followed by 0 to 3 Xs)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                        #        or 5-8 (V, followed by 0 to 3 Is)
    $                   # end of string
    '''
#need to include the re.VERBOSE constant as a third argument
print(re.search(pattern, 'MCMLXXXIX', re.VERBOSE))
#without the VERBOSE flag, the pattern will not match (due to whitespace and comments)
print(re.search(pattern, 'M'))
#creating pattern to match US phone numbers in variety of formats
phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
print(phonePattern.search('800-555-1212').groups())
print(phonePattern.search('800-555-1212-1234'))
phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})-(\d+)$')
print(phonePattern.search('800-555-1212-1234').groups())
#pattern that handles separators other than just hypens (any non-digit character)
#also allows extension to be omitted (0 or more characters)
phonePattern = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{4})\D+(\d+)$')
print(phonePattern.search('800 555 1212 1234').groups())
print(phonePattern.search('800-555-1212-1234').groups())
phonePattern = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
print(phonePattern.search('80055512121234').groups())
print(phonePattern.search('800.555.1212 x1234').groups())
print(phonePattern.search('800-555-1212').groups())
#allows for non-digit characters at the start as well
phonePattern = re.compile(r'^\D*(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
print(phonePattern.search('(800)5551212 ext. 1234').groups())
print(phonePattern.search('800-555-1212').groups())
#Don't worry about starting at the exact beginning of the string
phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
print(phonePattern.search('work 1-(800) 555.1212 #1234').groups())
print(phonePattern.search('800-555-1212').groups())
print(phonePattern.search('80055512121234').groups())
#verbose example. much more readable
#when using re.compile(), no need to use VERBOSE flag on each re.search() call
phonePattern = re.compile(r'''
                # don't match beginning of string, number can start anywhere
    (\d{3})     # area code is 3 digits (e.g. '800')
    \D*         # optional separator is any number of non-digits
    (\d{3})     # trunk is 3 digits (e.g. '555')
    \D*         # optional separator
    (\d{4})     # rest of number is 4 digits (e.g. '1212')
    \D*         # optional separator
    (\d*)       # extension is optional and can be any number of digits
    $           # end of string
    ''', re.VERBOSE)
print(phonePattern.search('work 1-(800) 555.1212 #1234').groups())
print(phonePattern.search('800-555-1212').groups())