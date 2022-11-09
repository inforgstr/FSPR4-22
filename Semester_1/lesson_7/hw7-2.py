'''
Applying the methods of dictionaries:

    clear
    copy
    fromkeys
    get
    items
    keys
    pop
    popitem
    setdefault
    update
    values
'''
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# Method - clear()
user = {
    'key': 'value',
    'dog': 'boxer',
    'cat': 'tiger',
}
user.clear()
print(user, '\n')

# -------------------------------------------------------------------

# Method - copy()
user = {
    'key': 'value',
    'dog': 'boxer',
    'cat': 'tiger',
}
user2 = user.copy()
print(user2, '\n')

# -------------------------------------------------------------------

# Method - fromkeys
user = ('plant', 'pet', 'dog', 'cat')
user_o = 'black'
user_is = dict.fromkeys(user, user_o)
print(user, user_is, sep='\n')

# ------------------------------------------------------------------

# Method - get
user = {
    'key': 'value',
    'dog': 'boxer',
    'cat': 'tiger',
}

out = user.get('dog')
print(out)

# или
out = user.get('shark', 'white')
print(out)

# --------------------------------------------------------------------
# Method - items()
user = {
    'key': 'value',
    'dog': 'boxer',
    'cat': 'tiger',
}
users = user.items()
user['dog'] = 'black'

print(users)
# ---------------------------------------------------------------------
# Method - keys()
user = {
    'key': 'value',
    'dog': 'boxer',
    'cat': 'tiger',
}
user1 = user.keys()
user['tiger'] = 'white'
print(user1)

# -----------------------------------------------------------------------
# Method - pop()
user = {
    'key': 'value',
    'dog': 'boxer',
    'cat': 'tiger',
}
user.pop('key')
print(user)

# ------------------------------------------------------------------------
# Method - popitem()
user = {
    'key': 'value',
    'dog': 'boxer',
    'cat': 'tiger',
}
user1 = user.popitem()
print(user1)

# ---------------------------------------------------------------------------

# Method - setdefault()
user = {
    'key': 'value',
    'dog': 'boxer',
    'cat': 'tiger',
}
user2 = user.setdefault('cat', 'white')
print(user2)

# ----------------------------------------------------------------------------
# Method - update()

user = {
    'key': 'value',
    'dog': 'boxer',
    'cat': 'tiger',
}
user.update({'color': 'blue'})
print(user)

# ---------------------------------------------------------------------------
# Method - values()
user = {
    'key': 'value',
    'dog': 'boxer',
    'cat': 'tiger',
}
users = user.values()
user['dog'] = 'black'
print(users)