line_number = 0

with open('people.txt', encoding='utf-8') as file:
    for line in file:
        line_number += 1
        print('{:>4} {}'.format(line_number, line.rstrip()))

with open('test.log', mode='w', encoding='utf-8') as file:
    file.write('test succeeded')

with open('test.log', encoding='utf-8') as file:
    print(file.read())

with open('test.log', mode='a', encoding='utf-8') as file:
    file.write('and again')

with open('test.log', encoding='utf-8') as file:
    print(file.read())

image = open('beauregard.jpg', mode='rb')
print(image.name)
print(image.tell())
data = image.read(3)
print(data)
print(len(image.read()))
image.seek(0)
print(len(image.read()))

string = 'PapayaWhip is the new black'
import io
file = io.StringIO(string)
print(file.read())

import gzip
with gzip.open('out.log.gz', mode='wb') as zipped:
    zipped.write('eighteen miles out'.encode('utf=8'))

# Redirecting stdout
import sys


class RedirectStdoutTo:

    def __init__(self, new_out):
        self.new_out = new_out

    def __enter__(self):
        self.old_out = sys.stdout
        sys.stdout = self.new_out

    def __exit__(self, *args):
        sys.stdout = self.old_out

print('A')
with open('out.log', mode='w', encoding='utf-8') as file:
    with RedirectStdoutTo(file):
        print('B')
print('C')
