from controlador_motorista import verifica_cpf, motorista_disponivel


# dictVeiculo = {
#     'PGL121': {'placa': 'PGL121', 'tipo': 'MOTO', 'motorista': {'cpf': 111, 'nome': 'Leonardo', 'carteira': 'A'}},
#     'PGL122': {'placa': 'PGL122', 'tipo': 'MOTO', 'motorista': None},
#     'PGL123': {'placa': 'PGL123', 'tipo': 'CARRO', 'motorista': None},
#     'PGL124': {'placa': 'PGL124', 'tipo': 'CARRO', 'motorista': None}
#   }


dictVeiculo = dict()


def verifica_placa(placa):
    return dictVeiculo.get(placa)


# def verifica_placa(placa):
#     for veiculo in dictVeiculo.keys():
#         if placa == veiculo:
#             return veiculo


def cadastra_veiculo():
    try:
        veiculo = {
            'placa':'',
            'tipo':'',
            'motorista':None
        }
        veiculo['placa'] = str(input('Informe a placa: ')).upper()
        placa = veiculo['placa']
        print('⩶⩶ Escoha o número referente ao tipo ⩶⩶')
        print('1 ↔ Para MOTO')
        print('2 ↔ Para CARRO')
        tipo = str(input('Informe o número aqui▸ '))

        if tipo == '1':
            veiculo['tipo'] = 'MOTO'
            if not dictVeiculo:
                dictVeiculo[placa] = veiculo.copy()
                print('Cadastro realixado com sucesso!')
            else:
                verifica = verifica_placa(placa)
                if verifica != None:
                    print('A PLACA INFORMADA,')
                    print('Veículo já exite cadastro!')
                else:
                    dictVeiculo[placa] = veiculo.copy()
                    print('Cadastro realixado com sucesso!')

        elif tipo == '2':
            veiculo['tipo'] = 'CARRO'
            if not dictVeiculo:
                dictVeiculo[placa] = veiculo.copy()
                print('Cadastro realixado com sucesso!')
            else:
                verifica = verifica_placa(placa)
                if verifica != None:
                    print('Veículo já exite cadastro!')
                else:
                    dictVeiculo[placa] = veiculo.copy()
                    print('Cadastro realixado com sucesso!')
        else:
            print('Tipo informado INCORRETO!')

    except ValueError:
        print("\tOCORREU UM ERRO :/")
        print("COM AS INFORMAÇÕES PASSADAS ")



def buscar_veiculo_Placa():
    if not dictVeiculo:
        print('NÃO há Nenhum Veículo Cadastrado \nCadastre Primeiro')
    else:
        try:
            placa = str(input('Informe a PLACA: ')).upper()
            veiculo = verifica_placa(placa)

            if veiculo != None:
                print('⩶⩶⩶⩶⩶⩶⩶⩶⩶⩶⩶⩶')
                print('A PLACA: ',veiculo['placa'])
                print('O TIPO: ', veiculo['tipo'])
                if veiculo['motorista'] == None:
                    print("Satus: Disponível")
                    print('⩶⩶⩶⩶⩶⩶⩶⩶⩶⩶⩶⩶')
                else:
                    motorista = veiculo['motorista']
                    print('——— O veículo Tem motorista cadastrado ———')
                    print('MOTORISTA: CPF ', motorista['cpf'])
                    print('MOTORISTA: Nome ', motorista['nome'])
                    print('MOTORISTA: Habilitação ', motorista['carteira'])
                    print('⩶⩶⩶⩶⩶⩶⩶⩶⩶⩶⩶⩶')
            else:
                print('NENHUM veícuo encontrado!')

        except ValueError:
            print("\tOCORREU UM ERRO :/")
            print("COM AS INFORMAÇÕES PASSADAS ")



def adiciona_motorista_veiculo():
    cpfEncontrado = None
    lista_veiculo_sem_motorista()
    motorista_livre()
    try:
        placa = str(input('Informe a Placa: ')).upper()
        cpf = int(input('Informe o CPF: '))
        veiculo = verifica_placa(placa)
        motorista = verifica_cpf(cpf)

        if motorista != None and veiculo != None:
            for motoristas in dictVeiculo.values():
                if motoristas['motorista'] != None:
                    if motoristas['motorista']['cpf'] == cpf:
                        cpfEncontrado = motoristas['motorista']['cpf']

            if cpfEncontrado != None:
                print('O CPF informado, o motorista está com um veículo. ')
                print('REMOVA primeiro o motorista do outro veículo \npara  adicionar neste!')

            else:
                if veiculo['tipo'] == 'MOTO':
                    listaCarteira = ['A', 'AB']
                    if motorista['carteira'] in listaCarteira:
                        veiculo['motorista'] = motorista
                        print('Motorista adicionado com sucesso!')
                    else:
                        print('Motorista NÃO é habilitado para esse veículo')

                elif veiculo['tipo'] == 'CARRO':
                    listaCarteira = ['B','AB']
                    if motorista['carteira'] in listaCarteira:
                        veiculo['motorista'] = motorista
                        print('Motorista adicionado com sucesso!')
                    else:
                        print('Motorista NÃO é habilitado para esse veículo')
        else:
            print('As informações passadas foram INCORRETAS!')

    except ValueError:
        print("\tOCORREU UM ERRO :/")
        print("COM AS INFORMAÇÕES PASSADAS ")

