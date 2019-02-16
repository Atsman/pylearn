# Array

## Definition

Is a ds consisting of a collection of elements of the same type, each identified by array index.

## Dynamic arrays

Array has static size. Inserting or removing elements is not allowed.

However by allocating a new array and copying the contents of the old array to it, it is possible to effectively implement a dynamic version of an array.

## Efficiency

Get / Set - O(1)

## Example python

*Array*

```python
import array

arr = array.array('i', [1, 2, 3])

for x in arr:
  print(x)
```

*List*
```python

ll = [1, 2, 3]

for x in arr:
  print(x)
```
