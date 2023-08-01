# fluent-python
A repository based on fluent python book

# Collections

## Set
* isdisjoint
* \_\_le\_\_
* \_\_lt\_\_
* \_\_gt\_\_
* \_\_ge\_\_
* \_\_eq\_\_
* \_\_ne\_\_
* \_\_and\_\_
* \_\_or\_\_
* \_\_sub\_\_
* \_\_xor\__

## Mapping
* \_\_getitem\_\_
* \_\_contains\_\_
* \_\_eq\_\_
* \_\_ne\_\_
* get
* items
* keys
* values

## Sequence
* \_\_getitem\_\_
* \_\_contains\_\_
* \_\_iter\_\_
* \_\_reversed\_\_
* index
* count

## Reversible
* \_\_reversed\_\_

## Iterable
* \_\_iter\_\_

## Sized
* \_\_len\_\_

## Container
* \_\_contains\_\_

# ABC

* Iterable (to support iter operator)
* Sized (to support len operator)
* Container (to support in operator)

# Special methods overview

## String/bytes representation

* \_\_repr\_\_
* \_\_str\_\_
* \_\_format\_\_
* \_\_bytes\_\_
* \_\_fspath\_\_

## Conversion to number

* \_\_bool\_\_
* \_\_complex\_\_
* \_\_int\_\_
* \_\_float\_\_
* \_\_hash\_\_
* \_\_index\_\_

## Emullating collections

* \_\_len\_\_
* \_\_getitem\_\_
* \_\_setitem\_\_
* \_\_deleteitem\_\_
* \_\_contains\_\_

## Iteration

* \_\_iter\_\_
* \_\_aiter\_\_
* \_\_next\_\_
* \_\_reversed\_\_

## Callable or coroutine execution

* \_\_call\_\_
* \_\_await\_\_

## Context management

* \_\_enter\_\_
* \_\_exit\_\_
* \_\_aexit\_\_
* \_\_aenter\_\_

## Instance creation and destruction

* \_\_new\_\_
* \_\_init\_\_
* \_\_delete\_\_

## Attribute management

* \_\_getattr\_\_
* \_\_getattribute\_\_
* \_\_setattr\_\_
* \_\_delattr\_\_
* \_\_dir\_\_

## Attribute descriptors

* \_\_get\_\_
* \_\_set\_\_
* \_\_delete\_\_
* \_\_setname\_\_

## Abstract base classes

* \_\_instancecheck\_\_
* \_\_subclasscheck\_\_

## Class metaprogramming

* \_\_prepare\_\_
* \_\_init_subclass\_\_
* \_\_class_gettitem\_\_
* \_\_mro_entries\_\_

## Unary numeric

* \_\_neg\_\_
* \_\_pos\_\_
* \_\_abs\_\_

## Rich comparison

* \_\_lt\_\_
* \_\_le\_\_
* \_\_eq\_\_
* \_\_ne\_\_
* \_\_gt\_\_
* \_\_ge\_\_

## Arithmetic

* \_\_add\_\_
* \_\_sub\_\_
* \_\_mul\_\_
* \_\_truediv\_\_
* \_\_floordiv\_\_
* \_\_mod\_\_
* \_\_matmul\_\_
* \_\_divmod\_\_
* \_\_round\_\_
* \_\_pow\_\_

## Reversed arithmetic

* \_\_radd\_\_
* \_\_rsub\_\_
* \_\_rmul\_\_
* \_\_rtruediv\_\_
* \_\_rfloordiv\_\_
* \_\_rmod\_\_
* \_\_rmatmul\_\_
* \_\_rdivmod\_\_
* \_\_rround\_\_
* \_\_rpow\_\_

## Augmented assignmet arithmetic

* \_\_iadd\_\_
* \_\_isub\_\_
* \_\_imul\_\_
* \_\_itruediv\_\_
* \_\_ifloordiv\_\_
* \_\_imod\_\_
* \_\_imatmul\_\_
* \_\_ipow\_\_

## Bitwise

* \_\_and\_\_
* \_\_or\_\_
* \_\_xor\_\_
* \_\_lshift\_\_
* \_\_rshift\_\_
* \_\_invert\_\_

## Reversed bitwise

* \_\_rand\_\_
* \_\_ror\_\_
* \_\_rxor\_\_
* \_\_rlshift\_\_
* \_\_rrshift\_\_

## Augmented assignment bitwise

* \_\_iand\_\_
* \_\_ior\_\_
* \_\_ixor\_\_
* \_\_ilshift\_\_
* \_\_irshift\_\_