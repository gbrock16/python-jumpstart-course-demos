

# Different ways to create dict
lookup = {}
lookup = dict()
lookup = {'age': 42, 'loc': 'Italy'}
lookup = dict(age=42, loc='Italy')

print(lookup)
print(lookup['loc'])

lookup['cat'] = 'Fun code demos'

if 'cat' in lookup:
    print(lookup['cat'])

# suppose these came from a data source, e.g. database, web service, etc.
# and we want to randomly access them

import collections

User = collections.namedtuple('User', "id, name, email")
users = [
    User(1, 'user1', 'user1@talkpython.fm'),
    User(2, 'user2', 'user2@talkpython.fm'),
    User(3, 'user3', 'user3@talkpython.fm'),
    User(4, 'user4', 'user4@talkpython.fm')
]

lookup = dict()
for u in users:
    lookup[u.email] = u

print(lookup['user4@talkpython.fm'])
