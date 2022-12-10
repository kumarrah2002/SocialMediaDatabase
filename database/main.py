# ----------------------------------------------------------------------------------------------------------------------
#                                             IMPORT LIBRARIES
# ----------------------------------------------------------------------------------------------------------------------
import mysql.connector
import names
import random
import string
import datetime
from essential_generators import DocumentGenerator
import os
import glob


# ----------------------------------------------------------------------------------------------------------------------
#                                        CONNECT TO MYSQL WORKBENCH
# ----------------------------------------------------------------------------------------------------------------------

# Global variables are dangerous. Store this in a main method or external file
mydb = mysql.connector.connect(host='localhost',
                               user='root',
                               password='root',
                               database='social_media_database')

mycursor = mydb.cursor()

# ----------------------------------------------------------------------------------------------------------------------
#                                             CREATE DATABASE
# ----------------------------------------------------------------------------------------------------------------------

mycursor.execute("CREATE DATABASE IF NOT EXISTS social_media_database")

# ----------------------------------------------------------------------------------------------------------------------
#                                               DEFINE USER TABLES
# ----------------------------------------------------------------------------------------------------------------------


# All of this is in-secure. Keep your queries in .sql files and call them like this: https://stackoverflow.com/questions/19472922/reading-external-sql-script-in-python
user = 'CREATE TABLE IF NOT EXISTS user (id bigint(20) PRIMARY KEY AUTO_INCREMENT, firstname varchar(45) NOT NULL, ' \
       'lastname varchar(45) NOT NULL, username varchar(45) NOT NULL UNIQUE, phone varchar(45), ' \
       'email varchar(45) NOT NULL, password varchar(45) NOT NULL, birthday DATETIME, age int, ' \
       'registerdate DATETIME NOT NULL, lastLogin DATETIME NOT NULL, bio TEXT, profilepic longblob)'

userFriend = 'CREATE TABLE IF NOT EXISTS userFriend (friendshipid bigint(20) PRIMARY KEY AUTO_INCREMENT, ' \
             'id bigint(20), friendid bigint(20) NOT NULL, username varchar(45) NOT NULL, ' \
             'friendusername varchar(45) NOT NULL,' \
             'type enum("Friend", "Close Friend"), createDate DATETIME NOT NULL, ' \
             'FOREIGN KEY (id) REFERENCES user(id)) AUTO_INCREMENT = 1000000'

userStore = 'CREATE TABLE IF NOT EXISTS userStore (itemid bigint(20) PRIMARY KEY AUTO_INCREMENT, id bigint(' \
            '20), itemName varchar(45) NOT NULL, cost bigint(20) NOT NULL, description TEXT, ' \
            'shippingDate DATETIME NOT NULL, shippingCost bigint(20), productReviews varchar(150), ' \
            'FOREIGN KEY (id) REFERENCES user(id)) AUTO_INCREMENT = 2000000'

# creates userPost
create_userPost = 'CREATE TABLE IF NOT EXISTS userPost (' \
                  'postID bigint(20) PRIMARY KEY AUTO_INCREMENT,' \
                  'id bigint(20),' \
                  'post longblob NOT NULL,' \
                  'textField TEXT,' \
                  'createDate DATETIME NOT NULL,' \
                  'updateDate DATETIME,' \
                  'FOREIGN KEY (id) REFERENCES user(id))  AUTO_INCREMENT = 3000000'
# creates userMessage
create_userMessage = 'CREATE TABLE IF NOT EXISTS userMessage (' \
                     'messageID bigint(20) PRIMARY KEY AUTO_INCREMENT,' \
                     'id bigint(20),' \
                     'targetID bigint(20) NOT NULL,' \
                     'message TEXT NOT NULL,' \
                     'createDate DATETIME NOT NULL,' \
                     'FOREIGN KEY (id) REFERENCES user(id)) AUTO_INCREMENT = 4000000'

# EDIT 1
mycursor.execute(user)
mycursor.execute(create_userPost)
mycursor.execute(create_userMessage)
mycursor.execute(userFriend)
mycursor.execute(userStore)

