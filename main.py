from controller import CarController
from controller import ClientController
from controller import ScheduleController

menu_options = {1: 'Carro', 2: 'Cliente', 3: 'Agendamento', 0: 'Sair'}
sub_menu = {1: 'Criar', 2: 'Listar', 3: 'Atualizar', 4: 'Deletar', 0: 'Voltar'}

car_controller = CarController()
client_controller = ClientController()
schedule_controller = ScheduleController()

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
                    brand = input('Digite a Marca: ')
                    model = input('Digite o Modelo: ')
                    color = input('Digite a Cor: ')
                    manufacturing_date = input('Digite o Ano de Fabricação: ')
                    _, created = car_controller.create(plate, brand, model, color, manufacturing_date)

                    if created:
                        print('\nCarro adicionado com sucesso !!!\n')

                    else:
                        print('\nO carro não pode ser adicionado !!!\n')

                if sub_option_selected == 2:
                    cars = car_controller.list()
                    if len(cars) == 0:
                        print('\nNão há carros cadastrados !!!\n')
                    else:
                        print("\nLista de Carros:")
                        for car in cars:
                            print(f"ID: {car['id']}")
                            print(f"Placa: {car['plate']}")
                            print(f"Marca: {car['brand']}")
                            print(f"Modelo: {car['model']}")
                            print(f"Cor: {car['color']}")
                            print(f"Ano de Fabricação: {car['manufacturing_date']}\n")

                if sub_option_selected == 3:
                    id = int(input('Digite o ID do Carro: '))
                    new_plate = input('Digite a Nova Placa: ')
                    brand = input('Digite a Nova Marca: ')
                    model = input('Digite o Novo Modelo: ')
                    color = input('Digite a Nova Cor: ')
                    manufacturing_date = input('Digite o Novo Ano de Fabricação: ')
                    _, updated = car_controller.update(id, new_plate, brand, model, color, manufacturing_date)
                    if updated:
                        print('\nCarro Atualizado com sucesso !!!\n')
                    else:
                        print('\nO carro não pode ser atualizado !!!\n')

                if sub_option_selected == 4:
                    id = int(input('Digite o ID do Carro: '))
                    deleted = car_controller.delete(id)
                    if deleted:
                        print('\nCarro Deletado com sucesso !!!\n')
                    else:
                        print('\nNão foi possível deletar o carro !!!\n')

            if option_selected == 2:
                if sub_option_selected not in sub_menu:
                    print('\nOpção Inválida !!!\n')
                    continue

                if sub_option_selected == 0:
                    break

                if sub_option_selected == 1:
                    cpf = input('Digite o CPF: ')
                    name = input('Digite o Nome: ')
                    birth = input('Digite a Data de Nascimento: ')
                    phone = input('Digite o Telefone: ')
                    _, created = client_controller.create(cpf, name, birth, phone)
                    if created:
                        print('\nCliente adicionado com sucesso !!!\n')
                    else:
                        print('\nO cliente não pode ser adicionado !!!\n')

                if sub_option_selected == 2:
                    clients = client_controller.list()
                    if len(clients) == 0:
                        print('\nNão há clientes cadastrados !!!\n')
                    else:
                        print("Lista de Clientes:")
                        for client in clients:
                            print(f"ID: {client['id']}")
                            print(f"CPF: {client['cpf']}")
                            print(f"Nome: {client['name']}")
                            print(f"Data de Nascimento: {client['birth']}")
                            print(f"Telefone: {client['phone']}\n")

                if sub_option_selected == 3:
                    id = int(input('Digite o ID do Cliente: '))
                    new_cpf = input('Digite o Novo CPF: ')
                    name = input('Digite o Novo Nome: ')
                    birth = input('Digite a Nova Data de Nascimento: ')
                    phone = input('Digite o Novo Telefone: ')
                    _, updated = client_controller.update(id, new_cpf, name, birth, phone)
                    if updated:
                        print('\nCliente Atualizado com sucesso !!!\n')
                    else:
                        print('\nO cliente não pode ser atualizado !!!\n')

                if sub_option_selected == 4:
                    id = int(input('Digite o ID do Cliente: '))
                    deleted = client_controller.delete(id)
                    if deleted:
                        print('\nCliente Deletado com sucesso !!!\n')
                    else:
                        print('\nNão foi possível deletar o cliente !!!\n')

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
                    car_id = int(input('Digite o ID do Carro: '))
                    initial_date = input('Digite a Data Inicial: ')
                    final_date = input('Digite a Data Final: ')
                    _, created = schedule_controller.create(client_id, car_id, initial_date, final_date)
                    if created:
                        print('\nAgendamento feito com sucesso !!!\n')
                    else:
                        print('\nNão foi possível fazer o Agendamento !!!\n')

                if sub_option_selected == 2:
                    schedules = schedule_controller.list()
                    if len(schedules) == 0:
                        print('\nAgendamentos não cadastrados !!!\n')
                    else:
                        print("Lista de Agendamento:")
                        for schedule in schedules:
                            print(f'ID: {schedule['id']}')
                            print(f'CPF do Cliente: {schedule["client_cpf"]}')
                            print(f'Placa do Carro: {schedule["car_plate"]}')
                            print(f'Data Inicial: {schedule["initial_date"]}')
                            print(f'Data Final: {schedule["final_date"]}\n')

                if sub_option_selected == 3:
                    id = int(input('Digite o ID do Agendamento: '))
                    client_id = int(input('Digite o ID do Novo Cliente: '))
                    car_id = int(input('Digite o ID do Novo Carro: '))
                    initial_date = input('Digite a Nova Data Inicial: ')
                    final_date = input('Digite a Nova Data Final: ')
                    _, updated = schedule_controller.update(id, client_id, car_id, initial_date, final_date)
                    if updated:
                        print('\nAgendamento Atualizado com Sucesso !!!\n')
                    else:
                        print('\nNão foi possível atualizar o Agendamento !!!\n')

                if sub_option_selected == 4:
                    id = int(input('Digite o ID do Agendamento: '))
                    deleted = schedule_controller.delete(id)
                    if deleted:
                        print('\nAgendamento Deletado com sucesso !!!\n')
                    else:
                        print('\nNão foi possível deletar o Agendamento !!!\n')

    except ValueError:
        print('\nOpção Inválida !!!\n')
