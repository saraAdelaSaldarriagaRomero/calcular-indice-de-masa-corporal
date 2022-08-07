# CALCULAR INDICE DE MASA CORPORAL

# IMC = peso /(Altura *Altura)


peso = float(input('Ingrese su peso en kg'))
altura= float(input('Ingrese su altura en Metros'))


imc = peso / (altura * altura)

print('Su IMC es de' + str(imc))

if imc < 18.5:
    print('Bajo peso')

if imc > 18.5 and imc < 24.9:
    print('Peso normal')

if imc > 25.0 and imc < 29.9:
    print('Sobrepeso')

if imc >30.0 and imc < 34.9:
    print('Obesidad grado 1')

if imc > 34.9 and imc < 39.9:
    print('Obesidad grado 2')

if imc > 40.0:
    print('Obesidad Morbida')

