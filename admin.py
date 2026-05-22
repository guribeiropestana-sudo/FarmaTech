from conexao import conectar


# ----------------------------
# CRUD PRODUTOS
# ----------------------------

def criar_produto():

    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO produtos (nome, preco, quantidade)
    VALUES (%s, %s, %s)
    """

    cursor.execute(sql, (nome, preco, quantidade))
    conexao.commit()

    cursor.close()
    conexao.close()

    print("✔ Produto criado com sucesso!")


def listar_produtos():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    print("\n=== PRODUTOS ===")

    for p in produtos:
        print(f"ID: {p[0]} | {p[1]} | R$ {p[2]} | Estoque: {p[3]}")

    cursor.close()
    conexao.close()


def atualizar_produto():

    id_produto = input("ID do produto: ")

    nome = input("Novo nome: ")
    preco = float(input("Novo preço: "))
    quantidade = int(input("Nova quantidade: "))

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE produtos
    SET nome=%s, preco=%s, quantidade=%s
    WHERE id=%s
    """

    cursor.execute(sql, (nome, preco, quantidade, id_produto))
    conexao.commit()

    cursor.close()
    conexao.close()

    print("✔ Produto atualizado!")


def deletar_produto():

    id_produto = input("ID do produto para deletar: ")

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "DELETE FROM produtos WHERE id=%s"

    cursor.execute(sql, (id_produto,))
    conexao.commit()

    cursor.close()
    conexao.close()

    print("✔ Produto removido!")


# ----------------------------
# RELATÓRIO DE VENDAS
# ----------------------------

def relatorio_vendas():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT COUNT(*), SUM(total) FROM vendas")
    resultado = cursor.fetchone()

    total_vendas = resultado[0] or 0
    valor_total = resultado[1] or 0

    print("\n=== RELATÓRIO DE VENDAS ===")
    print(f"Total de compras: {total_vendas}")
    print(f"Valor total arrecadado: R$ {valor_total:.2f}")

    cursor.close()
    conexao.close()


# ----------------------------
# MENU ADMIN
# ----------------------------

def menu_admin(usuario):

    while True:

        print("\n========================")
        print("     PAINEL ADMIN")
        print("========================")
        print("1 - Criar produto")
        print("2 - Listar produtos")
        print("3 - Atualizar produto")
        print("4 - Deletar produto")
        print("5 - Relatório de vendas")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            criar_produto()

        elif opcao == "2":
            listar_produtos()

        elif opcao == "3":
            atualizar_produto()

        elif opcao == "4":
            deletar_produto()

        elif opcao == "5":
            relatorio_vendas()

        elif opcao == "0":
            print("Saindo do admin...")
            break

        else:
            print("Opção inválida!")