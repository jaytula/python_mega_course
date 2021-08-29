# Get by: 'pip install mysql-connector-python'
import mysql.connector

from mysql.connector.connection_cext import CMySQLConnection

def main():
  con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
  )

  if isinstance(con, CMySQLConnection):
    cursor = con.cursor()

    word = input('Enter a word: ')
    query = cursor.execute("SELECT * FROM Dictionary Where Expression = '%s'" % word)
    results = cursor.fetchall()

    if results:
      for result in results:
        print(result[1])
    else:
      print('No word found!')

if __name__ == '__main__':
  main()