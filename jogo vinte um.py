import random

# Função para embaralhar o baralho
def embaralhar_baralho():
    baralho = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4  # 4 naipes
    random.shuffle(baralho)
    return baralho

# Função para calcular o valor da mão
def calcular_valor(mao):
    valor = 0
    ases = 0
    for carta in mao:
        if carta in ['J', 'Q', 'K']:
            valor += 10
        elif carta == 'A':
            valor += 11
            ases += 1
        else:
            valor += int(carta)
    while valor > 21 and ases:
        valor -= 10
        ases -= 1
    return valor

# Função para pedir uma carta do baralho
def pedir_carta(baralho, mao):
    carta = baralho.pop()
    mao.append(carta)
    return carta

# Função para mostrar a mão e o valor
def mostrar_mao(mao, jogador):
    print(f"Mão do {jogador}: {', '.join(mao)} (Valor: {calcular_valor(mao)})")

# Função principal do jogo
def jogar_vinte_um():
    baralho = embaralhar_baralho()
    mao_jogador = []
    mao_dealer = []

    # Jogador e Dealer recebem duas cartas
    for _ in range(2):
        pedir_carta(baralho, mao_jogador)
        pedir_carta(baralho, mao_dealer)

    # Mostrar mãos iniciais
    mostrar_mao(mao_jogador, "Jogador")
    print(f"Mão do Dealer: {mao_dealer[0]}, ?")

    # Jogador joga
    while True:
        if calcular_valor(mao_jogador) >= 21:
            break
        acao = input("Você quer pedir uma carta (p) ou parar (s)? ")
        if acao.lower() == 'p':
            carta = pedir_carta(baralho, mao_jogador)
            print(f"Você pediu: {carta}")
            mostrar_mao(mao_jogador, "Jogador")
        elif acao.lower() == 's':
            break

    # Se o jogador estourar
    if calcular_valor(mao_jogador) > 21:
        print("Você estourou! Dealer venceu.")
        return

    # Dealer joga
    while calcular_valor(mao_dealer) < 17:
        carta = pedir_carta(baralho, mao_dealer)
        print(f"Dealer pediu: {carta}")

    # Mostrar mãos finais
    mostrar_mao(mao_dealer, "Dealer")

    # Determinar o vencedor
    valor_jogador = calcular_valor(mao_jogador)
    valor_dealer = calcular_valor(mao_dealer)

    if valor_dealer > 21 or valor_jogador > valor_dealer:
        print("Parabéns, você venceu!")
    elif valor_jogador == valor_dealer:
        print("Empate!")
    else:
        print("Dealer venceu!")

# Iniciar o jogo
if __name__ == "__main__":
    jogar_vinte_um()
