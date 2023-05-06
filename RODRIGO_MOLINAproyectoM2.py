# if-elif-else longitud de palabras sencillo pero hace la funcion.
palabra = input("Ingrese una palabra: ")
longitud = len(palabra)

if longitud >= 4 and longitud <= 8:
    print("La palabra es correcta.")
elif longitud < 4:
    print(f"Hacen falta letras. Solo tiene {longitud} letras.")
else:
    print(f"Sobran letras. Tiene {longitud} letras.")


#opcion 1  Cuadrante
x = float(input("Ingrese la coordenada en x del punto: "))
y = float(input("Ingrese la coordenada en y del punto: "))

if x > 0 and y > 0:
    print("El punto se encuentra en el primer cuadrante")
elif x < 0 and y > 0:
    print("El punto se encuentra en el segundo cuadrante")
elif x < 0 and y < 0:
    print("El punto se encuentra en el tercer cuadrante")
elif x > 0 and y < 0:
    print("El punto se encuentra en el cuarto cuadrante")
else:
    print("El punto se encuentra en el origen")

#opcion 2 Cuandrante
x = float(input("Ingrese X: "))
y = float(input("Ingrese Y: "))

if x == 0 or y == 0:
    print("Las coordenadas deben ser distintas de cero.")
elif x > 0 and y > 0:
    print("El punto se encuentra en el cuadrante I.")
elif x < 0 and y > 0:
    print("El punto se encuentra en el cuadrante II.")
elif x < 0 and y < 0:
    print("El punto se encuentra en el cuadrante III.")
else:
    print("El punto se encuentra en el cuadrante IV.")