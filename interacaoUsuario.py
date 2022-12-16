import os


def cadastrarProduto():
    limparTela()
    print("-------- Cadastro de Produto --------")
    produto = {}
    produto['sku'] = input('SKU: ')
    produto['nome'] = input('Nome: ')
    produto['preco'] = float(input('Preço: '))
    produto['categoria'] = (input('Categoria: '))
    produto['condicao'] = (input('Condição: '))

    return produto


def editarProduto():
    limparTela()
    print("-------- Edição de Produto --------")
    produto = {}
    produto['sku'] = (input('sku: '))
    produto['nome'] = input('Nome: ')
    produto['preco'] = float(input('Preço: '))
    produto['categoria'] = (input('Categoria: '))
    produto['condicao'] = (input('Condição: '))

    return produto


def excluirProduto():
    print("-------- Exclusão de Produto --------")
    limparTela()
    sku = int(input('Código SKU: '))
    return sku


def selecionarProduto():
    limparTela()
    print("-------- Seleção de Produto --------")
    sku = int(input('Código SKU: '))
    return sku


def exibirProduto(produto):
    print("-------- Produto --------")
    print(f"sku: {produto['sku']}")
    print(f"Nome: {produto['nome']}")
    print(f"Preço: {produto['preco']}")
    print(f"Categoria: {produto['categoria']}")
    print(f"Condição: {produto['condicao']}")
    


def exibirProdutos(produtos):
    limparTela()
    print("---------------- Produtos ----------------")
    for produto in produtos:
        exibirProduto(produto)
    travarTela()


def limparTela():
    os.system('clear' if os.name == 'posix' else 'cls')


def travarTela():
    input('Pressione ENTER para continuar...')


def exibirMsg(msg):
    print(msg)
    travarTela()
