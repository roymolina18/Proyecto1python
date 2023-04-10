# Pedir informacion del usuario

nombre = input("Ingresa tu nombre: ")
apellido_paterno = input("Ingresa tu apellido paterno: ")
apellido_materno = input("Ingresa tu apellido materno: ")

# Asegurarse de que la edad, peso y estatura sean numeros

while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        peso = float(input("Ingresa tu peso en kg: "))
        estatura = float(input("Ingresa tu estatura en metros: "))
        break
    except ValueError:
        print("Debes introducir un numero valido.")

# calcular el IMC

imc = peso / (estatura ** 2)

#imprimir la informacion personal y el IMC

print("\nTu informacion personal es:")
print(f"Nombre: {nombre}")
print(f"Apellido paterno: {apellido_paterno}")
print(f"Apellido materno: {apellido_materno}")
print(f"Edad: {edad}")
print(f"Peso: {peso} kg")
print(f"Estatura: {estatura} m")
print(f"Tu indice de masa corporal es: {imc:.2f}")