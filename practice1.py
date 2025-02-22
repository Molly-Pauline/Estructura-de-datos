# nombre = "molly"
# edad = 19
# estatura = 1.62
# print(f"hola, me llamo {nombre}, tengo {edad} y mido {estatura}")

# a = 10
# b = 20
# c = b+a
# d = b-a
# e = b*a
# f = round (b/a, 2)
# print(f"el resultado de las operaciones de los dos valores es: suma {c}, resta {d}, multiplicación {e} y división {f}.")

# numero = 6
# if numero % 2 == 0:
#     print ("es un numero par")
# else:
#     print ("es un numero impar")



# Ejercicio 1: Número positivo, negativo o cero
# 📌 Instrucciones:
# Escribe un programa que lea un número y verifique si es:

# Positivo (mayor que 0)
# Negativo (menor que 0)
# Cero (igual a 0)
# 🔹 Ejemplo de entrada: 5
# 🔹 Salida esperada: "El número es positivo"

# solucion

# numero = int(input ("ingrese un numero"))
# if numero > 0:
#     print ("el numero es positivo")
# elif numero < 0:
#     print ("el numero es negativo")
# else:
#     print ("el numero es igual a 0")



# Ejercicio 2: Determinar si un año es bisiesto
# 📌 Instrucciones:
# Un año es bisiesto si cumple las siguientes reglas:

# Es divisible entre 4
# No es divisible entre 100, a menos que también sea divisible entre 400
# Escribe un programa que determine si un año es bisiesto.

# 🔹 Ejemplo de entrada: 2024
# 🔹 Salida esperada: "El año 2024 es bisiesto"

# Solucion

# year = int (input("enter a year: "))
# if year % 400 == 0:
#     print (f"the year {year} is a leap year")
# elif year % 100 == 0:
#     print (f"the year {year} isn't a leap year")
# elif year % 4 == 0:
#     print (f"the year {year} is a leap year")
# else:
#      print (f"the year {year} isn't a leap year")


# Ejercicio 3: Calculadora de descuentos
# 📌 Instrucciones:
# Un comercio ofrece descuentos según el monto de compra:

# Menos de $50: No hay descuento.
# Entre $50 y $100: 10% de descuento.
# Más de $100: 20% de descuento.
# El programa debe calcular el monto final que debe pagar el cliente.

# 🔹 Ejemplo de entrada: $120
# 🔹 Salida esperada: "Total a pagar con descuento: $96"

# solución

# x = int (input("ingrese el valor de su compra: "))
# a = x * 0.1
# b = x * 0.2
# c = x - a
# d = x - b
# if x < 50:
#     print (f"el valor de su compra es de ${x}, por ende no tiene descuento")
# elif x >= 50 and x < 100:
#     print (f"el valor de su compra es de ${x}, por ende su descuento es del 10%, se descontará de su factura ${a}, el valor a pagar es de ${c}")
# else:
#     print (f"el valor de su compra es de $ {x}, por ende su descuento es del 20%, se descontará de su factura ${b}, el valor a pagar es de ${d}")

#  corrección CGPT   

# x = float(input("Ingrese el valor de su compra: "))

# if x < 50:
#     print(f"El valor de su compra es de ${x:.2f}, por ende, no tiene descuento.")
# elif x < 100:
#     descuento = x * 0.1
#     total = x - descuento
#     print(f"El valor de su compra es de ${x:.2f}. Se aplica un 10% de descuento (${descuento:.2f}). Total a pagar: ${total:.2f}.")
# else:
#     descuento = x * 0.2
#     total = x - descuento
#     print(f"El valor de su compra es de ${x:.2f}. Se aplica un 20% de descuento (${descuento:.2f}). Total a pagar: ${total:.2f}.")


# Ejercicio 1: Verificación de contraseña 🔐
# Pide al usuario que ingrese una contraseña y verifica si coincide con una contraseña predefinida.

# Si coincide, muestra "Acceso concedido".
# Si no, muestra "Contraseña incorrecta. Inténtalo de nuevo".

# solucion

# pasword = input("ingrese su contraseña")
# if pasword == "1234567":
#     print ("acceso exitoso")
# else:
#     print ("contraseña incorrecta, intente otra vez")


