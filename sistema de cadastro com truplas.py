class SistemaCadastroProdutos:
    def __init__(self):
        self.produtos = []
 
    def adicionar_produto(self):
        nome = input("Digite o nome do produto: ")
        preco = float(input(f"Digite o preço do produto '{nome}': R$ "))
        quantidade = int(input(f"Digite a quantidade em estoque de '{nome}': "))
        produto = (nome, preco, quantidade)  # Cria uma tupla com as informações
        self.produtos.append(produto)
        print(f"Produto '{nome}' adicionado com sucesso!\n")
 
    def exibir_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.\n")
        else:
            print("Produtos cadastrados:")
            for produto in self.produtos:
                nome, preco, quantidade = produto
                print(f"Nome: {nome}, Preço: R${preco:.2f}, Quantidade: {quantidade}")
            print()  # Linha em branco
 
def menu():
    sistema = SistemaCadastroProdutos()
    while True:
        print("Menu de Opções:")
        print("1 - Adicionar produto")
        print("2 - Exibir todos os produtos")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            sistema.adicionar_produto()
        elif opcao == "2":
            sistema.exibir_produtos()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")
 
if __name__ == "__main__":
    menu()
 