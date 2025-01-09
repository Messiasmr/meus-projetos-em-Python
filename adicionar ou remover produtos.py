class Produto:
    def __init__(self, nome, quantidade, preco_unitario):
        self.nome = nome
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
 
    def atualizar_quantidade(self, nova_quantidade):
        self.quantidade = nova_quantidade
 
    def __str__(self):
        return f"Nome: {self.nome}, Quantidade: {self.quantidade}, Preço Unitário: R${self.preco_unitario:.2f}"
 
class Estoque:
    def __init__(self):
        self.produtos = []
 
    def adicionar_produto(self):
        nome = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade do produto: "))
        preco_unitario = float(input("Digite o preço unitário do produto: "))
        produto = Produto(nome, quantidade, preco_unitario)
        self.produtos.append(produto)
        print(f"Produto '{nome}' adicionado com sucesso!\n")
 
    def atualizar_quantidade(self):
        nome = input("Digite o nome do produto a ser atualizado: ")
        for produto in self.produtos:
            if produto.nome == nome:
                nova_quantidade = int(input(f"Digite a nova quantidade para o produto '{nome}': "))
                produto.atualizar_quantidade(nova_quantidade)
                print(f"Quantidade do produto '{nome}' atualizada para {nova_quantidade}.\n")
                return
        print(f"Produto '{nome}' não encontrado.\n")
 
    def remover_produto(self):
        nome = input("Digite o nome do produto a ser removido: ")
        for produto in self.produtos:
            if produto.nome == nome:
                self.produtos.remove(produto)
                print(f"Produto '{nome}' removido com sucesso!\n")
                return
        print(f"Produto '{nome}' não encontrado.\n")
 
    def exibir_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado no estoque.\n")
        else:
            print("Produtos cadastrados:")
            for produto in self.produtos:
                print(produto)
            print()  # Linha em branco
 
def menu():
    estoque = Estoque()
    while True:
        print("Menu de Opções:")
        print("1 - Adicionar produto")
        print("2 - Atualizar quantidade de produto")
        print("3 - Remover produto")
        print("4 - Exibir todos os produtos")
        print("5 - Sair")
       
        opcao = input("Escolha uma opção: ")
       
        if opcao == '1':
            estoque.adicionar_produto()
        elif opcao == '2':
            estoque.atualizar_quantidade()
        elif opcao == '3':
            estoque.remover_produto()
        elif opcao == '4':
            estoque.exibir_produtos()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")
 
if __name__ == "__main__":
    menu()
 