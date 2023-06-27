import sqlite3

conn = sqlite3.connect("projetos.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS projetos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome_do_projeto VARCHAR(255), status VARCHAR(50), link_repositorio VARCHAR(255))")


def adicionar_projeto():
    nome_projeto = input("Digite o nome do projeto: ")
    status = input("Digite o status do projeto (Em andamento/Pausado/Concluído): ")
    link_repositorio = input("Digite o link do repositório: ")

    # Verifica se o status fornecido é válido
    if status not in ["Em andamento", "Pausado", "Concluído"]:
        print("Status inválido. O status padrão 'A realizar' será atribuído.")
        status = "A realizar"

    cursor.execute("INSERT INTO projetos (nome_do_projeto, status, link_repositorio) VALUES (?, ?, ?)",
                   (nome_projeto, status, link_repositorio))
    conn.commit()
    print("Projeto adicionado com sucesso!")

def atualizar_status_projeto():
    nome_projeto = input("Digite o nome do projeto: ")
    novo_status = input("Digite o novo status do projeto (Em andamento/Pausado/Concluído): ")

    # Verifica se o novo status fornecido é válido
    if novo_status not in ["Em andamento", "Pausado", "Concluído"]:
        print("Status inválido.")
        return

    cursor.execute("UPDATE projetos SET status=? WHERE nome_do_projeto=?", (novo_status, nome_projeto))
    conn.commit()

    if cursor.rowcount > 0:
        print("Status do projeto atualizado com sucesso!")
    else:
        print("Projeto não encontrado.")

def atualizar_link_projeto():
    nome_projeto = input("Digite o nome do projeto: ")
    novo_link = input("Digite o novo link do projeto: ")

    cursor.execute("UPDATE projetos SET link_repositorio=? WHERE nome_do_projeto=?", (novo_link, nome_projeto))
    conn.commit()

    if cursor.rowcount > 0:
        print("Link do projeto atualizado com sucesso!")
    else:
        print("Projeto não encontrado.")

def deletar_projeto():
    nome_projeto = input("Digite o nome do projeto a ser deletado: ")

    cursor.execute("DELETE FROM projetos WHERE nome_do_projeto=?", (nome_projeto,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Projeto deletado com sucesso!")
    else:
        print("Projeto não encontrado.")


while True:
    print("===== MENU =====")
    print("1. Adicionar projeto")
    print("2. Atualizar status")
    print("3. Atualizar link do repositório")
    print("4. Deletar projeto")
    print("5. Sair")
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        adicionar_projeto()
    elif opcao == "2":
        atualizar_status_projeto()
    elif opcao == "3":
        atualizar_link_projeto()
    elif opcao == "4":
        deletar_projeto()
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Digite novamente.")

# Fechando a conexão com o banco de dados
conn.close()