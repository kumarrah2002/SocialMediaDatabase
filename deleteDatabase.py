import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                               user='root',
                               password='root',
                               database='social_media_database')

mycursor = mydb.cursor()
# ----------------------------------------------------------------------------------------------------------------------
#                                               ERASE TABLES
# ----------------------------------------------------------------------------------------------------------------------
# mycursor.execute("SET FOREIGN_KEY_CHECKS=0; TRUNCATE TABLE user; TRUNCATE TABLE userfriend; TRUNCATE TABLE userpost;"
#                  "TRUNCATE TABLE userstore; TRUNCATE TABLE usermessage; TRUNCATE TABLE group_table; "
#                  "TRUNCATE TABLE grouppost; TRUNCATE TABLE groupfollower; TRUNCATE TABLE groupmember; "
#                  "TRUNCATE TABLE groupmessage; SET FOREIGN_KEY_CHECKS=1")

# ----------------------------------------------------------------------------------------------------------------------
#                                               DELETE DATABASE
# ----------------------------------------------------------------------------------------------------------------------

# mycursor.execute("DROP DATABASE IF EXISTS social_media_database")
