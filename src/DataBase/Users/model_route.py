from dataclasses import dataclass

from src.DataBase.sdk.select_insert import select


@dataclass
class RouteResult:
    result: dict
    status: bool
    err_msg: str

def model_route(provider, sql_name, params):
    err_message = ''
    _sql = provider.get(sql_name)
    print(params)
    result = select(_sql, params)
    print(result)
    if result:
        return RouteResult(result, True, err_message)
    else:
        err_message = 'Данные не получены'
        return RouteResult(result, False, err_message)