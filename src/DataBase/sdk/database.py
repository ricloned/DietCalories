from pymysql import connect, OperationalError

class DBCM:
    def __init__(self, db_connect: dict):
        self.conn= None
        self.cursor = None
        self.db_connect = db_connect
    def __enter__(self):
        try:
            self.conn = connect(**self.db_connect)
            self.cursor = self.conn.cursor()
            self.conn.begin()
            return self.cursor
        except Exception as e:
            print('Error', e)
            return None
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            if exc_type:
                self.conn.rollback()
            else:
                self.conn.commit()
            self.cursor.close()
        self.conn.close()
        return True