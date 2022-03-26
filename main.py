"""
Escriba un programa que pregunte cuantos numeros se
van a introducir,permita el ingreso de dichos numeros y
muestrepor pantalla cuantos numeros pares y la suma de
todos los impares.
"""
veces=int(input("¿cuantos numeros desea ingresar?"))
cont=0
acum=0
for i in range(veces):
    print("---Ciclo ",str(i+1)+"---")
    num=int(input("Ingrese un numero: "))
    if num%2==0:
        cont+=1

    else:
        acum+=num
print("La cantidad de numeros pares es:",cont)
print("La suma de numeros impares es:", acum)