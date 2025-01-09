def adicionar_valor(display, valor):
    return display + valor

def limpar():
    return ""

def calcular(display):
    try:
        resultado = eval(display)
        return str(resultado)
    except Exception as e:
        return "Erro"

def main():
    display = ""
    while True:
        print("\nDisplay:", display)
        print("Escolha uma opção:")
        print("1. Adicionar valor")
        print("2. Limpar")
        print("3. Calcular")
        print("4. Sair")
        
        escolha = input("Opção: ")
        
        if escolha == "1":
            valor = input("Digite o valor: ")
            display = adicionar_valor(display, valor)
        elif escolha == "2":
            display = limpar()
        elif escolha == "3":
            display = calcular(display)
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
