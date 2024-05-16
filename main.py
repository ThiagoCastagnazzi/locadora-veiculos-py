cars = {1: {'id': 1, 'plate': 'abc1234', 'brand': 'bmw', 'model': 'x6', 'color': 'branca', 'manufacturing_date': '2024'}}
clients = {1: {'id': 1, 'cpf': '07237395106', 'name': 'thiago castagnazzi', 'birth': '04/10/1999', 'phone': '67998309537'}}
schedules = {}


def new_car(plate, brand, model, color, manufacturing_date):
    id = max(cars.keys()) + 1 if cars else 1

    cars[id] = dict(id=id, plate=plate, brand=brand, model=model, color=color, manufacturing_date=manufacturing_date)
    print('\nCarro adicionado com sucesso !!!\n')


def list_cars():
    print("\nLista de Carros:")
    for car_id, car in cars.items():
        print(f"ID: {car['id']}")
        print(f"Placa: {car['plate']}")
        print(f"Marca: {car['brand']}")
        print(f"Modelo: {car['model']}")
        print(f"Cor: {car['color']}")
        print(f"Ano de Fabricação: {car['manufacturing_date']}\n")

def update_car(id, plate, brand, model, color, manufacturing_date):
    cars[id] = dict(id=id, plate=plate, brand=brand, model=model, color=color, manufacturing_date=manufacturing_date)
    print('\nCarro Atualizado com sucesso !!!\n')

def delete_car(id):
    del cars[id]
    print('\nCarro Deletado com sucesso !!!\n')


# endregion

# region client

def verify_if_cpf_exists(cpf: str) -> bool:
    for _, client in clients.items():
        if client['cpf'] == cpf:
            return True

    return False


def find_client_by_id(client_id: int) -> bool:
    for _, client in clients.items():
        if client['id'] == client_id:
            return True

    return False


def new_client(cpf, name, birth, phone):
    if clients:
        id = max(clients.keys()) + 1
    else:
        id = 1

    clients[id] = {}
    clients[id]['cpf'] = cpf
    clients[id]['name'] = name
    clients[id]['birth'] = birth
    clients[id]['phone'] = phone
    clients[id]['id'] = id
    print('')
    print('Cliente adicionado com sucesso !!!')
    print('')

def list_clients():
    print('')
    print("Lista de Clientes:")
    for client_id, client in clients.items():
        print(f"ID: {client['id']}")
        print(f"CPF: {client['cpf']}")
        print(f"Nome: {client['name']}")
        print(f"Data de Nascimento: {client['birth']}")
        print(f"Telefone: {client['phone']}")
        print('')

def update_client(id, cpf, name, birth, phone):
    clients[id]['cpf'] = cpf
    clients[id]['name'] = name
    clients[id]['birth'] = birth
    clients[id]['phone'] = phone
    print('')
    print('Cliente Atualizado com sucesso !!!')
    print('')

def delete_client(id):
    del clients[id]
    print('')
    print('Cliente Deletado com sucesso !!!')
    print('')


def new_scheduling(client_id, car_id, initial_date, final_date):
    if schedules:
        id = max(schedules.keys()) + 1
    else:
        id = 1

    schedules[id] = {}
    schedules[id]['id'] = id
    schedules[id]['client_id'] = client_id
    schedules[id]['car_id'] = car_id
    schedules[id]['initial_date'] = initial_date
    schedules[id]['final_date'] = final_date
    print('\nAgendamento feito com sucesso !!!\n')

def list_schedules():
    print('')
    print("Lista de Agendamento:")
    for schedule_id, schedule in schedules.items():
        client_id = schedule['client_id']
        car_id = schedule['car_id']
        if client_id in clients and car_id in cars:
            client_cpf = clients[client_id]['cpf']
            car_plate = cars[car_id]['plate']
            print(f"ID: {schedule_id}")
            print(f"CPF do Cliente: {client_cpf}")
            print(f"Placa do Carro: {car_plate}")
            print(f"Data Inicial: {schedule['initial_date']}")
            print(f"Data Final: {schedule['final_date']}")
            print('')

def update_schedule(id, client_id, car_id, initial_date, final_date):
    schedules[id]['client_id'] = client_id
    schedules[id]['car_id'] = car_id
    schedules[id]['initial_date'] = initial_date
    schedules[id]['final_date'] = final_date
    print('\nAgendamento Atualizado com Sucesso !!!\n')

def delete_schedule(id):
    del schedules[id]
    print('\nAgendamento Deletado com sucesso !!!\n')


menu_options = {1: 'Carro', 2: 'Cliente', 3: 'Agendamento', 0: 'Sair'}
sub_menu = {1: 'Criar', 2: 'Listar', 3: 'Atualizar', 4: 'Deletar', 0: 'Voltar'}

