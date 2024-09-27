decrescente = True
numero = int(input("Digite o primeiro número da sequência: "))
proximoNumero = int(input("Digite o próximo número da sequência: "))

while proximoNumero != 0 and decrescente:
    if proximoNumero > numero:
        decrescente = False
        numero = proximoNumero

if decrescente:
    print("A sequência de números está em ordem decrescente!")
else:
    print("A sequência de números não está em ordem decrescente!")
    

