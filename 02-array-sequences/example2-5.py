def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True
tf = ('1', 2, ('a', 'b'))
tm = ('1', 2, ['a', 'b'])

print(fixed(tf))
print(fixed(tm))