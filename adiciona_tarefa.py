import sqlite3

conexao=sqlite3.connect('tarefas.db')
cursor=conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS minhas_tarefas(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               descricao TEXT NOT NULL)""")
conexao.commit()

while True: 
    print("---GERENCIADOR DE TAREFAS---")
    print("DIGITE 1 PARA ADICIONAR\n       2 PARA VER\n       3 PARA SAIR ")
    try:

        Opçao=int(input('Digite apenas a opcao: '))

        if Opçao== 1:
            adicionar=input('Digite o que voce deseja: ')

            cursor.execute("INSERT INTO minhas_tarefas (descricao) VALUES (?)",(adicionar,))
            conexao.commit()
            print('Adicionado com Sucesso')
        elif Opçao == 2:
            print(f'----SEUS DADOS----')

            cursor.execute("SELECT*FROM minhas_tarefas")
            tarefas=cursor.fetchall()

            if len(tarefas)==0:
                print('Voce nao adicionou nada ainda')

            else:
                for tare in tarefas:
                    print(f'seus dados: [{tare[0]}] - [{tare[1]}]')
            print()
           
        elif Opçao == 3:
           print('O programa foi fechado')
           conexao.close()
           break

        else:
            print('Por favor digite numeros de 1 a 3')
    except:
        print('Algo de errado nao esta certo\n -----PROGRAMA FOI FECHADO POR MOTIVOS DE SEGURANÇA-----')
        break