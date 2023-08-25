nomes_estudantes = []
while True:

    print("Seja Bem Vindo(a), ao sistema de gestão de dados acadêmicos da Puc Paraná!")

    print("########## Menu do usuario ##########")

    print("1 - Estudantes;")
    print("2 - Disciplinas;")
    print("3 - Professores;")
    print("4 - Turmas;")
    print("5 - matriculas")
    print("0 - Sair Agora.")

    while True:

        usuario_menu_principal = int(input("Escolha uma das opções do menu acima: "))


        if usuario_menu_principal < 0 or usuario_menu_principal > 5:
            print('Opção invalida, por favor colocar um numero entre "0 e 5"')
        else:
            break

    if usuario_menu_principal == 1:
        print(f"Ok, voce escolheu a opção {usuario_menu_principal} do menu acima.")

        print(" #### BEM VINDO AO MENU DE OPERAÇÕES DOS [ESTUDANTES] #### ")

        print("1 - Incluir;")
        print("2 - Listar;")
        print("3 - Excluir;")
        print("4 - Alterar;")
        print("0 - Voltar Ao Menu Principal")

        usuario_menu_secundario = int(input("Escolha uma das opçoes acima: "))

        if usuario_menu_secundario == 1:
            print(f"Você escolheu a opção 'Incluir' do menu de Estudantes.")
            nome = int(input("Digite o nome do Estudante"))
            nomes_estudantes.append(nome)
            print(f"Nome adicionado com sucesso!!")
            continue



        elif usuario_menu_secundario == 2:
            print(f"Você escolheu a opção 'Listar' do menu de Estudantes.")
            print(f"Lista dos Alunos:")
            for nome in nomes_estudantes:
                print(nome)
                continue


        elif usuario_menu_secundario == 3:
            print(f"Você escolheu a opção 'Excluir' do menu de Estudantes.")
            print(f"OPÇÃO EM DESENVOLVIMENTO....")
            continue
        elif usuario_menu_secundario == 4:
            print(f"Você escolheu a opção 'Alterar' do menu de Estudantes.")
            print(f"OPÇÃO EM DESENVOLVIMENTO....")
            continue
        elif usuario_menu_secundario == 0:
            print("Voltando ao Menu Principal.")
        else:
            break

    elif usuario_menu_principal == 2:
        print(f"Ok, voce escolheu a opção {usuario_menu_principal} do menu acima.")

        print(" #### BEM VINDO AO MENU DE OPERAÇÕES DAS [DISCIPLINAS] #### ")

        print("1 - Incluir;")
        print("2 - Listar;")
        print("3 - Excluir;")
        print("4 - Alterar;")
        print("0 - Voltar Ao Menu Principal")

        usuario_menu_secundario = int(input("Escolha uma das opçoes acima: "))

        if usuario_menu_secundario == 1:
            print(f"Você escolheu a opção 'Incluir' do menu das Disciplinas.")
            print(f"OPÇÃO EM DESENVOLVIMENTO....")
            continue
        elif usuario_menu_secundario == 2:
            print(f"Você escolheu a opção 'Listar' do menu das Disciplinas.")
            print(f"OPÇÃO EM DESENVOLVIMENTO....")
            continue
        elif usuario_menu_secundario == 3:
            print(f"Você escolheu a opção 'Excluir' do menu das Disciplinas.")
            print(f"OPÇÃO EM DESENVOLVIMENTO....")
            continue
        elif usuario_menu_secundario == 4:
            print(f"Você escolheu a opção 'Alterar' do menu das Disciplinas.")
            print(f"OPÇÃO EM DESENVOLVIMENTO....")
            continue
        elif usuario_menu_secundario == 0:
            print("Voltando ao Menu Principal.")
        else:
            break
    elif usuario_menu_principal == 3:
        print(f"Ok, voce escolheu a opção {usuario_menu_principal} do menu acima.")

        print(" #### BEM VINDO AO MENU DE OPERAÇÕES DOS [PROFESSORES] #### ")

        print("1 - Incluir;")
        print("2 - Listar;")
        print("3 - Excluir;")
        print("4 - Alterar;")
        print("0 - Voltar Ao Menu Principal")

        usuario_menu_secundario = int(input("Escolha uma das opçoes acima: "))

        if usuario_menu_secundario == 1:
            print(f"Você escolheu a opção 'Incluir' do menu dos Professores.")
            print(f"OPÇÃO EM DESENVOLVIMENTO....")
            continue

        elif usuario_menu_secundario == 2:
            print(f"Você escolheu a opção 'Listar' do menu dos Professores.")
            print(f"OPÇÃO EM DESENVOLVIMENTO....")
            continue
        elif usuario_menu_secundario == 3:
            print(f"Você escolheu a opção 'Excluir' do menu dos Professores.")
            print(f"OPÇÃO EM DESENVOLVIMENTO....")
            continue
        elif usuario_menu_secundario == 4:
            print(f"Você escolheu a opção 'Alterar' do menu dos Professores.")
            print(f"OPÇÃO EM DESENVOLVIMENTO....")
            continue
        elif usuario_menu_secundario == 0:
            print("Voltando ao Menu Principal.")
        else:
            break
    elif usuario_menu_principal == 4:
        print(f"Ok, voce escolheu a opção {usuario_menu_principal} do menu acima.")

        print(" #### BEM VINDO AO MENU DE OPERAÇÕES DAS [TURMAS] #### ")

        print("1 - Incluir;")
        print("2 - Listar;")
        print("3 - Excluir;")
        print("4 - Alterar;")
        print("0 - Voltar Ao Menu Principal")

        usuario_menu_secundario = int(input("Escolha uma das opçoes acima: "))

        if usuario_menu_secundario == 1:
            print(f"Você escolheu a opção 'Incluir' do menu das Turmas.")
            print(f"OPÇÃO EM DESENVOLVIMENTO....")
            continue
        elif usuario_menu_secundario == 2:
            print(f"Você escolheu a opção 'Listar' do menu das Turmas.")
            print(f"OPÇÃO EM DESENVOLVIMENTO....")
            continue
        elif usuario_menu_secundario == 3:
            print(f"Você escolheu a opção 'Excluir' do menu das Turmas.")
            print(f"OPÇÃO EM DESENVOLVIMENTO....")
            continue
        elif usuario_menu_secundario == 4:
            print(f"Você escolheu a opção 'Alterar' do menu das Turmas.")
            print(f"OPÇÃO EM DESENVOLVIMENTO....")
            continue
        elif usuario_menu_secundario == 0:
            print("Voltando ao Menu Principal.")
        else:
            break
    elif usuario_menu_principal == 5:
        print(f"Ok, voce escolheu a opção {usuario_menu_principal} do menu acima.")

        print(" #### BEM VINDO AO MENU DE OPERAÇÕES DAS [MATRICULAS] #### ")

        print("1 - Incluir;")
        print("2 - Listar;")
        print("3 - Excluir;")
        print("4 - Alterar;")
        print("0 - Voltar Ao Menu Principal")

        usuario_menu_secundario = int(input("Escolha uma das opçoes acima: "))

        if usuario_menu_secundario == 1:
            print(f"Você escolheu a opção 'Incluir' do menu das Matriculas.")
            print(f"OPÇÃO EM DESENVOLVIMENTO....")
            continue
        elif usuario_menu_secundario == 2:
            print(f"Você escolheu a opção 'Listar' do menu das Matriculas.")
            print(f"OPÇÃO EM DESENVOLVIMENTO....")
            continue
        elif usuario_menu_secundario == 3:
            print(f"Você escolheu a opção 'Excluir' do menu das Matriculas.")
            print(f"OPÇÃO EM DESENVOLVIMENTO....")
            continue
        elif usuario_menu_secundario == 4:
            print(f"Você escolheu a opção 'Alterar' do menu das Matriculas.")
            print(f"OPÇÃO EM DESENVOLVIMENTO....")
            continue
        elif usuario_menu_secundario == 0:
            print("Voltando ao Menu Principal.")
        else:
            break
    if usuario_menu_principal == 0:
        print("VOCÊ ESCOLHEU SAIR...")
        print(f"Obrigado por Utilizar o Gestão de Dados Acadêmicos da PUC.")
        break


    #proxima semana#

