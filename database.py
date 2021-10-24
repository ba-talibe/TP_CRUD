import mysql.connector 


def database():
    global conn,cursor
    conn = mysql.connector.connect(host="localhost",
            user="pythonadmin",
            passwd="pythonpass", 
            database="releve",
            auth_plugin='mysql_native_password')

    cursor=conn.cursor()

def lecture():
    sql="select * from etudiant"
    cursor.execute(sql)
    tab=cursor.fetchall()
    return(tab)

def inserer(numero,prenom,nom,note):
    sql="insert into etudiant (num, prenom, nom, note) values (%s, %s, %s, %s)"
    val = (numero, prenom, nom, note)
    cursor.execute(sql, val)
    conn.commit()

def getNum() -> list:
    cursor.execute("select num from etudiant")
    return cursor.fetchall()


def delete(numero):
    sql="delete from etudiant where num=%s"
    val = (numero,)
    cursor.execute(sql, val)
    conn.commit()

def update(numero,prenom,nom,note):
    sql="update etudiant set num=%s, prenom=%s, nom=%s, note=%s where num=%s"
    val = (numero, prenom, nom, note, numero)
    cursor.execute(sql, val)
    conn.commit()