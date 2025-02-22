# # 1. Triángulo de números
# def triangulo_numeros(n):
#     for i in range(1, n+1):
#         print(" ".join(str(j) for j in range(1, i+1)))

# triangulo_numeros(4)

# # 2. Multiplicación usando solo sumas
# def multiplicar(a, b):
#     resultado = 0
#     for _ in range(abs(b)):
#         resultado += abs(a)
#     if (a < 0 and b > 0) or (a > 0 and b < 0):
#         resultado = -resultado
#     return resultado

# print(multiplicar(3, 4))

# # 3. División usando solo restas
# def dividir(a, b):
#     if b == 0:
#         raise ValueError("No se puede dividir por cero")
    
#     contador = 0
#     negativo = (a < 0) != (b < 0)
#     a, b = abs(a), abs(b)

#     while a >= b:
#         a -= b
#         contador += 1

#     return -contador if negativo else contador

# print(dividir(10, 2))
# print(dividir(10, -2))