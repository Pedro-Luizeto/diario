from pathlib import Path

def main():
    diario_path = Path('diario.txt')
    while True:
        escolha = input('Você deseja escrever uma anotação ou consultar o diário?' \
        '[1] Escrever [2] Consultar [3] Sair: ')

        if escolha == '1':
            anotacao = input('Digite sua anotação: ')
            with open(diario_path, 'a') as diario:
                diario.write(anotacao + '\n')
            print('Anotação salva com sucesso!')

        elif escolha == '2':
            if diario_path.exists():
                with open(diario_path, 'r') as diario:
                    conteudo = diario.read()
                    if conteudo:
                        print('Anotações do diário: ')
                        print(conteudo)
                    else:
                        print('Seu diário ainda está vazio!')
            else:
                print('O diário não existe, gostaria de criar um novo diário ? [S/N]')

                if input().strip().upper() == 'S':
                    diario_path.touch()
                    print('Novo diário criado com sucesso!')

                else:
                    print('Operação cancelada. Nenhum diário foi criado.')


        elif escolha == '3':
            print('Saindo do programa.')
            break

        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')