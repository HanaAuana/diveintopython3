a_list = [1, 9, 8, 4]
b_list = [elem * 2 for elem in a_list]
print(a_list)
print(b_list)
import os
import glob
files = [os.path.realpath(f) for f in glob.glob('../*.txt')]
print(files)
#Create list containing all files found in '../' larger than 6000 bytes
big_files = [f for f in glob.glob('../*') if os.stat(f).st_size > 6000]
print(big_files)
import humansize
print([(humansize.approximate_size(os.stat(f).st_size), f) for f in glob.glob('../*.txt')])
a_dict = {'a': 1, 'b': 2, 'c': 3}
print({value:key for key, value in a_dict.items()})
a_set = set(range(10))
print(a_set)
b_set = {x**2 for x in a_set}
print(b_set)
b_set = {x for x in a_set if x % 2 == 0}
print(b_set)
b_set = {2**x for x in a_set}
print(b_set)