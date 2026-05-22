from conexao import conectar


def buscar_usuario(login, senha):

    conexao = conectar()
    if not conexao:
        return None

    cursor = conexao.cursor(dictionary=True)

    sql = """
    SELECT login, tipo
    FROM usuarios
    WHERE login = %s AND senha = %s
    """

    cursor.execute(sql, (login, senha))
    usuario = cursor.fetchone()

    cursor.close()
    conexao.close()

    return usuario

def usuario_existe(login):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT login FROM usuarios WHERE login = %s"
    cursor.execute(sql, (login,))

    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado is not None


def cadastrar_usuario():

    print("\n=== CADASTRO DE USUÁRIO ===")

    login = input("Login: ").strip()
    senha = input("Senha: ").strip()
    tipo = input("Tipo (admin/comprador): ").strip().lower()

    if not login or not senha:
        print("❌ Campos obrigatórios!")
        return None

    if tipo not in ["admin", "comprador"]:
        print("❌ Tipo inválido!")
        return None

    if usuario_existe(login):
        print("❌ Usuário já existe!")
        return None

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO usuarios (login, senha, tipo)
    VALUES (%s, %s, %s)
    """

    cursor.execute(sql, (login, senha, tipo))
    conexao.commit()

    cursor.close()
    conexao.close()

    print("✔ Cadastro realizado com sucesso!")

    #retorna o usuário para login automático
    return {
        "login": login,
        "tipo": tipo
    }

def tela_admin(nome_usuario):
    print('\n=================================')
    print('       TELA ADMINISTRATIVA')
    print('=================================')
    print(f'Bem-vindo(a), {nome_usuario}!')


def tela_comprador(nome_usuario):
    print('\n=================================')
    print('        TELA DO CLIENTE')
    print('=================================')
    print(f'Bem-vindo(a), {nome_usuario}!')



def realizar_login():
    from comprador import menu_comprador
    from admin import menu_admin

    while True:

        print("\n========================")
        print("      FARMATECH")
        print("========================")
        print("1 - Login")
        print("2 - Cadastrar usuário")
        print("0 - Sair")

        opcao = input("\nEscolha: ")

        # ---------------- LOGIN ----------------
        if opcao == "1":

            login = input("Login: ").strip()
            senha = input("Senha: ").strip()

            usuario = buscar_usuario(login, senha)

            if usuario:

                if usuario["tipo"] == "admin":
                    menu_admin(usuario["login"])                
                else:
                    menu_comprador(usuario["login"])
                break 

            else:
                print("❌ Login ou senha inválidos!")

        # ---------------- CADASTRO ----------------
        elif opcao == "2":

            usuario = cadastrar_usuario()

            if usuario:

                # entra direto na tela certa
                if usuario["tipo"] == "admin":
                    tela_admin(usuario["login"])
                else:
                    tela_comprador(usuario["login"])

                break 

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("❌ Opção inválida!")