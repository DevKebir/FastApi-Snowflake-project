import snowflake.connector
from credentials import get_connect_info
from pydantic import BaseModel
from statements import st1, st2, st3, st4, t1, u1, u2, u3


class ProductTemp(BaseModel):
    Id : int
    Name : str
    Price : float


def create_connex():
    """Create a connection to Snowflake"""
    connect_info = get_connect_info()
    con = snowflake.connector.connect(
        user = connect_info['user'],
        password = connect_info['password'],
        account = connect_info['account']
    )
    cur = con.cursor()
    return con, cur
    


def create_schema():
    """Create the schema if it doesn't exist already."""
    _, cur = create_connex()
    try:
        cur.execute(st1)
        cur.execute(st2)
        cur.execute(st3)
        cur.execute(st4)
        print("schema created successfully")
    except  Exception as err:
        print("Error creating schema: {}".format(err))
    

def use_schema():
    """Use the earlier created schema."""
    _,cur = create_connex()
    try:
        cur.execute(u1)
        cur.execute(u2)
        cur.execute(u3)
        print('Switched to data_pipeline')
    except Exception as e:
        print("Couldn't switch to the schema: {}: ".format(e.msg))
    
def create_table():
    _,conn_tab = create_connex()
    """Create table  in current schema"""
    try:
        conn_tab.execute(t1)
        print("Table created successfully")
    except  Exception as e:
        print("Error creating table as : {}" .format(e.msg))



    

if __name__ == "__main__":
    create_connex()
    create_schema()
    #use_schema()
    create_table()

