import mysql.connector 


def database():
    global conn,cursor
    conn = mysql.connector.connect(host="localhost",user="pythonadmin",passwd="pythonpass")
    cursor=conn.cursor()

def lecture():
    sql="select * from etudiant"
    cursor.execute(sql)
    tab=cursor.fetchall()
    return(tab)