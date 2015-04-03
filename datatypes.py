#Booleans

size = 1
size < 0
#False
size = 2
size > 1
#True

#Numbers

type(1)
#<class 'int'>
isinstance(1, int)
#True
1 + 1
#2
1 = 1.0
#2.0
type(2.0)
#<class 'float'>
float(2)
#2.0
int(2.0)
#2
int(2.5)
#2
int(-2.5)
#-2
11 // 2
#5
-11 // 2
#-6

#Lists

a_list = ['a', 'b', 'mpilgrim' 'z', 'example']
a_list[0]
#'a'
a_list[-1]
#'example'
a_list[1:3]
#[b', 'mpilgrim']
a_list[:3]
#['a', 'b', 'mpilgrim']
a_list[3:]
#['z', 'example']
a_list[:]
#['a', 'b', 'mpilgrim', 'z', 'example']
a_list = ['a']
a_list + [2.0, 3]
a_list
#['a', 2.0, 3]
a_list.append(True)
a_list
#['a', 2.0, 3, True]
a_list.extend(['four', 'U'])
a_list
#['a', 2.0, 3. True, 'four', 'U']
a_list.insert(0, 'U')
a_list
#['U', 'a', 2.0, 3, True, 'four', 'U']
a_list = ['a', 'b', 'new' 'mpilgrim', 'new']
a_list.count('new')
#2
'new' in a_list
#True
'c' in a_list
#False
a_list.index('mpilgrim')
#3
a_list.index('new')
#2
a_list[1]
#'b'
del a_list[1]
a_list
#['a', 'new', 'mpilgrim', 'new']
alist[1]
#'new'
a_list.remove('new')
a_list
#['a', 'mpilgrim', 'new']
a_list.remove('new')
a_list
#['a', 'mpilgrim']
a_list = ['a', 'b', 'new' 'mpilgrim']
a_list.pop()
#'mpilgrim'
a_list
#['a', b', 'new']
a_list.pop(1)
#'b'
a_list
#['a', 'new']

#Tuples
a_tuple = ('a', 'b', 'mpilgrim', 'z', 'example')
a_tuple[1]
#'b'
a_tuple[-1]
#'example'
a_tuple[1:3]
#('b', 'mpilgrim')
a_tuple.index('example')
#4
'z' in a_tuple
#True
v = ('a', 2, True)
(x, y, z) = v
x
#'a'
y
#2
z
#True
(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)
MONDAY
#0
SUNDAY
#6

#SETS
a_set = {1,2}
a_list = ['a', 'b', 'mpilgrim', True, False, 42]
a_set = set(a_list)
a_set
#{'a', 'b', 'mpilgrim', True, False, 42}
a_set = set()
a_set
#set()
type(a_set)
#<class 'set'>
a_set = {1, 2}
a_set.add(4)
a_set
#{1, 2, 4}
len(a_set)
#3
a_set.add(1)
a_set
#{1, 2, 4}
a_set.update({2, 4, 6})
a_set
#{1, 2, 4, 6}
a_set.update({3, 6, 9}, {1, 2, 3, 5, 8, 13})
a_set
#{1, 2, 3, 4, 5, 6, 8, 9, 13}
a_set.update([10, 20, 30])
#{1, 2, 3, 4, 5, 6, 8, 9, 10, 14, 20, 30}
a_set = {1, 3, 6, 10, 15, 21, 28, 36, 45}
a_set.discard(10)
#{1, 3, 6, 15, 21, 28, 36, 45}
a_set.discard(10)
#{1, 3, 6, 15, 21, 28, 36, 45}
a_set.remove(21)
#{1, 3, 6, 15, 28, 36, 45}
a_set.remove(21)
#KeyError: 21
a_set = {1, 3, 6, 10, 15, 21, 28, 36, 45}
a_set.pop()
#1
a_set.pop()
#3
a_set
#{6, 10, 15, 21, 28, 36, 45}
a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
30 in a_set
#True
31 in a_set
#False
a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}
a_set.union(b_set)
#{1, 2, 195, 4, 5, 6, 8, 12, 76, 15, 17, 18, 3, 21, 30, 51, 9, 127}
a_set.intersection(b_set)
#{2, 5, 9, 12, 21}
a_set.difference(b_set)
#{4, 30, 51, 76, 127, 195}
a_set.symmetric_difference(b_set)
#{1, 3, 4, 6, 8, 15, 17, 18, 30, 51, 76, 127, 195}
b_set.symmetric_difference(a_set)
#{1, 3, 4, 6, 8, 15, 17, 18, 30, 51, 76, 127, 195}
b_set.intersection(a_set) == a_set.intersection(b_set)
#True
b_set.union(a_set) == a_set.union(b_set)
#True
b_set.difference(a_set) == a_set.difference(b_set)
#False
a_set = {1, 2, 3}
b_set = {1, 2, 3, 4}
b_set.issubset(b_set)
#True
b_set.issuperset(a_set)
#True

#Dictionaries
dict = {'server':'diveintopython.org', 'database':'mysql'}
dict['server']
#'diveintopython.org'
dict['database'] = 'postgres'
dict
#{'server':'diveintopython.org','database':postgres'}
dict['user'] = 'rick'
dict
#{'server':'diveintopython.org', 'user':'rick', database':postgres'}
SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}
len(SUFFIXES)
#2
1000 in SUFFIXES
#True
SUFFIXES[1000]
#['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
SUFFIXES[1000][3]
#'TB'

#None
type(None)
#<class 'NoneType'>
None == False
#False
None == 0
#False
None == ''
#False
None == None
#True
x = None
x == None
#True
y = None
x == y
True