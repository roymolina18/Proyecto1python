# Ejemplos de la funcion print()

print("Hola mundo")
print("Hola mundo", "otra vez")
print('Son las', 9, 'de la manana')

print('El resultado de 3 * 4 es:', 3*4)

# Ejemplos de cadenas formateadas
print('El numero 15 en sistema decimal el %d, en sistema octal es %o, en el sistema hexadecimal es %x' %(15, 15, 15))

pi = 3.141592
r = 5
print(f' El radio de un circulo es{r} y el area de ese circulo es {pi * r ** 2 : .2f}')

print(' La letra beta es: \n\t \u03B2')

#Caracteres de escape
print('Hola mundo', end = ' ' ' ')
print('otra vez', end = '\t \t \t')
print(' y otra vez')
