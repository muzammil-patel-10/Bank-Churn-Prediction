import sqlite3
from sqlite3 import Error


custd={'CreditScore': '343', 'Geography': 'France', 'Gender': 'Female', 'Age': '34', 'Tenure': '34', 'Balance': '322222222222', 'NumOfProducts': '2', 'HasCrCard': '1', 'IsActiveMember': '1', 'EstimatedSalary': '345'}
c_id = "272"
CreditScore = custd['CreditScore']
Geography = custd['Geography']
Gender = custd['Gender']
Age = custd['Age']
Tenure = custd['Tenure']
Balance = custd['Balance']
NumOfProducts = custd['NumOfProducts']
HasCrCard = custd['HasCrCard']
IsActiveMember = custd['IsActiveMember']
EstimatedSalary = custd['EstimatedSalary']
pred = "yeessss"




def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("con done")
    except Error as e:
        print(e)

    return conn


def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO df_pred_info(c_id,CreditScore,Geography,Gender,Age,
    Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary,Exited)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

# db funtions end 
# def insert_data_into_table_with_conn(conn, project):
#     with conn:
#         create_project(conn, project)




database = r"../db/sqlite1.db"
# create a database connection
conn = create_connection(database)
project = (c_id, CreditScore, Geography, Gender, 
           Age, Tenure, Balance, NumOfProducts, 
           HasCrCard, IsActiveMember, EstimatedSalary, pred);
create_project(conn, project)


# isd(conn, project)

# def isd(con, porj):

# with conn:
#     project = (c_id, CreditScore, Geography, Gender, 
#                Age, Tenure, Balance, NumOfProducts, 
#                HasCrCard, IsActiveMember, EstimatedSalary, pred);
#     create_project(conn, project)