# ----------------------------------------------------------------------------------------------------------------------
#                                               DEFINE GROUP TABLES
# ----------------------------------------------------------------------------------------------------------------------


# EDIT 2

# group table
group = 'CREATE TABLE IF NOT EXISTS group_table(' \
        'groupID bigint(20) PRIMARY KEY AUTO_INCREMENT,' \
        'createdBy bigint(20) NOT NULL,' \
        'updatedBy bigint(20),' \
        'title TINYTEXT NOT NULL,' \
        'summary TEXT NOT NULL,' \
        'createDate DATETIME NOT NULL,' \
        'updateDate DATETIME,' \
        'size INT NOT NULL,' \
        'status enum("Open", "Closed") NOT NULL,' \
        'FOREIGN KEY (createdBy) REFERENCES user(id),' \
        'FOREIGN KEY (updatedBy) REFERENCES user(id)) '

groupMember = "CREATE TABLE IF NOT EXISTS groupMember(" \
              "groupID bigint(20) NOT NULL," \
              "userID bigint(20) NOT NULL," \
              "role enum('Member', 'Administrator', 'None') NOT NULL," \
              "FOREIGN KEY (groupID) REFERENCES group_table(groupID)," \
              "FOREIGN KEY (userID) REFERENCES user(id))"

groupFollower = "CREATE TABLE IF NOT EXISTS groupFollower(" \
                "groupID bigint(20) NOT NULL, " \
                "userID BIGINT(20) NOT NULL," \
                "follower enum('Following', 'Not Following') NOT NULL," \
                "FOREIGN KEY (groupID) REFERENCES group_table(groupID)," \
                "FOREIGN KEY (userID) REFERENCES user(id))"

groupMessage = 'CREATE TABLE IF NOT EXISTS groupMessage (ID BIGINT(20) PRIMARY KEY AUTO_INCREMENT,' \
               'groupID BIGINT(20) NOT NULL,' \
               'creatorID BIGINT(20) NOT NULL,' \
               'message text NOT NULL,' \
               'createDate DATETIME NOT NULL,' \
               'FOREIGN KEY (groupID) REFERENCES group_table(groupID),' \
               'FOREIGN KEY (creatorID) REFERENCES user(id)) AUTO_INCREMENT = 1000000'

groupPost = 'CREATE TABLE IF NOT EXISTS groupPost (ID BIGINT(20) PRIMARY KEY AUTO_INCREMENT, ' \
            'groupID BIGINT(20) NOT NULL,' \
            'userID BIGINT(20) NOT NULL,' \
            'post longblob NOT NULL,' \
            'message text,' \
            'createDate DATETIME NOT NULL,' \
            'FOREIGN KEY (groupID) REFERENCES group_table(groupID),' \
            'FOREIGN KEY (userID) REFERENCES user(id)) AUTO_INCREMENT = 2000000'

mycursor.execute(group)
mycursor.execute(groupMember)
mycursor.execute(groupFollower)
mycursor.execute(groupMessage)
mycursor.execute(groupPost)

# ----------------------------------------------------------------------------------------------------------------------
#                                               DEFINE FUNCTIONS
# ----------------------------------------------------------------------------------------------------------------------


# EDIT 3
gen = DocumentGenerator()


def create_username(first, last, number):
    username = first + "_" + last + str(number)
    return str(username)


def create_password():
    password_length = 8
    characters = string.ascii_letters + string.digits
    password = ""
    for index in range(password_length):
        password = password + random.choice(characters)

    return password


def date():
    year = random.randrange(2010, 2022)
    month = random.randrange(1, 12)
    if month == 2:
        day = random.randrange(1, 28)
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        day = random.randrange(1, 30)
    else:
        day = random.randrange(1, 31)
    return datetime.datetime(year, month, day).strftime('%Y-%m-%d')


def user_date():
    register = date()
    login = date()
    while register > login:
        register = date()
        login = date()
    else:
        return register, login


