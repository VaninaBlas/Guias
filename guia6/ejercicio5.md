(a) Dada:<br>
 
xs:list[int] = [10,11,12,13,14,15,16,17,18,19]<br>

Determinar a mano el valor
de las siguientes expresiones. Después revisar las respuestas en Python.

***xs[start:stop:step]***
<br>
| expresiones | output | 
|----------|----------|
| xs[3:7]    | [13,14,15,16]   | 
| xs[3:]    | [13,14,15,16,17,18,19]   |
| xs[:3]    | [10,11,12]   | 
| xs[:]    | [10,11,12,13,14,15,16,17,18,19]   | 
| xs[3:-2]    | [13,14,15,16,17]   | 
| xs[-7:7]    | [13,14,15,16]   | 
| xs[-5:]    | [15,16,17,18,19]   | 
| xs[:-5]    | [10,11,12,13,14]   | 
| xs[::-1]    | [19,18,17,16,15,14,13,12,11,10]   | 
| xs[1:8:-2]    | []   | 
| xs[8:1:-2]   | [18,16,14,12]   | 
| xs[::]    | [10,11,12,13,14,15,16,17,18,19]   | 
<br>

(b) Evaluar las expresiones del punto anterior, suponiendo ahora que:<br>

 xs:str = 'abcdefghij'<br>

| expresiones | output | 
|----------|----------|
| xs[3:7]    | defg   | 
| xs[3:]    | defghij   |
| xs[:3]    | abc   | 
| xs[:]    | abcdefghij   | 
| xs[3:-2]    | defgh   | 
| xs[-7:7]    | defg   | 
| xs[-5:]    | fghij   | 
| xs[:-5]    | abcde   | 
| xs[::-1]    | jihgfedcba   | 
| xs[1:8:-2]    |  ""  | 
| xs[8:1:-2]   | igec   | 
| xs[::]    | abcdefghij   | 