# Bit Manipulation

## Operators

* `&`: AND

```
1 & 1 = 1
1 & 0 = 0
0 & 1 = 0
0 & 0 = 0
```

* `|`: OR

```
1 | 1 = 1
1 | 0 = 1
0 | 1 = 1
0 | 0 = 0
```

* `^`: XOR

```
1 ^ 1 = 0
1 ^ 0 = 1
0 ^ 1 = 1
0 ^ 0 = 0
```

* `~`: NOT

```
~ 1 = -10
~ 0 = -1 
```

* `<<`: Binary left shift (multiply by 2)

```
1 << 1 = 10
1 << 2 = 100
1 << 3 = 1000
```

* `>>`: Binary right shift (divide by 2)

```
1000 >> 1 = 100
1000 >> 2 = 10
1000 >> 3 = 1
```

## Practical 

### Read bit at a specific position

Shift uninterested bits to the right and use *bitmask*.

```
bitmask = 0b1
(0b1101 >> 2) & bitmask # 1
(0b1101 >> 1) & bitmask # 0
```

The bitmask controls how much info is returned. To get two bits use two bits mask.
```
bitmask = 0b11
(0b1101 >> 2) & bitmask # 11
```

### Set a bit

Set bit to one

```
byte = 0b0000
mask = 0b1 << 2 # 0100
byte | mask # 0100
```

Toggle bit at a specific position

```
byte = 0b1111
mask = 0b1 << 2 # 0000
byte ^ mask # 1011
```

### Change specific bit 

[Change specific bit](../py/primitives/specific_bit.py)

### Binary flags


```
None      = 0b000000
Stark     = 0b000001
Targarian = 0b000010
Martel    = 0b000100
Tully     = 0b001000
Frey      = 0b010000
Lanister  = 0b100000
```

Mixed?

```
StarkAndTargarian = Stark | Targarian
StarkAndTully = Stark | Tully
```

### Convert Int to Bin 

```python
bin(7) # '0b111'
```
