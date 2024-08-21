# Receba um número inteiro na entrada e imprima (Fizz) se o número for divisível 
# por 3. Caso contrário, imprima o mesmo número que foi dado na entrada.

numero = int(input("Informe um número inteiro: "))

print("Fizz" if numero % 3 == 0 else numero)