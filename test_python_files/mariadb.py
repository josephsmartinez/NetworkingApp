# MariaDB Code
#from flask_sqlalchemy import SQLAlchemy
import mysql.connector as mariadb

def create_database():
  '''
  Create database unless present 
  '''
  # Handle errors if connection issues
  try:
    mariadb_connection = mariadb.connect(user='root', password='password', 
                                        host='127.0.0.1', database='netapi')

    cursor = mariadb_connection.cursor()
    number = 126
    cursor.execute("SELECT * FROM `users`")
    print(cursor)

    print(cursor.fetchall())

  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  else:
    mariadb_connection.close()


if __name__ == "__main__":
    create_database()

