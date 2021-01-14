from menus_secundario import *
from time import sleep
from controlador_motorista import cadastra_motorista, lista_todos_motoristas, buscar_por_cpf,\
    editar_nome_motorista, remover_motorista, lista_tipo_carteira

from controlador_veiculo import cadastra_veiculo, lista_veiculo_sem_motorista, buscar_veiculo_Placa, \
adiciona_motorista_veiculo, remove_motorista_veiculo, lista_veiculo_com_motorista, remove_veiculo

from controlador_viagem import criar_viagem, finalizar_viagem, viagens_ativas, veiculo_em_viagem, \
    veiculo_disponivel_viagem, listar_todas_viagens



def main():
    while True:
        menuPrincipal()
        opcao = input('Escolha uma das opções: ')
        if opcao == '1':
            menu_motorista()

        elif opcao == '2':
            menu_veiculo()

        elif opcao == '3':
            menu_viagem()

        elif opcao == '4':
            print('Você optou por SAIR')
            sleep(0.5)
            print('SAINDO...')
            sleep(0.5)
            print('Fechando Programa!')
            sleep(0.5)
            break
        else:
            print('∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺')
            print('∺∺∺ Opção Inválida ∺∺∺')
            print('∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺')




def menu_motorista():
    while True:
        menuMotorista()
        opcao = input('Escolha uma das opções: ')

        if opcao == '1':
            titulo('Cadastrar Motorista')
            cadastra_motorista()

        elif opcao == '2':
            titulo('Buscar Motorista por CPF')
            buscar_por_cpf()

        elif opcao == '3':
            titulo('Editar NOME do Motorista')
            editar_nome_motorista()

        elif opcao == '4':
            titulo('REMOVER Motorista')
            remover_motorista()

        elif opcao == '5':
            titulo('Listar os Motorista por TIPO da carteira')
            lista_tipo_carteira()

        elif opcao == '6':
            titulo('Listar Todos os Motorista')
            lista_todos_motoristas()

        elif opcao == '7':
            titulo('SAIR')
            print('Você optou por SAIR')
            sleep(0.5)
            print('SAINDO...')
            sleep(0.5)
            print('Retornando ao Menu Incial')
            sleep(0.5)
            break

        else:
            print('∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺')
            print('∺∺∺ Opção Inválida ∺∺∺')
            print('∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺')




def menu_veiculo():
    while True:
        menuVeiculo()
        opcao = input('Escolha uma das opções: ')

        if opcao == '1':
            titulo('Cadastrar Veículo')
            cadastra_veiculo()

        elif opcao == '2':
            titulo('Buscar Veículo por PLACA')
            buscar_veiculo_Placa()

        elif opcao == '3':
            titulo('Adicionar motorista ao veículo')
            adiciona_motorista_veiculo()

        elif opcao == '4':
            titulo('REMOVER motorista do veículo')
            remove_motorista_veiculo()

        elif opcao == '5':
            titulo('Listar Veículos Com Motoristas')
            lista_veiculo_com_motorista()

        elif opcao == '6':
            titulo('Listar veículos Sem Motoristas')
            lista_veiculo_sem_motorista()
        elif opcao == '7':
            titulo('REMOVER Veículo')
            remove_veiculo()

        elif opcao == '8':
            titulo('SAIR')
            print('Você optou por SAIR')
            sleep(0.5)
            print('SAINDO...')
            sleep(0.5)
            print('Retornando ao Menu Incial')
            sleep(0.5)
            break

        else:
            print('∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺')
            print('∺∺∺ Opção Inválida ∺∺∺')
            print('∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺')

def menu_viagem():
    while True:
        menuViagem()
        opcao = input('Escolha uma das opções: ')
        if opcao == '1':
            titulo('Criar Viagem')
            criar_viagem()

        elif opcao == '2':
            titulo('Finalizar Viagem Por Placa')
            finalizar_viagem()

        elif opcao == '3':
            titulo('Viagens Ativas')
            viagens_ativas()

        elif opcao == '4':
            titulo('Veiculos Que Estão Em Viagem')
            veiculo_em_viagem()

        elif opcao == '5':
            titulo('Veículos Que Estão Disponíveis Para Viagem')
            veiculo_disponivel_viagem()

        elif opcao == '6':
            titulo('Listar Todas As Viagens')
            listar_todas_viagens()

        elif opcao == '7':
            titulo('SAIR')
            print('Você optou por SAIR')
            sleep(0.5)
            print('SAINDO...')
            sleep(0.5)
            print('Retornando ao Menu Incial')
            sleep(0.5)
            break

        else:
            print('∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺')
            print('∺∺∺ Opção Inválida ∺∺∺')
            print('∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺∺')

if __name__ == '__main__':
    main()