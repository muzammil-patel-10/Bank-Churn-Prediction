import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def insert_data(conn, tabel_name, project):
    """
    Create a new table in database 
    :param conn:
    :param project:
    :return: project id
    """
    sql = f''' INSERT INTO {tabel_name}(name,begin_date,end_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid



# def select_all_tasks(conn):
#     """
#     Query all rows in the tasks table
#     :param conn: the Connection object
#     :return:
#     """
#     cur = conn.cursor()
#     cur.execute("SELECT name FROM projects")

#     rows = cur.fetchall()

#     for row in rows:
#         print(row)


def main():
    database = r"sqllite1.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        insert_qury = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30');
        a = input("enter how many recode you wnat to insert ")
        print(a)
        if a == "no":
            pass
        else:
            for i in range(int(a)):
                
                print(f"\n recode {i+1}")
                s1 = (input("enter s1 "))
                d1 = (input("enter d1 "))
                d2 = (input("enter d2 "))

                insert_qury = (s1, d1, d2)
                insert_data(conn, insert_qury)
            

if __name__ == '__main__':
    main()