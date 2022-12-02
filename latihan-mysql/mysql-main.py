from mysql.connector import connect,Error
from mysql_config import host,username,password,database


mydb = connect(
        host=host,
        user=username,
        password=password,
        database=database
        # when connect with database with low security (SSL not configured)
        # ssl_disabled= True
    )

mycursor = mydb.cursor()

mycursor.execute(f"{insert_query_here}")

myresult = mycursor.fetchall()
print(myresult)