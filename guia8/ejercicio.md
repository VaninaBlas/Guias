``` python
t:tuple[int,str]
u:tuple[int,str]
t=(10,"diez")
u=t
print(u[0],u[1])
t=(20,"veinte")
print(t,u)
t[0]=30
```
El primer print muestra 10 diez, el segundo (20, "veinte") (10,"diez") y lo ultimo no se puede hacer porque las tuplas no se pueden modificar. Las tuplas no son mutables por eso tambien al modificar t no cambia u.