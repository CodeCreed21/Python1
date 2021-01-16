#Scorrere una lista di numeri e stamparli uno alla volta finch'e' la lista non e' finita
for i in [0,1,2,3,4,5]:
    print(i)

#Qui viene dato un range di 6 numeri da stampare. Con il range gli elementi sono indicizzati per cui parte a contare da 0
for i in range(6):
    print(i)  


#Lavorando con liste si puo' fare la stessa cosa
names=["Harry","Ermione","Ron"]

for name in names:
    print(name)

#Si puo' lavorare anche sulla singola stringa    

name="Harry"

for character in name:
    print(character)