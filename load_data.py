import pymysql
import pandas as pd


class songs_mysql(object):

    def __init__ (self, usr_name, password, address, port, database_name):
        self.user_name = usr_name
        self.password = password
        self.address = address
        self.port = port
        self.database_name = database_name

    def Read_database (self, sql):
        global df
        conn = pymysql.connect(host=self.address, user=self.user_name, passwd=self.password, \
                               db=self.database_name, port=int(self.port), charset="utf8mb4")
        try:
            df = pd.read_sql(sql, con=conn)

        except:
            print('\n Reading Error  \n')

        finally:
            conn.close()
        print('\n Completion of data reading \n')

        return df

    def Operating_database (self, sql):
        conn = pymysql.connect(host=slef.address, user=self.user_name, passwd=self.password, \
                               db=self.database_name, port=int(self.port), charset="utf8mb4")
        cur = conn.cursor()  
        try:
            cur.execute(sql)  
            conn.commit()  
            print('\n Completion of database operation \n')
        except Exception as e:
            conn.rollback()  
            print('\n Operation error \n')
        finally:
            conn.close()
