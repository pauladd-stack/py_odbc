import pyodbc
from config import save_config

class odbc_class():
    dsn: str
    uid: str
    pwd: str
    table: str
    conn_str: str

    def __init__(self, _dsn: str, _uid: str, _pwd: str, _table: str) -> None:
        self.dsn=_dsn
        self.uid=_uid
        self.pwd=_pwd
        self.table=_table
        self.conn_str=self.mk_conn_str()
        save_config(self.dsn, self.uid, self.pwd, self.table)

    def mk_conn_str(self):
        # CONNECTION_STRING="DSN=TestODBC;UID=test;PWD=test"
        connection_string: str = f'DSN={self.dsn}'
        if self.uid:
            connection_string = f'DSN={self.dsn};UID={self.uid};PWD={self.pwd}'
        
        return connection_string
    
    def execute(self)->str | list:
        
        try:
            conn = pyodbc.connect(self.conn_str, readonly=True, autocommit=True)
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self.table}")
            rows = cursor.fetchall()
            label = f"Success!\nSELECT * FROM {self.table}"

            cursor.close()
            conn.close()

            return label, rows

        except pyodbc.Error as e:
            label = f"FAILED\nwith config:\n {self.conn_str} \n {e.args[0]} \n {e.args[1]}"
            rows = [["...", "...", "..."]]
            return label, rows
    
    def __del__(self):
        print('deleted')

    