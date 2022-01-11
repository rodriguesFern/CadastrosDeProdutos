

def exibir_menu(): #definindo a função de menu que mais para frente será requisitada
    print('''----------------------------------------
           Escolha uma opção:
    
1 - NOVO CADASTRO.
2 - EXIBIR CADASTROS.
3 - BUSCAR CADASTRO.
----------------------------------------''')

def cadastrar(produtos): #definindo a função de cadastro de produtos
    nome = input('NOME:  ') #definindo a variavel do nome do produto
    qnt = int(input('QUANTIDADE: ')) #definindo a variavel do nome do produto
    cod = int(input('CODIGO: '))

    produtos.append((nome, qnt, cod)) #gravou as informações escritas


def listar(produtos): #definindo a função de listagem de produtos
    for produto in produtos: #produto e a variavel que e chamada na linha de baixo
        nome, qnt, cod = produto #as trea variaveis juntas se tornam 1 produto
    print(f'''  
NOME DO PRODUTO: {nome}
QUANTIDADE: {qnt}
CÓDIGO DO PRODUTO: {cod}''')

def buscar(produtos): #definindo a função de busca de produtos
    cod_busca = input('INSIRA O CÓDIGO DO PRODUTO:  ')
    for produto in produtos: #o produto dentre os produtos cadastrados
        nome, qnt, cod = produto #as tres variaveis resultam em uma so que seria a produto

        if cod_busca == cod: #se tiver um codigo de busca for igual ao digitado
            print(f'''  
NOME DO PRODUTO: {nome}
QUANTIDADE: {qnt}
CÓDIGO DO PRODUTO: {cod}''')
            break #parar o codigo
    else: #se nao gouver um codigo igual o digitado, mandar a mensagem abaixo
        print(f'Código {cod_busca} não encontrado!')

def excluir (produtos):
    cod_prod = input('INSIRA O CODIDO DO PRODUTO :')
    for produto in produtos:
        nome,qnt, cod = produto
        

def main(): #funcao main, tecnicamente a principal
    produtos = [] #em branco pois ja temos a lista




    while True:
        exibir_menu()
        opcao = int(input('OPÇÃO DESEJADA: '))
        if opcao == 1:
            cadastrar(produtos)
        elif opcao == 2:
            listar(produtos)
        elif opcao == 3:
            buscar(produtos)
        else:
            print('Opção inválida')

main()