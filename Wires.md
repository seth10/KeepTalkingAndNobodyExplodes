### 3 wires
```
0 R => 2nd
Last W => 3rd
>1 B => last B
3rd
```

### 4 wires
```
>1 R, last digit odd => last R
1 B => 1st
Last Y, 0 R => 1st
>1 Y => 4th
2nd
```

### 5 Wires
```
Last K, last digit odd => 4th
No K, (≠1 R OR 0-1 Y) => 2nd
1st
```

### 6 Wires
```
0 Y, last digit odd => 3rd
1 Y, >1 W => 4th
0 R => 6th
4th
```

## Based on last digit of serial number
| # of Wires |   Even    |   Odd   |
| ---------- |   -----   |   ---   |
|      3     |   0 R => 2nd <br> Last W => 3rd <br> >1 B => last B <br> 3rd   |   0 R => 2nd <br> Last W => 3rd <br> >1 B => last B <br> 3rd   |
|      4     |   1 B => 1st <br> Last Y, 0 R => 1st <br> >1 Y => 4th <br> 2nd   |   >1 R => last R <br> 1 B => 1st <br> Last Y, 0 R => 1st <br> >1 Y => 4th <br> 2nd   |
|      5     |   No K, (≠1 R OR 0-1 Y) => 2nd <br> 1st   |   Last K => 4th <br> No K, (≠1 R OR 0-1 Y) => 2nd <br> 1st   |
|      6     |   1 Y, >1 W => 4th <br> 0 R => 6th <br> 4th   |   0 Y => 3rd <br> 1 Y, >1 W => 4th <br> 0 R => 6th <br> 4th   |

### Footnotes
- When there are 3 wires, never cut the first wire.
- When there are 5 wires, never cut the third or fifth wires.
- When there are 6 wires, never cut the first, second, or fifth wires.

#### Alternatively
- Never cut the fifth wire.
- Never cut the first wire when there are 3 or 6 (minimum or maximum).
- Never cut the third wire when there are 5 (middle wire).
- Never cut the second wire when there are 6.
