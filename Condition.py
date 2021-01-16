n=int(input("Insert a value: ")) #si forza il valore inserito a integer, perche' la funzione input non sa che cosa inserisci quindi considera tutto string

if n>0:
    print("n is positive")
elif n<0:
    print("n is negative")    
else:
    print("n is 0")    