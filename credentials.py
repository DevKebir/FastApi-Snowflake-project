import os

from dotenv import load_dotenv

load_dotenv()

def get_connect_info():
    return {
            'user' : os.getenv("user"),
            'password' : os.getenv("password"),
            'account' : os.getenv("account")
            }


print(f"Connecting to: \n\tUser: {get_connect_info()['user']}\n\tAccount: {get_connect_info()['account']}")
#'warehouse' : os.getenv("warehouse"),
#'database' : os.getenv("dbname"),
#'schema' : os.getenv("schema")