from conexao import conectar

def listar_produtos():
    conexao = conectar()
    
    cursor = conexao.cursor()
    
    cursor.execute("SELECT id, nome, preco, quantidade FROM produtos")
    
    produtos = cursor.fetchall()

    print("\n=== PRODUTOS DISPONÍVEIS ===")

    for p in produtos:
        print(f"ID: {p[0]} | {p[1]} | R$ {p[2]} | Estoque: {p[3]}")

    cursor.close()
    conexao.close()

def pesquisar_produto():

    nome = input("Digite o nome do produto: ")

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT id, nome, preco, quantidade FROM produtos WHERE nome LIKE %s"
    cursor.execute(sql, (f"%{nome}%",))

    produtos = cursor.fetchall()

    print("\n=== RESULTADO DA PESQUISA ===")

    if produtos:
        for p in produtos:
            print(f"ID: {p[0]} | {p[1]} | R$ {p[2]} | Estoque: {p[3]}")
    else:
        print("Nenhum produto encontrado.")

    cursor.close()
    conexao.close()

carrinho = []


def adicionar_carrinho():

    id_produto = input("Digite o ID do produto: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT nome, preco FROM produtos WHERE id = %s", (id_produto,))
    produto = cursor.fetchone()

    if produto:
        carrinho.append(produto)
        print(f"✔ {produto[0]} adicionado ao carrinho!")
    else:
        print("❌ Produto não encontrado.")

    cursor.close()
    conexao.close()


def ver_carrinho():

    print("\n=== CARRINHO ===")

    total = 0

    if not carrinho:
        print("Carrinho vazio.")
        return

    for item in carrinho:
        print(f"{item[0]} - R$ {item[1]}")
        total += item[1]

    print(f"\nTOTAL: R$ {total:.2f}")

def finalizar_compra():

    print("\n=== FINALIZAR COMPRA ===")

    if not carrinho:
        print("Carrinho vazio!")
        return

    total = 0

    print("\nItens da compra:")
    for item in carrinho:
        print(f"- {item[0]} | R$ {item[1]}")
        total += item[1]

    print(f"\nTOTAL DA COMPRA: R$ {total:.2f}")

    print("\nFormas de pagamento:")
    print("1 - Dinheiro")
    print("2 - Cartão de crédito")
    print("3 - Pix")

    opcao = input("Escolha a forma de pagamento: ")

    if opcao == "1":
        forma = "Dinheiro"
    elif opcao == "2":
        forma = "Cartão de crédito"
    elif opcao == "3":
        forma = "Pix"
    else:
        print("Forma inválida!")
        return

    print(f"\n✔ Compra finalizada com sucesso!")
    print(f"Pagamento: {forma}")
    print(f"Total pago: R$ {total:.2f}")

    # limpa carrinho após compra
    carrinho.clear()

    print("\n====================================")
    resposta = input("Deseja comprar com a FarmaTech novamente? (s/n): ").lower()

    if resposta == "s":
        print("\n✔ Redirecionando para o menu...")
        return "continuar"

    else:
        print("\n👋 Obrigado por comprar na FarmaTech!")
        return "sair"

def menu_comprador(usuario):

    while True:

        print("\n========================")
        print("   ÁREA DO COMPRADOR")
        print("========================")
        print("1 - Listar produtos")
        print("2 - Pesquisar produto")
        print("3 - Adicionar ao carrinho")
        print("4 - Ver carrinho")
        print("5 - Finalizar compra")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            listar_produtos()

        elif opcao == "2":
            pesquisar_produto()

        elif opcao == "3":
            adicionar_carrinho()

        elif opcao == "4":
            ver_carrinho()
        
        elif opcao == "5":
            resultado = finalizar_compra()

            if resultado == "sair":
                break

        elif opcao == "0":
            print("Saindo do sistema do comprador...")
            break

        else:
            print("❌ Opção inválida")