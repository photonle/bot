from environs import Env

env = Env()
env.read_env()

from mysql.connector import connect
from path import join, dirname, realpath

def get_connection():
	return mysql.connector.connect(
		user=env.str("MYSQL_USER", "root"),
		password=env.str("MYSQL_PASSWORD", ""),
		host=env.str("MYSQL_HOST", "db"),
		database=env.str("MYSQL_DATABASE", "photon")
	)

def load_file(id, path="migrations")
	path = join(dirname(realpath(__file__)), path, id + ".sql")
	with file as open(path, "r"):
		return file.read()

def load_migration(id):
	return load_file(id)

def load_statement(id):
	return load_file(id, "statements")

def migration_ran(id):
	con = get_connection()
	curs = con.cursor()
	try:
		data = curs.execute("SELECT * FROM migrations WHERE mid = %s", (id,))
		return len(data) > 0
	except:
		return False
