``` python
def agregar1(x:str,c:set[str]):
    c.add(x)
def agregar2(x:str,c:set[str])->set[str]:
    r:set[str]= c | {x}
    return r
conjunto:set[str]=set()
agregar1("a", conjunto)
print(conjunto)

otro:set[str]=conjunto
agregar1("b", otro)
print(conjunto,otro)

otro=agregar2("c", otro)
print(conjunto, otro)

agregar1("d",conjunto)
print(conjunto,otro)
```
Los valores vienen sin un orden
En el primer print se ejecuta {"a"}
En el segundo print se ejecuta {"a","b"} {"a","b"}
En el tercer print se ejecuta {"a","b"} {"a","b","c"}
En el cuarto print se ejecuta {"a","b","d"} {"a","b","c"}

Cuando se reasigna otro con el valor retornado de agregar2 deja de ser dependiente de conjunto.
