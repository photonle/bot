from os import listdir
from os.path import isfile, join, splitext, dirname, realpath
from .shared import load_file, get_connection


def load_migration(id):
    return load_file(id)


def migration_ran(id):
    con = get_connection()
    curs = con.cursor()
    try:
        data = curs.execute("SELECT * FROM migrations WHERE mid = %s", (id,))
        return id == "init" and True or (len(data) > 0)
    except:
        return False


def migration(id, curs):
    curs.execute(load_migration(id))


def migrate():
    con = get_connection()
    curs = con.cursor()

    curs.execute("SET autocommit = OFF;")
    curs.execute("START TRANSACTION;")

    base_path = join(dirname(realpath(__file__)), "migrations")
    migrations = [file for file in listdir(base_path) if isfile(join(base_path, file))]
    migrations.sort()

    try:
        if not migration_ran("init"):
            migration("init", curs)

        for mig in migrations:
            pair = splitext(mig)
            id = pair[0]
            print("Checking migration", mig)
            if not migration_ran(id):
                print("\tmigration", mig)
                migration(id, curs)
    except:
        curs.execute("ROLLBACK;")
        raise
    else:
        curs.execute("COMMIT;")
    finally:
        curs.close()
