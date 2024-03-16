import operadores
operador = input('Que quieres hacer Sumar, Restar, Multiplicar o Dividir: ')
operador = operador.capitalize()

if operador == 'Sumar':
    v1 = input('ingrese el primer valor => ')
    v2 = input('ingrese el segundo valor => ')
    v1 = int(v1)
    v2 = int(v2)
    print(operadores.suma(v1,v2))

elif operador == 'Restar':
    v1 = input('ingrese el primer valor => ')
    v2 = input('ingrese el segundo valor => ')
    v1 = int(v1)
    v2 = int(v2)
    print(operadores.resta(v1,v2))

elif operador == 'Multiplicar':
    v1 = input('ingrese el primer valor => ')
    v2 = input('ingrese el segundo valor => ')
    v1 = int(v1)
    v2 = int(v2)
    print(operadores.multiplicacion(v1,v2))

elif operador == 'Dividir':
    v1 = input('ingrese el primer valor => ')
    v2 = input('ingrese el segundo valor => ')
    v1 = int(v1)
    v2 = int(v2)
    print(operadores.divicion(v1,v2))
 