## Ejercicio 5. 
Representar los siguientes enunciados en lógica proposicional, usando las variables indicadas:

(a) Si p: “María aprobó Plástica”, q: “María aprobó Química”:

(I) “María aprobó Plástica y Química”.

(II) “María aprobó Plástica, pero no aprobó Química”.

(III) “María aprobó exactamente una de las dos materias”.

(b) Si p: “Pedro juega al paddle”, t: “Pedro juega al tenis”, r: “Pedro juega al rugby”:

(I) “Pedro juega al paddle, al tenis y al rugby”.

(II) “Pedro juega al paddle, pero no al tenis ni al rugby”.

(III) “Pedro no juega al paddle, pero sí juega al tenis y al rugby”.

(IV) “Pedro no juega al paddle, ni al tenis, ni al rugby”.

(V) “Pedro juega a exactamente uno de esos tres deportes (juega solamente al paddle, o bien juega solamente al tenis, o bien juega solamente al rugby).”

(VI) “Pedro juega a exactamente dos de esos tres deportes.”

(a)

(I) p ∧ q

(II) p ∧ ¬q

(III) (p∨q) ∧ ¬(p∧q) / (aprobo alguna de las dos) ∧ (no aprobo ambas)

(III) (p∧ -q) V (-p ∧ q )

| p | q | III| caso| 
|----------|----------|----------|----------|
| V| V  |  ❌ aprobo ambas  | - |
| V| F   |  ✔️ | p ∧ -q  | 
| F | V  | ✔️ | -p ∧ q| 
| F | F  | ❌ | - |


(b)

(I) p ∧ t ∧ r

(II) p ∧ ¬t ∧ ¬r

(III) ¬p ∧ t ∧ r

(IV) ¬p ∧ ¬t ∧ ¬r o ¬(p ∨ t ∨ r)

(V) (p ∧ ¬t ∧ ¬r) ∨ (¬p ∧ t ∧ ¬r) ∨ (¬p ∧ ¬t ∧ r)

| p | t | r| V| caso |
|----------|----------|----------|----------|----------|
| V| V  | V   | ❌ juegan los 3|-
| V| V   |F   | ❌ | -
| V | F  |V  | ❌| -
| V | F  |F  |✔️ | p ∧ -t ∧ -r
| F | V  |V  |❌| -
| F | V  |F  |✔️| -p ∧ t ∧ -r
| F | F  |V  |✔️| -p ∧ -t ∧ r
| F | F  |F  |❌| -

(VI) (p ∧ t ∧ ¬r) ∨ (¬p ∧ t ∧ r) ∨ (p ∧ ¬t ∧ r)

| p | t | r| VI| caso |
|----------|----------|----------|----------|----------|
| V| V  | V   | ❌ juegan los 3|-
| V| V   |F   |✔️ | p ∧ t ∧ -r
| V | F  |V  |✔️ | p ∧ -t ∧ r
| V | F  |F  |❌ | -
| F | V  |V  |✔️| -p ∧ t ∧ r
| F | V  |F  |❌| -
| F | F  |V  |❌| -
| F | F  |F  |❌| -



