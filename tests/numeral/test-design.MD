# The design of test case

## Base case
    มีทั้งหมด 7 แบบคือ I, V, X, L, C, D, M

## Boundary Value condition
    1.Min case. 1 | I
    2.Max case. 3,999 | MMMCMXCIX

## 1st approach
### Addition case
2 | II
3 | III
6 | VI
7 | VII

### Subtraction case
4 | IV
9 | IX
40 | XL
49 | IL
99 | IC

### Mixed case
24 | XXIV
42 | XLII

## 2nd approach
### Unit case
1 | I
2 | II
3 | III
4 | IV
5 | V
6 | VI
7 | VII
8 | VIII
9 | IX

### Tens case
10 | X
11 | XI
12 | XII

### Hundreds case
100 | C
120 | CXX

### Thousand case
1000 | M
1342 | MCCCXLII