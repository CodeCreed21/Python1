#Prima di tutto si crea il set vuoto. attribuendolo ad una variabile

s=set()

#Add some elements to the set

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3) #questo elemento non verra' ripetuto perche' nei sets non vengono ripetuti elementi esistenti
print(s)

s.remove(2)
print(s)
print(f"La nuova lista ha {len(s)} elemnti.")

