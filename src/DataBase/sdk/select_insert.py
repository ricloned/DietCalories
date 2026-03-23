from src.DataBase.sdk.database import DBCM
from bot import CONFIG


def select(_sql, params):
    with DBCM(CONFIG['db_info']) as cursor:
        result = None
        if cursor is None:
            raise ValueError("Cursor not define")
        else:
            if params:
                cursor.execute(_sql, params)
                result = cursor.fetchall()
            else:
                cursor.execute(_sql)
                result = cursor.fetchall()
    return result