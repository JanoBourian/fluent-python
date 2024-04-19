import timeit

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirt = [(color, size) for color in colors for size in sizes]
print(tshirt)

tshirts = []
for color in colors:
    for size in sizes:
        tshirts.append(
            (color, size)
        )

print(tshirt)

### Testing time of each operation
TIMES = 100000
SETUP = """
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
"""
FOR_STATEMENT = """
tshirts = []
for color in colors:
    for size in sizes:
        tshirts.append(
            (color, size)
        )
"""

def clock(label:str, cmd:str) -> None:
    res = timeit.repeat(cmd, repeat=10, setup=SETUP, number=TIMES)
    print(label, *(f'{x:.3f}' for x in res))

clock('listcomp        :', '[(color, size) for color in colors for size in sizes]')
clock('tuplecomp       :', '((color, size) for color in colors for size in sizes)')
clock('for statement   :', FOR_STATEMENT)