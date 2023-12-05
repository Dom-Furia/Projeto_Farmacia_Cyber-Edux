import  sqlite3

conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS
produto (id INTEGER PRIMARY KEY,
         nome TEXT,
         qtd INTEGER,
         preco REAL
        )''')
conexao.commit()


def exibir():
    cursor.execute('''SELECT * FROM produto''')
    produtos = cursor.fetchall()
    print("="*15,"RELATORIO ESTOQUE","="*15)
    print("\nID  Produto  Quantidade     Preço")
    for produto in produtos:
        print(f"{produto[0]} \t{produto[1]} \t\t{produto[2]} \t\t\t{produto[3]}")
def adicionar(nome,qtd,preco):
    cursor.execute(f'''INSERT INTO produto (
    nome,qtd,preco) VALUES ('{nome}',{qtd},{preco})''')
    conexao.commit()
def remover(id):
    cursor.execute(f"DELETE FROM produto WHERE id = {id}")
    conexao.commit()
    print("Produto removido com sucesso!!!")
def alterar(id):
    while True:
        print('''1 - Alterar o nome do produto
         2 - Alterar a quantidade do produto
         3 - alterar o preço do produto
         4 - Voltar ao menu principal''')
        op = input("Digite a opção: ")
        if op == "1":
            nome = input("Digite o novo nome do produto: ")
            cursor.execute(f"UPDATE produto SET nome = '{nome}' WHERE id = {id}")
            conexao.commit()
            print("Nome do produto alterado com sucesso!!!")
        elif op == "2":
            qtd = input("Digite o nome do produto: ")
            cursor.execute(f"UPDATE produto SET qtd = '{qtd}' WHERE id = {id}")
            conexao.commit()
            print("Quantidade do produto alterado com sucesso!!!")
        elif op == "3":
            preco = input("Digite o nome do produto: ")
            cursor.execute(f"UPDATE produto SET preco = '{preco}' WHERE id = {id}")
            conexao.commit()
            print("Preço do produto alterado com sucesso!!!")
        elif op == "4":
            break


while True:
    print("="*15,"Controle de Estoque","="*15)
    print('''\ta - Adicionar produto
\tp - Exibir na tela
\td - Excluir produto
\tt - Alterar produto
\ts - Sair''')
    op = input("Escolha uma opção: ")
    if op == "a":
        nome = input("Digite o nome do produto: ")
        qtd = int(input("Digite a quantidade: "))
        preco = float(input("Digite o valor: "))
        adicionar(nome,qtd,preco)
    elif op == "p":
        exibir()
    elif op == "d":
        id = int(input("Digite o Codigo do produto: "))
        remover(id)
    elif op == "t":
        print("="*15,"ALTERAÇÃO DE PRODUTO","="*15)
        id = int(input("Digite o Codigo do produto: "))
        alterar(id)

    elif op == "s":
        break
#teste


