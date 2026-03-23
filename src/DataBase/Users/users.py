import os
from datetime import datetime

from src.DataBase.Users.model_route import model_route
from src.DataBase.sdk.sql_provider import SQLProvider

provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


def create_new_user(tg_id, username, first_name, second_name):
    model_result = model_route(provider, 'insert_new_user.sql',
                               [tg_id, username, first_name, second_name, datetime.now()])

    if model_result.status:
        print('Success add new user in db')
    else:
        print(f'Error add new user in db {model_result.err_msg}')

