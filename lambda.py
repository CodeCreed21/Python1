#Creo una lista di dictionaries, in python si puo' fare una lista con qualunque elemento
people= [
{"name":"Harry","House": "Grifondoro"},
{"name":"Ginny","House": "Tassorosso"},
{"name":"Draco","House": "Serpeverde"},
]
#Python non sa come comparare i dizionari...per ovviare al problema definisco una funzione che dice come 
# voglio fare il sort della lista...ad esempio per nome 
def f(person):
    return person["name"]
#Poi voglio fare il sort della lista e stamparla...ma..
#...ricevo errore -- type error '<' not supported between instances of 'dict' and 'dict' -- 
# quindi aggiungo prima la definizione di una funzione che dice per quale attributo voglio fare sort e poi..

#people.sort(key=f) #prendi people e fai il sort...come? Utilizzando la funzione f

people.sort(key=lambda person:person["name"]) #posso dirlo cosi prendi in imput person e 
                                               #restituisci il sort del nome 

print(people)



