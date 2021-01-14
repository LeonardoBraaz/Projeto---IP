def menuPrincipal():
    print('⩶⩶⩶⩶⩶⩶ MENU INICIAL ⩶⩶⩶⩶⩶⩶')
    print('1 ⇾ Menu dos Motoristas')
    print('2 ⇾ Menu de Veículos')
    print('3 ⇾ Menu de Viagem')
    print('4 ⇾ SAIR')

def menuMotorista():
    print('⩶⩶⩶⩶⩶⩶ MENU DOS MOTORISTAS ⩶⩶⩶⩶⩶⩶')
    print('1 ⇾ Cadastrar Motorista')
    print('2 ⇾ Buscar Motorista por cpf')
    print('3 ⇾ Editar Nome do Motorista')
    print('4 ⇾ Remover Motorista')
    print('5 ⇾ Listar Todos os Motorista por tipo da carteira')
    print('6 ⇾ Listar Todos os Motorista')
    print('7 ⇾ SAIR')

#perguntar antes qual tipo da carteira ('A' - 'B' - 'AB')
#antes Buscar por cpf o motorista


def menuVeiculo():
    print('⩶⩶⩶⩶⩶⩶ MENU DE VEÍCULOS ⩶⩶⩶⩶⩶⩶')
    print('1 ⇾ Cadastrar Veículo')
    print('2 ⇾ Buscar Veículo por Placa')
    print('3 ⇾ Adicionar motorista ao veículo')
    print('4 ⇾ Remover motorista do veículo')
    print('5 ⇾ Listar veículos com motoristas')
    print('6 ⇾ Listar veículos sem motoristas')
    print('7 ⇾ Remover Veículo')
    print('8 ⇾ SAIR')


def titulo(titulo):
    print('⩶⩶⩶⩶⩶⩶ '+titulo+' ⩶⩶⩶⩶⩶⩶\n')


def menuViagem():
    print('⩶⩶⩶⩶⩶⩶ MENU ⩶⩶⩶⩶⩶⩶')
    print('1 ⇾ Criar Viagem')
    print('2 ⇾ Finalizar Viagem por placa') # - Aqui muda somente o status de True para False
    print('3 ⇾ Viagens Ativas')
    print('4 ⇾ Veículos que estão em Viagem')
    print('5 ⇾ Veículos que estão Disponíveis para Viagem')
    print('6 ⇾ Listar todas as viagens')
    print('7 ⇾ SAIR')
