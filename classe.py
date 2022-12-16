from interacaojson import lerJson, gravarJson

class Produto :
    sku : int
    nome : str
    preco : float
    categoria : str
    condicao : str

def criar(dado: dict) -> dict:
    dados = lerJson()
    dado['sku'] 
    dados.append(dado)
    gravarJson(dados)


def editar(dado: dict) -> None:
    dados = lerJson()
    for i, data in enumerate(dados):
        if data['sku'] == dado['sku']:
            dados[i] = dado
    gravarJson(dados)
    
def excluir(sku: int) -> None:
    dados = lerJson()
    for dado in dados:
        if dado['sku'] == sku:
            dados.remove(dado)
    gravarJson(dados)


def selecionar(sku: int) -> dict | None:
    dados = lerJson()
    for dado in dados:
        if dado['sku'] == sku:
            return dado
    return None


def selecionar_todos() -> list:
    return lerJson()
