class Client:
    def __init__(self):
        self.clients = {
            1: dict(id=1, cpf='07237395106', name='thiago castagnazzi', birth='04/10/1999', phone='67998309537')
        }

    def create(self, cpf, name, birth, phone):
        if self.exists_with_this_cpf(cpf):
            return None, False

        id = max(self.clients.keys()) + 1 if self.clients else 1

        self.clients[id] = dict(
            id=id,
            cpf=cpf,
            name=name,
            birth=birth,
            phone=phone
        )

        return self.clients, True

    def list(self):
        return [client for _, client in self.clients.items()]

    def update(self, id, cpf, name, birth, phone):
        if not self.exists_with_this_id(id):
            return None, False

        if self.exists_with_this_cpf(cpf):
            return None, False

        client = self.clients[id]
        client.update(
            id=id,
            cpf=cpf,
            name=name,
            birth=birth,
            phone=phone
        )

        return client, True

    def delete(self, id):
        if self.exists_with_this_id(id):
            del self.clients[id]
            return True
        else:
            return False

    def exists_with_this_cpf(self, cpf: str) -> bool:
        for _, client in self.clients.items():
            if client['cpf'] == cpf:
                return True

        return False

    def exists_with_this_id(self, id: int):
        return self.clients.get(id)

    def get_by_id(self, id):
        return self.clients.get(id)
