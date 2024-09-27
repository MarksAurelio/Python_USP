meuCartao = int(input("Digite o número do seu cartão de crédito: "))

cartaoLido = None
encontreiMeuCartaoNaLista = False

while cartaoLido != 0 and not encontreiMeuCartaoNaLista:
    cartaoLido = int(input("Digite o número do próximo cartão de crédito: "))
    if cartaoLido == meuCartao:
        encontreiMeuCartaoNaLista = True

if encontreiMeuCartaoNaLista:
    print("Eba!!! Meu cartão está lá!")
else:
    print("Xi, meu cartão não está lá...")
