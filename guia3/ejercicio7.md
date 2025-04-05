## Ejercicio 7. 
Demostrar que los siguientes pares de expresiones son equivalentes, usando las propiedades conocidas (conmutatividad, asociatividad, distributividad, absorción, De Morgan, etc.):

(a) p = p ∧ (p ∨ q ∨ r) <br>
(b) p ∨ q ∨ r = ¬(¬p ∧ ¬q ∧ ¬r)<br>
(c) p ∨ ¬q = ¬((p ∨ q) ∧ ¬(¬q ∧ p) ∧ ¬(p ∧ q))<br>
(d) p ∧ q = ¬(¬p ∨ ¬q) ∨ (p ∧ q ∧ r)<br>
(e) p ∧ q = (p ∨ q) ∧ ¬(¬p ∨ ¬q)<br>
(f) ¬p ∧ ¬q ∧ r = (¬p ∨ q ∨ r) ∧ ¬(p ∨ q ∨ ¬r)

(a) p = p ∧ (p ∨ q ∨ r)

p ∧ (p ∨ q ∨ r) ≡ distributividad <br>
(p ∧ p) V ( p ∧ q) V (p ∧ r) ≡ Idempotencia <br>
p V (p ∧ q) V (p ∧ r) ≡ Distributividad <br>
p V (p ∧ (q V r)) ≡ Absorcion <br>
**p**

(b) p ∨ q ∨ r = ¬(¬p ∧ ¬q ∧ ¬r)

¬(¬p ∧ ¬q ∧ ¬r) ≡ de Morgan <br>
¬¬p V ¬¬q V ¬¬r ≡ doble negacion <br>
p V q V r

(c) p ∨ ¬q = ¬((p ∨ q) ∧ ¬(¬q ∧ p) ∧ ¬(p ∧ q))

¬((p ∨ q) ∧ ¬(¬q ∧ p) ∧ ¬(p ∧ q)) ≡ de Morgan, dos veces <br>

¬((p ∨ q) ∧ (¬¬q V ¬p) ∧ (¬p V ¬q)) ≡ doble negacion<br>
¬((p ∨ q) ∧ (q V ¬p) ∧ (¬p V ¬q)) ≡ conmutativa<br>
¬((p ∨ q) ∧ (¬p V q) ∧ (¬p V ¬q)) ≡ distributividad<br>
¬((p ∨ q) ∧ (¬p V ( q ∧ ¬q))) ≡ inverso<br>
¬((p ∨ q) ∧ (¬p V F)) ≡ identidad<br>
¬((p ∨ q) ∧ ¬p) ≡ de morgan<br>
¬(p ∨ q) ∧ ¬¬p ≡ de morgan<br>
(¬p ∧ ¬q) V ¬¬p ≡ doble negacion<br>
(¬p ∧ ¬q) V p ≡ ditributividad<br>
(p V ¬p) ∧ (p V ¬q) ≡ inverso<br>
V  ∧ (p V ¬q) ≡ identidad<br>
p V ¬q

(d) p ∧ q = ¬(¬p ∨ ¬q) ∨ (p ∧ q ∧ r)

¬(¬p ∨ ¬q) ∨ (p ∧ q ∧ r) ≡ de morgan <br>
(¬¬p ∧ ¬¬q) ∨ (p ∧ q ∧ r) ≡ doble negacion<br>
(p ∧ q) ∨ (p ∧ q ∧ r) ≡ absorcion<br>
p ∧ q

(e) p ∧ q = (p ∨ q) ∧ ¬(¬p ∨ ¬q)

(p ∨ q) ∧ ¬(¬p ∨ ¬q) ≡ de morgan<br>
(p ∨ q) ∧ (¬¬p ∧ ¬¬q) ≡ doble negacion<br>
(p ∨ q) ∧ (p ∧ q) ≡ distributividad<br>
(((p V q) ∧ p) ∧ ((p V q) ∧ q)) ≡ absorcion<br>
p ∧ q

(f) ¬p ∧ ¬q ∧ r = (¬p ∨ q ∨ r) ∧ ¬(p ∨ q ∨ ¬r)

(¬p ∨ q ∨ r) ∧ ¬(p ∨ q ∨ ¬r) ≡ de morgan
(¬p ∨ q ∨ r) ∧ (¬p ∧ ¬q ∧ ¬¬r) ≡ doble negacion

(¬p ∨ q ∨ r) ∧ (¬p ∧ ¬q ∧ r) ≡ distributividad

((¬p ∨ q ∨ r)∧ ¬p)  ∧ ((¬p ∨ q ∨ r) ∧ ¬q) ∧ ((¬p ∨ q ∨ r)∧ r) ≡ absorcion triple
¬p ∧ ¬q ∧ r
