from controller import CarController
from controller import ClientController
from controller import ScheduleController
from utils import utils as utils_controller

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

                    plate_exists = car_controller.exists_with_this_plate(plate)

                    if plate_exists:
                        print('\nPlaca já cadastrada.\n')

                    if not plate_exists:
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
                    if utils_controller.verify_empty_dict('cars'):
                        print('\nNão há carros cadastrados !!!\n')
                    else:
                        print("\nLista de Carros:")
                        for car in car_controller.list():
                            print(f"ID: {car['id']}")
                            print(f"Placa: {car['plate']}")
                            print(f"Marca: {car['brand']}")
                            print(f"Modelo: {car['model']}")
                            print(f"Cor: {car['color']}")
                            print(f"Ano de Fabricação: {car['manufacturing_date']}\n")


                if sub_option_selected == 3:
                    if utils_controller.verify_empty_dict('cars'):
                        print('\nNão há carros cadastrados !!!\n')
                    else:
                        id = int(input('Digite o ID do Carro: '))

                        if not car_controller.exists_with_this_id(id):
                            print('\nID Inválido !!!\n')
                        else:
                            new_plate = input('Digite a Nova Placa: ')

                            plate_exists = car_controller.exists_with_this_plate(new_plate)

                            if plate_exists:
                                print('\nPlaca já cadastrada.\n')
                                break

                            if not plate_exists:
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
                    if utils_controller.verify_empty_dict('cars'):
                        print('\nNão há carros cadastrados !!!\n')
                    else:
                        id = int(input('Digite o ID do Carro: '))
                        if not car_controller.exists_with_this_id(id):
                            print('\nID Inválido !!!\n')
                        else:
                            car_controller.delete(id)
                            print('\nCarro Deletado com sucesso !!!\n')

            if option_selected == 2:
                if sub_option_selected not in sub_menu:
                    print('\nOpção Inválida !!!\n')
                    continue

                if sub_option_selected == 0:
                    break

                if sub_option_selected == 1:
                    cpf = input('Digite o CPF: ')

                    cpf_exists = client_controller.exists_with_this_cpf(cpf)

                    if cpf_exists:
                        print('\nCPF já cadastrado !!!\n')

                    if not cpf_exists:
                        name = input('Digite o Nome: ')
                        birth = input('Digite a Data de Nascimento: ')
                        phone = input('Digite o Telefone: ')
                        _, created = client_controller.create(cpf, name, birth, phone)
                        if created:
                            print('\nCliente adicionado com sucesso !!!\n')
                        else:
                            print('\nO cliente não pode ser adicionado !!!\n')

                if sub_option_selected == 2:
                    if utils_controller.verify_empty_dict('clients'):
                        print('\nNão há clientes cadastrados !!!\n')
                    else:
                        print("Lista de Clientes:")
                        for client in client_controller.list():
                            print(f"ID: {client['id']}")
                            print(f"CPF: {client['cpf']}")
                            print(f"Nome: {client['name']}")
                            print(f"Data de Nascimento: {client['birth']}")
                            print(f"Telefone: {client['phone']}\n")


                if sub_option_selected == 3:
                    if utils_controller.verify_empty_dict('clients'):
                        print('\nNão há clientes cadastrados !!!\n')
                    else:
                        id = int(input('Digite o ID do Cliente: '))
                        if not client_controller.exists_with_this_id(id):
                            print('\nID Inválido !!!\n')
                        else:
                            new_cpf = input('Digite o Novo CPF: ')
                            cpf_exists = client_controller.exists_with_this_cpf(new_cpf)

                            if cpf_exists:
                                print('\nCPF já cadastrado !!!\n')

                            if not cpf_exists:
                                name = input('Digite o Novo Nome: ')
                                birth = input('Digite a Nova Data de Nascimento: ')
                                phone = input('Digite o Novo Telefone: ')
                                _, updated = client_controller.update(id, new_cpf, name, birth, phone)
                                if updated:
                                    print('\nCliente Atualizado com sucesso !!!\n')
                                else:
                                    print('\nO cliente não pode ser atualizado !!!\n')

                if sub_option_selected == 4:
                    if utils_controller.verify_empty_dict('clients'):
                        print('\nNão há clientes cadastrados !!!\n')
                    else:
                        id = int(input('Digite o ID do Cliente: '))

                        if not client_controller.exists_with_this_id(id):
                            print('\nID Inválido !!!\n')
                        else:
                            client_controller.delete(id)
                            print('\nCliente Deletado com sucesso !!!\n')

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
                    if not client_controller.exists_with_this_id(client_id):
                        print('\nCliente não encontrado !!!\n')
                    else:

                        car_id = int(input('Digite o ID do Carro: '))
                        if not car_controller.exists_with_this_id(car_id):
                            print('\nCarro não encontrado !!!\n')
                            break
                        else:
                            initial_date = input('Digite a Data Inicial: ')
                            final_date = input('Digite a Data Final: ')
                            schedule_controller.create(client_id, car_id, initial_date, final_date)
                            print('\nAgendamento feito com sucesso !!!\n')

                if sub_option_selected == 2:
                    if utils_controller.verify_empty_dict('schedules'):
                        print('\nAgendamentos não cadastrados !!!\n')
                    else:
                        print("Lista de Agendamento:")
                        for schedule in schedule_controller.list():
                            print(f'ID: {schedule['id']}')
                            print(f'CPF do Cliente: {schedule["client_cpf"]}')
                            print(f'Placa do Carro: {schedule["car_plate"]}')
                            print(f'Data Inicial: {schedule["initial_date"]}')
                            print(f'Data Final: {schedule["final_date"]}\n')

                if sub_option_selected == 3:
                    if utils_controller.verify_empty_dict('schedules'):
                        print('\nAgendamentos não cadastrados !!!\n')
                    else:
                        id = int(input('Digite o ID do Agendamento: '))
                        if not schedule_controller.exists_with_this_id(id):
                            print('\nID Inválido\n')
                        else:
                            client_id = int(input('Digite o ID do Novo Cliente: '))
                            if not client_controller.exists_with_this_id(client_id):
                                print('\nCliente não encontrado\n')
                                break

                            car_id = int(input('Digite o ID do Novo Carro: '))
                            if not car_controller.exists_with_this_id(car_id):
                                print('\nCarro não encontrado\n')
                                break

                            initial_date = input('Digite a Nova Data Inicial: ')
                            final_date = input('Digite a Nova Data Final: ')
                            schedule_controller.update(id, client_id, car_id, initial_date, final_date)
                            print('\nAgendamento Atualizado com Sucesso !!!\n')

                if sub_option_selected == 4:
                    if not utils_controller.verify_empty_dict('schedules'):
                        print('\nNão há Agendamentos cadastrados !!!\n')
                    else:
                        id = int(input('Digite o ID do Agendamento: '))
                        if not schedule_controller.exists_with_this_id(id):
                            print('\nID Inválido !!!\n')
                        else:
                            schedule_controller.delete(id)
                            print('\nAgendamento Deletado com sucesso !!!\n')

    except ValueError:
        print('\nOpção Inválida !!!\n')
