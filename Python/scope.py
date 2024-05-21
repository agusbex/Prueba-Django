#Alcances global/local. Global: se define a nivel de modulo (pegado al margen izquierdo, todo archivo .py)

a = 5

def funcion_1():
    print(a)
    b = 10
    
funcion_1()

#print(b) no se puede porque b es local, el alcance de b es en funcion_1


#cuando escribimos variables en mayusculas, python la toma como una convencion, no es una constante en si porque se puede modificar. las torna de otro color, no DEBERIAMOS cambiar su valor
#es mejor evitarlas
PI = 3.14