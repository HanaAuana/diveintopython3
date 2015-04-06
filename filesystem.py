import os
print(os.getcwd())
#...\diveintopython3
os.chdir('../')
print(os.getcwd())
#...\Desktop
print(os.path.join('/Users/Michael/Desktop/diveintopython3/', 'filesystem.py'))
print(os.path.join('/Users/Michael/Desktop/diveintopython3', 'filesystem.py'))
print(os.path.expanduser('~'))
pathname = '/Users/Michael/Desktop/diveintopython3/filesystem.py'
print(os.path.split(pathname))
(dirname, filename) = os.path.split(pathname)
print(dirname)
(shortname, extension) = os.path.splitext(filename)
print(extension)
import glob
print(glob.glob('*.txt'))
metadata = os.stat('finances.txt')
print(metadata.st_mtime)
import time
print(time.localtime(metadata.st_mtime))
print(metadata.st_size)
import humansize
print(humansize.approximate_size(metadata.st_size))
print(os.path.realpath('finances.txt'))