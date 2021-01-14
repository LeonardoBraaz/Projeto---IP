from controlador_veiculo import verifica_placa, lista_veiculos_disponivel


#dictViagem = {1: {'placa': 'PGL121', 'destino': 'Sei lá', 'status': True}}


dictViagem = dict()


indice = 0

def tamanho_dictviagens():
    return len(dictViagem)


def indice_viagem():
    global indice
    indice += 1
    return indice


def viagem_ativa(placa):
    for viagem in dictViagem.values():
        if viagem['placa'] == placa:
            if viagem['status'] == True:
                return True


def verifica_viagem(placa):
    for veiculo in dictViagem.values():
        if veiculo['placa'] == placa:
            return veiculo


def criar_viagem():
    try:
        def viagem_Criada():
            viagemid = indice_viagem()
            viagem['placa'] = placa
            viagem['destino'] = str(input('Pra onde vai ser a viagem: '))
            viagem['status'] = True
            dictViagem[viagemid] = viagem.copy()
            print('Viagem aprovada, Veículo autorizado para saída!')

        viagem = {'placa':0,
                  'destino':'',
                  'status':False
                  }
        placa = str(input('Informe a PLACA: ')).upper()
        veiculo = verifica_placa(placa)
        veiEmViagem = verifica_viagem(placa)

        if veiculo != None:
            if not dictViagem:
                if veiculo['motorista'] != None:
                    viagem_Criada()
                    print('Primeira Viagem encaminhada!')
                else:
                    print('O veículo deve ter um motorista cadastrado!')

            elif veiEmViagem != None:
                viagemAtiva = viagem_ativa(placa)
                if viagemAtiva:
                    print('A placa',veiEmViagem['placa'])
                    print('Veíclo se encontra em uma viagem')

                else:
                    if veiculo['motorista'] != None:
                        viagem_Criada()
                    else:
                        print('O veículo deve ter um motorista cadastrado!')

            elif veiEmViagem == None:
                if veiculo['motorista'] != None:
                    viagem_Criada()
                else:
                    print('O Veículo deve ter um motorista!')
        else:
            print('A placa informada NÃO existe!')

    except ValueError:
        print("\tOCORREU UM ERRO :/")
        print("COM AS INFORMAÇÕES PASSADAS ")



def finalizar_viagem():
    if not dictViagem:
        print('NÃO Existem Nenhum Cadastro de Viagem ')
    else:
        try:
            placa = str(input('Informe a PLACA: ')).upper()
            viagem = verifica_viagem(placa)
            veiculo = verifica_placa(placa)
            if veiculo != None:
                if viagem != None:
                    if viagem['status'] == True:
                        viagem['status'] = False
                        print('Viagem finalizada com sucesso!')

                    elif viagem['status'] == False:
                        print('O Veículo já finalizou a Viagem!')

                else:
                    if veiculo != None:
                        print('O veículo NÃO está em nenhuma viagem!')
            else:
                print('A placa informada não existe!')

        except ValueError:
            print("\tOCORREU UM ERRO :/")
            print("COM AS INFORMAÇÕES PASSADAS ")


def viagens_ativas():
    if not dictViagem:
        print('NÃO Existem Nenhum Cadastro de Viagem ')
    else:
        condicao = True
        for viagem in dictViagem.values():
            if viagem['status'] == True:
                print('A PLACA: ',viagem['placa'])
                print('Viagem/Destino: ', viagem['destino'])
                print('Viagem Ativa')
                print('⩶⩶⩶⩶⩶⩶⩶⩶⩶⩶⩶⩶')
                condicao = False
            if condicao:
                print('⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗')
                print('\tNÃO Existe Viagens ativas')
                print('⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗')

def veiculo_em_viagem():
    if not dictViagem:
        print('NÃO Existem Nenhum Cadastro de Viagem ')
    else:
        condicao = True
        for viagem in dictViagem.values():
            placa = viagem['placa']
            veiculo = verifica_placa(placa)
            if veiculo['placa'] == viagem ['placa']:
                if viagem['status'] == True:
                    print('PLACA: ',viagem ['placa'])
                    print('Tipo: ', veiculo['tipo'])
                    print('Viagem/ Destino: ',viagem['destino'])
                    print('⩶⩶ dados Do Motorista ⩶⩶')
                    print('Motorista: Nome ', veiculo['motorista']['nome'])
                    print('Motorista: CPF ', veiculo['motorista']['cpf'])
                    print('Motorista: Habilitação ', veiculo['motorista']['carteira'])
                    print('⩶⩶⩶⩶⩶⩶⩶⩶⩶⩶⩶⩶⩶')
                    condicao = False
            if condicao:
                print('⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗')
                print(' \tNÃO Há Veículos em viagem!')
                print('⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗')


def veiculo_disponivel_viagem():
    VeiculoOcupado = lista_veiculos_disponivel()
    condicao = False
    cont = 0

    if VeiculoOcupado != None:
        for viagem in dictViagem.values():
            if viagem['status'] == True:
                placa = viagem['placa']
                if placa in VeiculoOcupado:
                    del VeiculoOcupado[placa]
                    condicao = True
                    cont +=1
    if not VeiculoOcupado and cont == 0:
        if not VeiculoOcupado:
            print('⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗')
            print(' \tNÃO Há Veículos Disponíveis!')
            print('⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗⁗')
            print("Talvez não tenha nehum motorista Cadastrado nos veículos")

    if condicao:
        if VeiculoOcupado != None:
            for veiculo in VeiculoOcupado.values():
                print('Placa: ', veiculo['placa'])
                print('Tipo: ', veiculo['placa'])
                print('Dados do motorista')
                print('CPF: ', veiculo['motorista']['cpf'])
                print('nome: ', veiculo['motorista']['nome'])
                print('nome: ', veiculo['motorista']['carteira'])
                print("-----------------------------")
        if not VeiculoOcupado:
            print('Todos os Veículos ocupados estão em viagem!')

    print(f'Existe {cont} viagem em andamento')


def listar_todas_viagens():
    if not dictViagem:
        print('Não há viagens feitas ainda!')
    else:
        for viagem in dictViagem.values():
            print('PLACA do veiculo: ',viagem['placa'])
            print('Viagem/Destino: ',viagem['destino'])
            if viagem['status'] == True:
                print('Veículo em Viagem')
            else:
                print('Viagem já foi Concluída!')