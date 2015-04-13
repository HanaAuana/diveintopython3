entry = {}
entry['title'] = 'Dive into history'
entry['article_link'] = 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition'
entry['comments_link'] = None
entry['internal_id'] = b'\xDE\xD5\xB4\xF8'
entry['tags'] = ('diveintopython', 'docbook', 'html')
entry['published'] = True
import time
entry['published_date'] = time.strptime('Fri Mar 27 22:20:42 2009')

import pickle
with open('entry.pickle', 'wb') as f:
    pickle.dump(entry, f)

with open('entry.pickle', 'rb') as f:
    entry1 = pickle.load(f)
print(entry1)
with open('entry.pickle', 'rb') as f:
    entry2 = pickle.load(f)
print(entry == entry1 == entry2)
print(entry is entry2)

b = pickle.dumps(entry)
print(type(b))
entry3 = pickle.loads(b)
print(entry == entry3)

import pickletools
with open('entry.pickle', 'rb') as f:
    print(pickletools.dis(f))


basic_entry = {}
basic_entry['id'] = 256
basic_entry['title'] = 'Dive into history, 2009 edition'
basic_entry['tags'] = ('diveintopython', 'docbook', 'html')
basic_entry['published'] = True
basic_entry['comments_link'] = None
import json
with open('basic.json', mode='w', encoding='utf-8') as f:
    json.dump(basic_entry, f, indent=2)

with open('basic.json', mode='r', encoding='utf-8') as f:
    basic = json.load(f)
print(basic)
