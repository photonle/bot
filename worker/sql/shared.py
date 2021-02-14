from environs import Env

env = Env()
env.read_env()

from mysql.connector import connect
from os.path import join, dirname, realpath


def get_connection():
    return connect(
        user=env.str("MYSQL_USER", "root"),
        password=env.str("MYSQL_PASSWORD", ""),
        host=env.str("MYSQL_HOST", "db"),
        database=env.str("MYSQL_DATABASE", "photon")
    )


def load_file(id, path="migrations"):
    path = join(dirname(realpath(__file__)), path, id + ".sql")
    with open(path, "r") as file:
        return file.read()


def load_statement(id, data=None, path="migrations"):
    if data is None:
        data = {}

    content = load_file(id, path)
    for key in data.keys():
        k = "{{" + key + "}}"
        v = data[key]
        content = content.replace(k, v)
    return content