def birthday():
    year = random.randrange(1933, 2009)  # At least 13 years old to use app
    month = random.randrange(1, 12)
    if month == 2:
        day = random.randrange(1, 28)
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        day = random.randrange(1, 30)
    else:
        day = random.randrange(1, 31)

    age = 2022 - year
    return datetime.datetime(year, month, day).strftime('%Y-%m-%d'), age


def item():
    items = ['chair', 'computer', 'desk', 'car', 'dresser', 'speakers', 'iphone']
    index = random.randrange(0, len(items) - 1)
    return items[index]


def get_id(username):
    mycursor.execute("SELECT id FROM user where username = %s", (username,))
    userfriendid = mycursor.fetchone()
    return int(userfriendid[0])


def get_username(input_id):
    mycursor.execute("SELECT username FROM user where id = %s", (input_id,))
    user = mycursor.fetchone()
    return user[0]


def get_friend_id(userid, upper):
    target_id = random.randint(1, upper)
    while userid == target_id:
        target_id = random.randint(1, upper)
    return target_id


def convert_image(file):
    with open(file, 'rb') as f:
        binarydata = f.read()
    return binarydata


def generate_image():
    # Download the photos at https://www.kaggle.com/c/dogs-vs-cats/data?select=test1.zip
    # Place the images into a folder and change the directory given below
    directory = r"C:\Users\kumar\OneDrive\Documents\Databases\images"
    os.chdir(directory)
    pic = random.choice(glob.glob("*.jpg"))
    pic = convert_image(pic)
    return pic


def status(option1, option2):
    rand = random.randrange(0, 2)
    if rand == 0:
        return option1
    else:
        return option2


def get_rows(table):
    query = "SELECT COUNT(*) FROM " + table
    mycursor.execute(query)
    rows = mycursor.fetchone()
    return rows[0]


# EDIT 4 ( add a main method )

# ----------------------------------------------------------------------------------------------------------------------
#                                               DATA INSERTION
# ----------------------------------------------------------------------------------------------------------------------
iterations = 100
for i in range(iterations):
    num = random.randrange(0, 999999)
    first = names.get_first_name()
    last = names.get_last_name()
    email = gen.email()
    username_gen = create_username(first, last, num)
    password = create_password()
    register, login = user_date()
    phone_num = gen.phone()
    bio = gen.sentence()
    picture = generate_image()
    birthdate, age = birthday()

    # -----------------------------------------------USER TABLE---------------------------------------------------------
    user_sql = "INSERT INTO user (firstname, lastname, username, phone, email, password, birthday, age," \
               "registerdate, lastlogin, bio, profilepic) " \
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    user_data = (first, last, username_gen, phone_num, email, password,
                 birthdate, age, register, login, str(bio), picture)

    mycursor.execute(user_sql, user_data)
    mydb.commit()

    # -----------------------------------------------USER FRIEND TABLE--------------------------------------------------
    user_friend_sql = "INSERT INTO userfriend (id, friendid, username, friendusername, type, createdate) " \
                      "VALUES (%s , %s, %s, %s, %s, %s)"
    userid = get_id(username_gen)

    rows = get_rows("user")

    if i == 0:
        friend_id = 1
    else:
        friend_id = get_friend_id(userid, rows)
    friend_username = get_username(friend_id)
    user_friend_data = (userid, friend_id, username_gen, friend_username, status("Friend", "Close Friend"), date())
    mycursor.execute(user_friend_sql, user_friend_data)

    # -----------------------------------------------USER STORE TABLE---------------------------------------------------

    user_store_sql = "INSERT INTO userstore (id, itemname, cost, description, shippingdate, shippingcost, productreviews)" \
                     "VALUES (%s , %s, %s, %s, %s, %s, %s)"
    item_name = item()
    if item_name == 'car':
        cost = random.randrange(2000, 200000)
        shippingcost = 1000
    else:
        cost = random.randrange(1, 200)
        shippingcost = random.randrange(0, 25)
    description = gen.sentence()
    shippingdate = date()

    review = random.randrange(0, 5) + 1
    productreview = str(review) + " stars"

    user_store_data = (userid, item_name, cost, str(description), shippingdate, shippingcost, productreview)
    mycursor.execute(user_store_sql, user_store_data)

    # -----------------------------------------------USER POST TABLE----------------------------------------------------
    user_post_sql = "INSERT INTO userpost (id, post, textfield, createdate, updatedate)" \
                    "VALUES (%s, %s, %s, %s, %s)"
    textfield = gen.sentence()
    create, update = user_date()
    user_post_data = (userid, picture, str(textfield), create, update)
    mycursor.execute(user_post_sql, user_post_data)

    # -----------------------------------------------USER MESSAGE TABLE-------------------------------------------------
    user_message_sql = "INSERT INTO usermessage (id, targetid, message, createdate) " \
                       "VALUES (%s , %s, %s, %s)"
    userid = get_id(username_gen)

    if i == 0:
        target_id = 1
    else:
        target_id = get_friend_id(userid, rows)

    message = gen.sentence()
    createdate = date()
    user_message_data = (userid, target_id, str(message), createdate)
    mycursor.execute(user_message_sql, user_message_data)

    mydb.commit()