def remove_motorista_veiculo():
    if not dictVeiculo:
        print('NÃO há Nenhum Veículo Cadastrado \nCadastre Primeiro')
    else:
        placa = str(input('Informe a placa')).upper()
        veiculo = verifica_placa(placa)
        if veiculo != None:
            if veiculo['motorista'] != None:
                veiculo['motorista'] = None
                print('Motorista removido com sucesso!')
                print('Veículo agora está disponível!')
            else:
                print('Veículo NÃO Existe motorista')
        else:
            print('Nemhum veículo encontrado!')


def lista_veiculo_com_motorista():
    condicao = True
    if not dictVeiculo:
        print('Nenhum veículo Cadastrado!')
    else:
        for veiculo in dictVeiculo.values():
            if veiculo['motorista'] != None:
                print('=== Dado do veículo ')
                motorista = veiculo['motorista']
                print('- placa: ',veiculo['placa'])
                print('- Tipo: ',veiculo['tipo'])
                #print('Status: ', veiculo['motorista'].get('cpf'))
                #print('Status: ', veiculo['motorista']['cpf'])
                print('=== Dados do motorista ==')
                print('- CPF: ',motorista['cpf'])
                print('- NOME: ',motorista['nome'])
                print('- HABILITAÇÃO -',motorista['carteira'])
                print('⩶⩶⩶⩶⩶⩶⩶⩶⩶⩶⩶⩶⩶⩶⩶⩶')
                condicao = False
        if condicao:
            print('⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗')
            print('⁗⁗ \tNehum Veículo Encontrado Com Motorista ⁗⁗')
            print('⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗')



def lista_veiculo_sem_motorista():
    condicao = True
    print('⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗ Veículos Disponivéis ⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗')
    if not dictVeiculo:
        print('Nenhum veículo cadastrado!')
    else:
        for veiculo in dictVeiculo.values():
            if veiculo['motorista'] == None:
                print('placa: ',veiculo['placa'])
                print('Tipo: ',veiculo['tipo'])
                print('Status: Veículo Disponível!' )
                print('⩶⩶⩶⩶⩶⩶⩶⩶⩶⩶⩶⩶')
                condicao = False
        if condicao:
            print('⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗')
            print('⁗⁗ \tNehum Veículo Encontrado Sem Motorista ⁗⁗')
            print('⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗')


def remove_veiculo():
    if not dictVeiculo:
        print('NÃO Há Veículo Cadstrado!')
    else:
        placa = str(input('Informe a placa')).upper()
        veiculo = verifica_placa(placa)
        if veiculo != None:
            del dictVeiculo[placa]
            print('Veículo REMOVIDO com sucesso!')
        else:
            print('Nenhum veículo encontrado!')





def lista_veiculos_disponivel():
    dicitVeiculosCadastrado = {}
    for veiculo in dictVeiculo.values():
        if veiculo['motorista'] != None:
            veiculoOcupado = veiculo['placa']
            dicitVeiculosCadastrado[veiculoOcupado] = veiculo.copy()
    return dicitVeiculosCadastrado


def motorista_livre():
    print('⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗ Motoristas Disponivéis ⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗')
    cont = 0
    condicao = True
    cpfsMotoristas = motorista_disponivel()
    if cpfsMotoristas == None:
        print('Não há motorista Cadastrado!')
    else:
        for motorista in dictVeiculo.values():
            if motorista['motorista'] != None:
                cpf = motorista['motorista']['cpf']
                if cpf in cpfsMotoristas.keys():
                    cont +=1
                    del cpfsMotoristas[cpf]
        for motorista in cpfsMotoristas.values():
            print('CPF: ',motorista['cpf'])
            print('NOME: ',motorista['nome'])
            print('HABILITAÇÃO: ',motorista['carteira'])
            print('⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻')
            condicao = False

        if condicao:
            print("Não Há Motoristas Disponiveis!")

    print(f'Existem {cont} Motorista Cadastrado em Veículo!')





