clients = {
    1: {'id': 1, 'cpf': '07237395106', 'name': 'thiago castagnazzi', 'birth': '04/10/1999', 'phone': '67998309537'}
}

class ClientController:
    def exists_with_this_cpf(self, cpf: str) -> bool:
        for _, client in clients.items():
            if client['cpf'] == cpf:
                return True

        return False

    def exists_with_this_id(self, id: int):
        return clients.get(id)

    def create(self, cpf, name, birth, phone):
        cpf_exists = self.exists_with_this_cpf(cpf)

        if not cpf_exists:
            if clients:
                id = max(clients.keys()) + 1
            else:
                id = 1

            clients[id] = dict(
                id=id,
                cpf=cpf,
                name=name,
                birth=birth,
                phone=phone
            )

            return clients, True
        else:
            return None, False

    def list(self):
        return [client for _, client in clients.items()]

    def update(self, id, cpf, name, birth, phone):
        cpf_exists = self.exists_with_this_cpf(cpf)

        if not cpf_exists:
            clients[id] = dict(
                id=id,
                cpf=cpf,
                name=name,
                birth=birth,
                phone=phone
            )

            return clients, True
        else:
            return None, False

    def delete(self, id):
        del clients[id]
