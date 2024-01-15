# Get by: 'pip install mysql-connector-python'
from typing import List, Tuple
import mysql.connector

from mysql.connector.connection_cext import CMySQLConnection
from mysql.connector.cursor_cext import CMySQLCursor

def main():
  con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
  )

  if isinstance(con, CMySQLConnection):
    cursor: CMySQLCursor = con.cursor()

    word = input('Enter a word: ')
    cursor.execute("SELECT * FROM Dictionary Where Expression = '%s'" % word)
    results: List[Tuple[str, str]] = cursor.fetchall()

    if results:
      for result in results:
        print(result[1])
    else:
      print('No word found!')

if __name__ == '__main__':
  main()