# -----------------------------------------------GROUP TABLE------------------------------------------------------------
for j in range(iterations):
    group_sql = "INSERT INTO group_table (createdBy, updatedBy, title, summary, createDate, updateDate, size, status)" \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    rows = get_rows("user")
    creator = random.randrange(1, rows)
    updatedby = random.randrange(1, rows)
    title1 = gen.word()
    title2 = gen.word()
    title = title1 + " " + title2
    summary = gen.sentence() + gen.sentence()
    group_createdate, group_updatedate = user_date()
    size = random.randrange(1, 100)
    group_data = (
        creator, updatedby, title, str(summary), group_createdate, group_updatedate, size, status("Open", "Closed"))
    mycursor.execute(group_sql, group_data)
    mydb.commit()

    # -----------------------------------------------GROUP FOLLOWER TABLE-----------------------------------------------
    group_rows = get_rows("group_table")
    group_follower_sql = "INSERT INTO groupfollower(groupid, userid, follower)" \
                         "VALUES (%s, %s, %s)"
    if group_rows == 1:
        groupid = 1
    else:
        groupid = random.randrange(1, group_rows)
    user = random.randrange(1, rows)
    following = status("Following", "Not Following")
    group_follower_data = (groupid, user, following)
    mycursor.execute(group_follower_sql, group_follower_data)
    mydb.commit()

    # -----------------------------------------------GROUP MEMBER TABLE-------------------------------------------------
    group_member_sql = "INSERT INTO groupmember(groupid, userid, role)" \
                       "VALUES (%s, %s, %s)"
    if group_rows == 1:
        groupid = 1
    else:
        groupid = random.randrange(1, group_rows)
    if following == "Not Following":
        role = 'None'
    else:
        role = status('Member', 'Administrator')
    group_member_data = (groupid, user, role)
    mycursor.execute(group_member_sql, group_member_data)
    mydb.commit()

    # -----------------------------------------------GROUP MESSAGE TABLE------------------------------------------------
    group_message_sql = "INSERT INTO groupmessage(groupid, creatorid, message, createdate)" \
                        "VALUES (%s, %s, %s, %s)"
    if group_rows == 1:
        groupid = 1
    else:
        groupid = random.randrange(1, group_rows)

    creator = random.randrange(1, rows)
    message = gen.sentence() + gen.sentence()
    createdate = date()

    group_message_data = (groupid, creator, str(message), createdate)
    mycursor.execute(group_message_sql, group_message_data)
    mydb.commit()
    # -----------------------------------------------GROUP POST TABLE---------------------------------------------------
    group_post_sql = "INSERT INTO grouppost(groupid, userid, post, message, createdate)" \
                     "VALUES (%s, %s, %s, %s, %s)"
    if group_rows == 1:
        groupid = 1
    else:
        groupid = random.randrange(1, group_rows)

    creator = random.randrange(1, rows)
    post = generate_image()
    message = gen.sentence() + gen.sentence()
    createdate = date()

    group_post_data = (groupid, creator, post, str(message), createdate)
    mycursor.execute(group_post_sql, group_post_data)
    mydb.commit()


