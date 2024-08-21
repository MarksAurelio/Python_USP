# Receba um número inteiro na entrada e imprima (Buzz) se o número for divisível 
# por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.

numero = int(input("Informe um número inteiro: "))

print("Buzz" if numero % 5 == 0 else numero)