while True:
    print('--- MENU ---')
    for key, value in menu_options.items():
        print(f'{key} - {value}')

    try:
        option_selected = int(input('\nEscolha a opção: \n'))

        if option_selected == 0:
            break

        if option_selected not in menu_options:
            print('\nOpção Inválida !!!\n')
            continue

        while True:
            print('--- MENU ---')
            for key, value in sub_menu.items():
                print(f'{key} - {value}')

            sub_option_selected = int(input('\nEscolha a opção: \n'))

            if option_selected == 1:
                if sub_option_selected not in sub_menu:
                    print('\nOpção Inválida !!!\n')
                    continue

                if sub_option_selected == 0:
                    break

                if sub_option_selected == 1:
                    plate = input('Digite a Placa: ')
                    plate_exists = False
                    for car_id, car in cars.items():
                        if car['plate'] == plate:
                            print('\nPlaca já cadastrada.\n')
                            plate_exists = True
                            break

                    if not plate_exists:
                        brand = input('Digite a Marca: ')
                        model = input('Digite o Modelo: ')
                        color = input('Digite a Cor: ')
                        manufacturing_date = input('Digite o Ano de Fabricação: ')
                        new_car(plate, brand, model, color, manufacturing_date)

                if sub_option_selected == 2:
                    if verify_empty_dict('cars'):
                        print('\nNão há carros cadastrados !!!\n')
                    else:
                        list_cars()

                if sub_option_selected == 3:
                    if verify_empty_dict('cars'):
                        print('\nNão há carros cadastrados !!!\n')
                    else:
                        id = int(input('Digite o ID do Carro: '))

                        if not find_car_by_id(id):
                            print('\nID Inválido !!!\n')
                        else:
                            plate_exists = False
                            new_plate = input('Digite a Nova Placa: ')
                            for car_id, car in cars.items():
                                if car_id != id and car['plate'] == new_plate:
                                    print('\nPlaca já cadastrada.\n')
                                    plate_exists = True
                                    break

                            if not plate_exists:
                                brand = input('Digite a Nova Marca: ')
                                model = input('Digite o Novo Modelo: ')
                                color = input('Digite a Nova Cor: ')
                                manufacturing_date = input('Digite o Novo Ano de Fabricação: ')
                                update_car(id, new_plate, brand, model, color, manufacturing_date)

                if sub_option_selected == 4:
                    if not cars:
                        print('\nNão há carros cadastrados.\n')
                    else:
                        id = int(input('Digite o ID do Carro: '))
                        if not find_car_by_id(id):
                            print('\nID Inválido !!!\n')
                        else:
                            delete_car(id)

            if option_selected == 2:
                if sub_option_selected not in sub_menu:
                    print('\nOpção Inválida !!!\n')
                    continue

                if sub_option_selected == 0:
                    break

                if sub_option_selected == 1:
                    cpf = input('Digite o CPF: ')
                    cpf_exists = False
                    for client_id, client in clients.items():
                        if client['cpf'] == cpf:
                            print('\nCPF já cadastrado.\n')
                            cpf_exists = True
                            break

                    if not cpf_exists:
                        name = input('Digite o Nome: ')
                        birth = input('Digite a Data de Nascimento: ')
                        phone = input('Digite o Telefone: ')
                        new_client(cpf, name, birth, phone)

                if sub_option_selected == 2:
                    if verify_empty_dict('clients'):
                        print('\nNão há clientes cadastrados !!!\n')
                    else:
                        list_clients()

                if sub_option_selected == 3:
                    if verify_empty_dict('clients'):
                        print('\nNão há clientes cadastrados !!!\n')
                    else:
                        id = int(input('Digite o ID do Cliente: '))
                        if not find_client_by_id(id):
                            print('\nID Inválido !!!\n')
                        else:
                            new_cpf = input('Digite o Novo CPF: ')
                            for client_id, client in clients.items():
                                if client_id != id and client['cpf'] == new_cpf:
                                    print('\nCPF já cadastrado.\n')
                                    cpf_exists = True
                                    break

                            if not cpf_exists:
                                name = input('Digite o Novo Nome: ')
                                birth = input('Digite a Nova Data de Nascimento: ')
                                phone = input('Digite o Novo Telefone: ')
                                update_client(id, new_cpf, name, birth, phone)

                if sub_option_selected == 4:
                    if verify_empty_dict('clients'):
                        print('\nNão há clientes cadastrados !!!\n')
                    else:
                        id = int(input('Digite o ID do Cliente: '))
                        if id not in clients:
                            print('\nID Inválido\n')
                        else:
                            delete_client(id)

                elif sub_option_selected == 0:
                    break

            if option_selected == 3:
                if sub_option_selected not in sub_menu:
                    print('\nOpção Inválida !!!\n')
                    continue

                if sub_option_selected == 0:
                    break

                if sub_option_selected == 1:
                    client_id = int(input('Digite o ID do Cliente: '))
                    if not find_client_by_id(client_id):
                        print('\nCliente não encontrado !!!\n')
                    else:

                        car_id = int(input('Digite o ID do Carro: '))
                        if not find_car_by_id(car_id):
                            print('\nCarro não encontrado !!!\n')
                            break
                        else:
                            initial_date = input('Digite a Data Inicial: ')
                            final_date = input('Digite a Data Final: ')
                            new_scheduling(client_id, car_id, initial_date, final_date)

                if sub_option_selected == 2:
                    if verify_empty_dict('schedules'):
                        print('\nAgendamentos não cadastrados !!!\n')
                    else:
                        list_schedules()

                if sub_option_selected == 3:
                    if verify_empty_dict('schedules'):
                        print('\nAgendamentos não cadastrados !!!\n')
                    else:
                        id = int(input('Digite o ID do Agendamento: '))
                        if not find_schedule_by_id(id):
                            print('\nID Inválido\n')
                        else:
                            client_id = int(input('Digite o ID do Novo Cliente: '))
                            if not find_client_by_id(client_id):
                                print('\nCliente não encontrado\n')
                                break

                            car_id = int(input('Digite o ID do Novo Carro: '))
                            if not find_car_by_id(car_id):
                                print('\nCarro não encontrado\n')
                                break

                            initial_date = input('Digite a Nova Data Inicial: ')
                            final_date = input('Digite a Nova Data Final: ')
                            update_schedule(id, client_id, car_id, initial_date, final_date)

                if sub_option_selected == 4:
                    if not schedules:
                        print('\nNão há Agendamentos cadastrados !!!\n')
                    else:
                        id = int(input('Digite o ID do Agendamento: '))
                        if not find_schedule_by_id(id):
                            print('\nID Inválido !!!\n')
                        else:
                            delete_schedule(id)

    except ValueError:
        print('\nOpção Inválida !!!\n')
