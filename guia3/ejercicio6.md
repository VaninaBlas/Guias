## Ejercicio 6. 
Demostrar las siguientes propiedades usando tablas de verdad:

(a) (p ∧ q) ∧ r = p ∧ (q ∧ r) (asociatividad)

(b) p ∧ (q ∨ r) = (p ∧ q) ∨ (p ∧ r) (distributividad)

(c) p ∨ (p ∧ q) = p (absorción)

(d) p ∧ (p ∨ q) = p (absorción)

(e) ¬(p ∨ q) = ¬p ∧ ¬q (De Morgan)

<br>
(a) (p ∧ q) ∧ r = p ∧ (q ∧ r) (asociatividad)

| p | q | r| p ∧ q | (p ∧ q) ∧ r | q ∧ r | p ∧ (q ∧ r)
|----------|----------|----------|----------|----------|----------|----------|
| V| V  | V   |V | V |V |V
| V| V   |F   | V| F|F|F
| V | F  |V  | F|F|F|F
| V | F  |F  | F|F|F|F
| F | V  |V  |F| F|V|F
| F | V  |F  |F| F|F|F
| F | F  |V  |F| F|F|F
| F | F  |F  |F| F|F|F

| (p ∧ q) ∧ r | p ∧ (q ∧ r) | 
|----------|----------|
| V    | V   | 
| F    | F   |
| F    | F   | 
| F    | F   | 
| F    | F   | 
| F    | F   | 
| F    | F   | 
| F    | F   | 

**son iguales**

(b) p ∧ (q ∨ r) = (p ∧ q) ∨ (p ∧ r) (distributividad)

| p | q | r| q ∨ r | p ∧ (q ∨ r)| p ∧ q | p ∧ r|(p ∧ q) ∨ (p ∧ r)
|----------|----------|----------|----------|----------|----------|----------|----------|
| V| V  | V   | V| V |V |V|V
| V| V   |F   | V| V|V|F|V
| V | F  |V  | V|V|F|V|V
| V | F  |F  | F|F|F|F|F
| F | V  |V  |V| F|F|F|F
| F | V  |F  |V| F|F|F|F
| F | F  |V  |V| F|F|F|F
| F | F  |F  |F| F|F|F|F

| p ∧ (q ∨ r) | (p ∧ q) ∨ (p ∧ r)  | 
|----------|----------|
| V    | V   | 
| V    | V   |
| V    | V   | 
| F    | F   | 
| F    | F   | 
| F    | F   | 
| F    | F   | 
| F    | F   | 

**son iguales**

(c) p ∨ (p ∧ q) = p (absorción)


| p | q |  p ∧ q | p ∨ (p ∧ q) |
|----------|----------|----------|----------|
| V| V  |    V | V |
| V| F   |   F| V|
| F | V  | F|F|
| F | F  | F|F|


| p ∨ (p ∧ q)| p | 
|----------|----------|
| V    | V   | 
| V    | V   |
| F    | F   | 
| F    | F   | 


**son iguales**

(d) p ∧ (p ∨ q) = p (absorción)

| p | q |p ∨ q | p ∧ (p ∨ q) |
|----------|----------|----------|----------|
| V| V  |  V| V |
| V| F   |V| V|
| F | V  |V|F|
| F | F  |F|F|


| p ∧ (p ∨ q)| p | 
|----------|----------|
| V    | V   | 
| V    | V   |
| F    | F   | 
| F    | F   | 


**son iguales**

(e) ¬(p ∨ q) = ¬p ∧ ¬q (De Morgan)

| p | q |p ∨ q | ¬(p ∨ q)| ¬p| ¬q|¬p ∧ ¬q
|----------|----------|----------|----------|----------|----------|----------|
| V| V  | V| F| F| F|F
| V| F   | V| F| F| V|F
| F | V  | V| F| V| F|F
| F | F  | F| V| V| V|V  

| p ∧ (p ∨ q)| p | 
|----------|----------|
| F    | F   | 
| F    | F   |
| F    | F   | 
| V    | V   | 