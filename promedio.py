nota1 = float(input("Digite la nota 1: "))
nota2 = float(input("Digite la nota 2: "))
nota3 = float(input("Digite la nota 3: "))

promedio = (nota1 + nota2 + nota3) / 3

print("Promedio:", promedio)

if promedio >= 3:
    print("Aprobado")
else:
    print("No aprobado")
