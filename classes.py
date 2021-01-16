class Flight(): #si definisce la classe Flight
    def __init__(self,capacity): #Si inizializza dichiarando quanti argomenti  verrsanno passati...in questo caso 1, il numero di passeggeri max che puo' ospitare il volo
        self.capacity=capacity #si setta la proprieta' capacity, nell'oggetto self, con il alore che avra' l'argomento capacity
        self.passengers=[] #si setta la proprieta' passengers, nell'oggetto self, come lista vuota (verra' riempita poi passando i valori alla funzione)

    def add_passenger(self, name): #Definisco anche una funzione che mi permetta di aggiungere passeggeri tramite il nome
        if not self.open_seats():
            return False  
        self.passengers.append(name) #do accesso all'oggetto self e dico di mettere il valore name passato alla funzione, in fondo alla lista passengers 
        return True

    def open_seats(self): #Definisco una funzione a cui non passo argomenti, che mi dica se ci sono posti liberi...
        return self.capacity-len(self.passengers) #..e che restituisce come valore la differenza tra il numero di elementi all'interno della lista passengers e il valore in capacity

flight=Flight(3) #Definisco variabile flight in cui si mette il valore passato dalla funzione Flight() di max 3 passeggeri
people=["Harry","Ermione","Ron","Ginny","Draco"] #Creo la lista di passeggeri in people

for person in people: #Per ogni elemento nella lista people...
    if flight.add_passenger(person): #se l'inserimento del passefggero ha successo, cioe' se c'e' ancora spazio sul volo...
        print(f"Added the passenger {person} to the flight sucessfully") #restituisci messaggio
    else:
        print(f"Spiacente, ma non c'e' posto per {person}")  #...altrimenti restituisci questo messaggio


