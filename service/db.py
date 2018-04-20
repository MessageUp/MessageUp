import sqlite3
from hashlib import md5
from service.crypt import encrypt, decrypt

class DB:
    def __init__(self):
        conn = sqlite3.connect('db.sqlite')
        try:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS Messages
            (key Text NOT NULL, message Text  NOT NULL)''')
        except:
            pass
        finally:
            conn.close()

    def get(self, key, id_):
        if not isinstance(id_, int):
            raise ValueError("Incorrect ID type")
        if not isinstance(key, str):
            raise ValueError("Incorrect key type")
        conn = sqlite3.connect('db.sqlite')
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT message FROM Messages WHERE rowid = %d AND key = '%s'" % (id_, key))
            message = cursor.fetchone()
            if not message:
                raise ValueError("Message not found for ID/Key pair")
            message = decrypt(message[0], key)
        except Exception as e:
            raise ValueError(e)
        finally:
            conn.close()

        return message

    def store(self, key, message):
        if not isinstance(message, str):
            raise ValueError("Incorrect Message type")
        if not isinstance(key, str):
            raise ValueError("Incorrect key type")
        message = encrypt(message, key)
        conn = sqlite3.connect('db.sqlite')
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Messages(key, message) VALUES ('%s', '%s')" % (key, message))
            rowid = cursor.lastrowid
            conn.commit()
        except Exception as e:
            raise ValueError(e)
        finally:
            conn.close()
        return rowid
