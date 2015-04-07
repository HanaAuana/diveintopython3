s = '深入 Python' 
print(len(s))
username = 'rick'
password = 'PapayaWhip'
print("{0}'s password is {1}".format(username, password))
import humansize
si_suffixes = humansize.SUFFIXES[1000]
print(si_suffixes)
#Compount field names
print('1000{0[0]} = 1{0[1]}'.format(si_suffixes))
import sys
print('1MB = 1000{0.modules[humansize].SUFFIXES[1000][0]}'.format(sys))
#Format specifier
print('{0:.1f} {1}'.format(698.24, 'GB'))
s = '''Finished files are the re-
sult of years of scientif-
ic study combined with the
experience of years.'''
print(s.splitlines())
print(s.lower())
print("Found {0} f's".format(s.count('f')))
print(s.lower().count('f'))
query = 'user=pilgrim&database=master&password=PapayaWhip'
a_list = query.split('&')
print(a_list)
a_list_of_lists = [v.split('=', 1) for v in a_list if '=' in v]
print(a_list_of_lists)
a_dict = dict(a_list_of_lists)
print(a_dict)
a_string = 'My alphabet starts where your alphabet ends.'
print(a_string[3:11])
print(a_string[0:2])
print(a_string[:18])
print(a_string[18:])
by = b'abcd\x65' 
print(by)
by += b'\xff' 
print(by)
print(by[0])
by = b'abcd\x65'
barr = bytearray(by)
print(barr)
print(len(barr))
barr[0] = 102
print(barr)
by = b'd'
s = 'abcde'
print(s.count(by.decode('ascii')))
a_string = '深入 Python'
print(len(a_string))
by = a_string.encode('utf-8')
print(by)
print(len(by))
by = a_string.encode('gb18030')
print(by)
print(len(by))
b_string = by.decode('gb18030')
print(a_string == b_string)