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
    (3,"mark", datetime(2023, 9, 19)),
    (4,"albert", datetime(2023, 9, 19)),
    ]

for record in sorted(db_records, key= lambda item: item[2]):
    print(record)
    
### Operator Module Functions and Partial Function Evaluation
print("*")
from operator import itemgetter, attrgetter
sorted_records = sorted(db_records, key=itemgetter(2, 1), reverse=True)

for record in sorted_records:
    print(record)
    
### Partial sorts
print("*")
from random import randint
import timeit
import heapq

create_long_items = timeit.default_timer()
long_items_1 = [randint(0, 10000000000000) for _ in range(0, 100000)]
long_items_2 = [randint(0, 10000000000000) for _ in range(0, 100000)]
print(f"Create list: {timeit.default_timer() - create_long_items}")

start_1 = timeit.default_timer()
max_1 = max(long_items_1)
end_1 = timeit.default_timer() - start_1

start_2 = timeit.default_timer()
max_2 = heapq.nlargest(1, long_items_2)
end_2 = timeit.default_timer() - start_2


print(end_1, end_2)
print(max_1, max_2)

def test_speed(number: int):
    nlargest_total = 0
    max_total = 0
    tie = 0
    
    for _ in range(0, number):
        start_1 = timeit.default_timer()
        _ = max(long_items_1)
        end_1 = timeit.default_timer() - start_1

        start_2 = timeit.default_timer()
        _ = heapq.nlargest(1, long_items_2)
        end_2 = timeit.default_timer() - start_2
        
        if end_2 < end_1:
            nlargest_total += 1
        elif end_1 < end_2:
            max_total += 1
        else:
            tie += 1
            print(end_1, end_2)
    
    print(f"nlargest_total: {nlargest_total}, max_total: {max_total}, tie: {tie}")

for _ in range(0,100):
    test_speed(1000)
