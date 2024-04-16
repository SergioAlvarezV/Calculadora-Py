import operadores
def user_input():
  operadores = ('Sumar', 'Restar', 'Multiplicar', 'Dividir')
  user_options = input('Que quiere hacer Sumar, restar, multiplicar o dividir ')
  user_options = user_options.capitalize()
  if user_options not in operadores:
    print('Esa operador no esta en las opciones')
    return None,None
  
  return user_options

def operacioness(next,user_options):
  if user_options == 'Sumar':
    v1 = input('ingrese el primer valor: ')
    v2 = input('ingrese el segundo valor: ')
    v1 = int(v1)
    v2 = int(v2)
    print(f'la suma de {v1} + {v2} es', operadores.suma(v1, v2))
    next = input('Quiere hacer otra opercion Si o No => ')
    next = str(next)
    next = next.capitalize()
     
  elif user_options == 'Restar':
    v1 = input('ingrese el primer valor: ')
    v2 = input('ingrese el segundo valor: ')
    v1 = int(v1)
    v2 = int(v2)
    print(f'la resta de {v1} - {v2} es', operadores.resta(v1, v2))
    next = input('Quiere hacer otra opercion Si o No => ')
    next = str(next)
    next = next.capitalize()
  
  elif user_options == 'Multiplicar':
    v1 = input('ingrese el primer valor: ')
    v2 = input('ingrese el segundo valor: ')
    v1 = int(v1)
    v2 = int(v2)
    print(f'{v1} x {v2} es igual a ',operadores.multiplicacion(v1, v2))
    next = input('Quiere hacer otra opercion Si o No => ')
    next = str(next)
    next = next.capitalize()
  
  elif user_options == 'Dividir':
    v1 = input('ingrese el primer valor: ')
    v2 = input('ingrese el segundo valor: ')
    v1 = int(v1)
    v2 = int(v2)
    v3 = int(operadores.divicion(v1, v2))
    print(f'{v1} / {v2} es igual a ', v3)
    next = input('Quiere hacer otra opercion Si o No => ')
    next = str(next)
    next = next.capitalize()
  return next

def run():
  next = "Si"
  while True:
    user_options = user_input()
    next = operacioness(next,user_options)
    if next == 'No':
      print('Nos vemos Babay')
      break

      



run()
 