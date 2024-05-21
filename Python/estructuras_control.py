# variables

contador = 0
print(contador)

contador += 1
contador += 1

print(contador)

# Tipado dinamico
contador = "Hola"
print(contador)

# estructuras de control

condicion = True

if condicion:
    print("la condicion es verdadera")
else:
    print("la condicion es falsa")
    
    
#for comun    
for i in range(0, 10): #incluye el 0, no incluye el 10
    print(i)
    
    
#for each
lista = ["Hola", "Si", "Adios"]

for palabra in lista:
    print(palabra)
    

condicion2 = True
contador2 = 0

while condicion2:
    contador2 += 1
    print(contador2)
    
    if contador2 > 12:
        break
print("Adios")