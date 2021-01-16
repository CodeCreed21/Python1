#Si puo' importare solo la funzione che ci interessa, da un modulo specifico
from functions import square

for i in range(10):
    print(f"Il quadrato di {i} e' {square(i)}")  

#Oppure importare tutto il modulo
import functions

for i in range(10):
    print(f"Il doppio del quadrato di {i} e' {functions.square2(i)}") #e poi specificare quale funzione del modulo si vuole usare

