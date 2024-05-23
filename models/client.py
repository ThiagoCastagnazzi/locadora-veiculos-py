import sqlite3


class Client:
    def __init__(self):
        self.db_filename = 'clients.db'
        self.conn = sqlite3.connect(self.db_filename)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS clients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cpf TEXT UNIQUE,
                    name TEXT,
                    birth TEXT,
                    phone TEXT
                )
            """)

    def create(self, cpf, name, birth, phone):
        cpf_exists = self.exists_with_this_cpf(cpf)

        if cpf_exists:
            return None, False

        with self.conn:
            cursor = self.conn.execute("""
                        INSERT INTO clients (cpf, name, birth, phone)
                        VALUES (?, ?, ?, ?)
                    """, (cpf, name, birth, phone))
            client_id = cursor.lastrowid
            return {'id': client_id, 'cpf': cpf, 'name': name, 'birth': birth, 'phone': phone}, True

    def list(self):
        cursor = self.conn.execute("SELECT id, cpf, name, birth, phone FROM clients")
        columns = [column[0] for column in cursor.description]
        clients = cursor.fetchall()
        return [dict(zip(columns, row)) for row in clients]

    def update(self, id, cpf, name, birth, phone):
        client_exists = self.get_by_id(id)
        if client_exists:
            with self.conn:
                self.conn.execute("""
                       UPDATE clients
                       SET cpf = ?, name = ?, birth = ?, phone = ?
                       WHERE id = ?
                   """, (cpf, name, birth, phone, id))
                return {'id': id, 'cpf': cpf, 'name': name, 'birth': birth, 'phone': phone}, True
        else:
            return None, False

    def delete(self, id):
        with self.conn:
            cursor = self.conn.execute("DELETE FROM clients WHERE id = ?", (id,))
            if cursor.rowcount > 0:
                return True
            else:
                return False

    def get_by_id(self, id):
        cursor = self.conn.execute("SELECT id, cpf, name, birth, phone FROM clients WHERE id = ?", (id,))
        row = cursor.fetchone()
        if row:
            return dict(zip([column[0] for column in cursor.description], row))
        return None

    def exists_with_this_cpf(self, cpf):
        cursor = self.conn.execute("SELECT 1 FROM clients WHERE cpf = ?", (cpf,))
        return cursor.fetchone()