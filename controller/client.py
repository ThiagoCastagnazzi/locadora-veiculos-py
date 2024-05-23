from models import Client


class ClientController:
    def __init__(self):
        self.client = Client()

    def create(self, cpf, name, birth, phone):
        client, success = self.client.create(
            cpf=cpf,
            name=name,
            birth=birth,
            phone=phone
        )

        if success:
            return client, True
        else:
            return None, False

    def list(self):
        return self.client.list()

    def update(self, id, cpf, name, birth, phone):

        client, success = self.client.update(
            id=id,
            cpf=cpf,
            name=name,
            birth=birth,
            phone=phone
        )

        if success:
            return client, True
        else:
            return None, False

    def delete(self, id):
        deleted = self.client.delete(id)
        if deleted:
            return True
        else:
            return False
