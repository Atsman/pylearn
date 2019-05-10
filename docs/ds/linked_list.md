# Linked List

## Definition

Linked List is a ds that represents a sequence of nodes. In a single LinkedList, each node points to the next node in the ll. A doubly list gives each node poiters to both the next node and the previouse node.

## Efficiency

Get / Set: O(N)

Insert / Delete at beginning O(1)

Wasted space O(N)

## Example

```python
class Node:
  def __init__(self, value):
    self.next = None
    self.value = value

class LinkedList:
  def __init__(self):
    self.root = None

  def append(self, value):
    .
    .
    .

  def prepend(self, value):
    .
    .
    .
```
