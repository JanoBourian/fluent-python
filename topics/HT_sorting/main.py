from datetime import datetime

### Working with sorted method
items = [3, 5, 7, 8, 4, 2]
values_level = dict(even=1, odd=0)

def odd_first(value):
    tag = "odd" if value%2!=0 else "even"
    return value*values_level[tag]

for item in sorted(items, key=odd_first):
    print(item)

### Another example
# (id, name, datetime)
db_records = [
    (1,"john", datetime(2024, 1, 15)),
    (2,"pink", datetime(2024, 2, 14)),
    (3,"mark", datetime(2023, 9, 19))
    ]

for record in sorted(db_records, key= lambda item: item[2]):
    print(record)