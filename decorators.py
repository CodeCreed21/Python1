def announce(f): #Definisco una funzione che prende come valore una funzion f
    def wrapper(): #All'interno della funzione announce definisco un'altra funzione...
        print("The function is about to run...") #...che mi avvisa che sta per far partire la 
                                                 #funzione passata ad announce...
        f() #...poi gli dico che deve far partire la funzione...
        print("Done with the function") #...ed infine do il messaggio che ha finito
    return wrapper() #Restituisce il valore della nuova funzione

#Questo codice passa alla funzione announce, la funzione hello e poi restituisce il nuovo valore di hello.
@announce
def hello():
    print("Hello!!")
#hello() se lascio questa da errore di tipo non definito?????

