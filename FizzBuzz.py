Fizz = 0
Buzz = 0
Contador = 0
Pasada = 0
ContadorReal = []

while True:
    Fizz += 1
    Buzz += 1
    Pasada += 1
    Contador += 1

    if Fizz == 3 and Buzz == 5:  # Múltiplo de 3 y de 5
        ContadorReal.append("FizzBuzz")
        Fizz = 0
        Buzz = 0
        if Contador == 100:
            break

    elif Fizz == 3:  # Múltiplo de 3
        ContadorReal.append("Fizz")
        Fizz = 0
        if Contador == 100:
            break

    elif Buzz == 5:  # Múltiplo de 5
        ContadorReal.append("Buzz")
        Buzz = 0
        if Contador == 100:
            break

    elif Fizz != 3 and Buzz != 5:  # Múltiplo de ninguno
        ContadorReal.append(Contador)
        if Contador == 100:
            break

print(ContadorReal)

input("cerrar")
