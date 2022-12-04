import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                               user='root',
                               password='root')

mycursor = mydb.cursor()
# ----------------------------------------------------------------------------------------------------------------------
#                                             CREATE DATABASE
# ----------------------------------------------------------------------------------------------------------------------

mycursor.execute("CREATE DATABASE IF NOT EXISTS social_media_database")
