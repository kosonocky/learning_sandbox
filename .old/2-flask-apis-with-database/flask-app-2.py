import sqlite3
from sqlite3 import Error, sqlite_version
import flask
from flask import g, request
import json
import requests as req

app = flask.Flask(__name__)
app.config["DEBUG"] = True

DATABASE = r'pythonsqlite.db'


@app.route('/', methods=['GET'])
def index():
    return f'This is the homepage!'


@app.route('/api', methods=['GET', 'POST', 'PUT'])
def api_receiving():
    receieved_dictionary = request.args.to_dict()
    keys_list = list(receieved_dictionary.keys())
    values_list = list(receieved_dictionary.values())
    returned_string_keys = 'Keys are '
    returned_string_values = ', and the Values are '
    for k in range(len(values_list)):
        returned_string_keys += f'{keys_list[k]}'
        returned_string_values += f'{values_list[k]}'
        if k != len(values_list) - 1:
            returned_string_keys += ', '
            returned_string_values += ', '
    print("THIS IS BEING RUN!")

    returned_string = returned_string_keys + returned_string_values
    return f'{returned_string}'


# def create_connection(db_file):
#     """
#     Create a database connection to a new SQLite database
#     """
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#         print(sqlite_version)
#     except Error as e:
#         print(e)
#     finally:
#         if conn:
#             conn.close()


# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     return db

# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()
if __name__ == '__main__':
    # create_connection(r"pythonsqlite.db")
    app.run(debug=True, port=8080)
