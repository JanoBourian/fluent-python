from collections import abc
print(issubclass(tuple, abc.Sequence))
print(issubclass(list, abc.MutableSequence))

symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

codes = [ord(symbol) for symbol in symbols]
print(codes)

## Walrus operator
x = 'ABC'
codes = [ord(x) for x in x]
print(x)
print(codes)

codes = [last := ord(c) for c in x]
print(last)

## List comprehensions and filter and map
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)