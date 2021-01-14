

# dictMotorista = {
#  111: {'cpf': 111, 'nome': 'Leonardo', 'carteira': 'A'},
#  122: {'cpf': 122, 'nome': 'Leandro', 'carteira': 'B'},
#  123: {'cpf': 123, 'nome': 'Cássio', 'carteira': 'AB'}
#
# }

dictMotorista = dict()

def verifica_cpf(cpf):
    return dictMotorista.get(cpf)



def cadastra_motorista():
    try:
        cadastro = {'cpf':0,
                    'nome':'',
                    'carteira':''}
        cadastro['cpf'] = int(input('Informe o CPF do motorista: '))
        cadastro['nome'] = str(input('Informe o NOME do motorista: '))
        cadastro['carteira'] = str(input('Informe o CARTEIRA do motorista - A, B ou AB: ')).upper()
        cpf = cadastro['cpf']

        if not dictMotorista:
            dictMotorista[cpf] = cadastro.copy()
            print('Cadastro realizado com sucesso!')
        else:
            motorista = verifica_cpf(cpf)
            if motorista != None:
                print('Cadastro já existente com esse CPF!')
            else:
                dictMotorista[cpf] = cadastro.copy()
                print('Cadastro realizado com sucesso!')

    except ValueError:
        print("\tOCORREU UM ERRO :/")
        print("COM AS INFORMAÇÕES PASSADAS ")


def buscar_por_cpf():
    if not dictMotorista:
        print('Nenhum Motorista Cadastrado!')
    else:
        try:
            cpf = int(input('Informe o CPF: '))
            motorista = verifica_cpf(cpf)
            if motorista != None:
                print('O motorista possui essas Informações ')
                print('CPF: ▸',motorista['cpf'])
                print('NOME: ▸', motorista['nome'])
                print('HABILITAÇÃO: ▸', motorista['carteira'])
            else:
                print('Nemhum CPF foi encontrado!')
        except ValueError:
            print("\tOCORREU UM ERRO :/")
            print("COM AS INFORMAÇÕES PASSADAS ")


def editar_nome_motorista():
    if not dictMotorista:
        print('Nenhum Motorista Cadastrado!')
        print('Cadastre Primeiro um')
    else:
        try:
            cpf = int(input('Informe o CPF: '))
            motorista = verifica_cpf(cpf)
            if motorista != None:
                motorista['nome'] = str(input('Iforme o novo nome: '))
                print('Troca realizada com sucesso! ')
            else:
                print('Motorista NÃO encontrado com o CPF informado!')

        except ValueError:
            print("\tOCORREU UM ERRO :/")
            print("COM AS INFORMAÇÕES PASSADAS ")


def remover_motorista():
    if not dictMotorista:
        print('Nenhum Motorista Cadastrado!')
        print('Cadastre Primeiro um')
    else:
        try:
            cpf = int(input('Informe o CPF que deseja EXCLUIR!: '))
            motorista = verifica_cpf(cpf)
            if motorista != None:
                del dictMotorista[cpf]
                print('Exclusão feita com sucesso!')
            else:
                print('CPF Informado NÃO Encontrado!')
        except ValueError:
            print("\tOCORREU UM ERRO :/")
            print("COM AS INFORMAÇÕES PASSADAS ")

def lista_tipo_carteira():
    if not dictMotorista:
        print('Nenhum Motorista Cadastrado!')
        print('Cadastre Primeiro um')
    else:
        try:
            tipo = str(input('Informe a Habilitação: ')).upper()
            for motorita in dictMotorista.values():
                if motorita['carteira'] == tipo:
                    print('CPF: ',motorita['cpf'])
                    print('NOME: ', motorita['nome'])
                    print('HABILITADÇÃO: ', motorita['carteira'])
                    print('⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻')

        except ValueError:
            print("\tOCORREU UM ERRO :/")
            print("COM AS INFORMAÇÕES PASSADAS ")



def lista_todos_motoristas():
    if not dictMotorista:
        print('NÃO Há Motorista Cadastrado')
    else:
        for cpf, motorista in dictMotorista.items():
            print('O CPF: ',cpf)
            print('Com Nome: ',motorista['nome'])
            print('Possui Habiitação: ', motorista['carteira'])
            print('⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻⫻')



def motorista_disponivel():
    dictcpf = {}
    for motorista in dictMotorista.values():
        if motorista['cpf'] != None:
            cpf = motorista['cpf']
            dictcpf[cpf] = motorista.copy()
    return dictcpf