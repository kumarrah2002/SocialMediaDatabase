![image text](https://media.istockphoto.com/id/1288255759/photo/database-or-network-server-concept.jpg?b=1&s=170667a&w=0&k=20&c=hUK2K6raAvqMvhE_9EgHHUYw9qF5-VC5WHG-CceH5Bk=)
# CS 365 Final Project

Final for CS 365 - Principles of Database Systems

## Description

For this project, we were tasked with creating a database design for a social media platform. 
Due to the large amounts of data collected on these platforms, we created multiple tables to
hold information concerning different user actions on these platforms. 

## Getting Started

### Dependencies

* Applications
  * MySQL Workbench
  * Python
  * Any Python IDE (PyCharm, IntelliJ, etc.)
* Packages
  * pip (v. 22.3.1)
  * names (v. 0.3.0)
  * mysql-connector-python (v. 8.0.31)
  * essential-generators (v. 1.0)
* Data
  * Any collection of images work. I recommend downloading a small sample of the 
  <b>Dogs vs. Cats</b> Dataset given below:
  * https://www.kaggle.com/c/dogs-vs-cats/data?select=test1.zip
  * <i>We used 3,000 images but there is no minimum/maximum amount of photos needed, any amount should suffice. </i>

### Preliminary Steps

* Download <i>createDatabase.py</i>, <i>main.py</i>, and <i>deleteDatabase.py</i>
* Download packages specified through "Python Packages" in your IDE or through the terminal
```
pip install (package_name)
```
* Change login information for accessing database in <i>createDatabase.py</i> and <i>main.py</i>
  * For this, you must have an accessible MySQL Connection in MySQL Workbench
* Change image directory in line 221 of <i>main.py</i> to location of image folder
### Executing program
* Run <i>createDatabase.py</i> first
* Run <i>main.py</i> after
* If you want to delete the database:
  * run <i>deleteDatabase.py</i>
## Results

Once you run the code successfully, refresh your Workbench and you will see data for 
every table. The tables created are as follows:
* User Tables
  * user
    * id (primary key), first name, last name, username, phone number, email, 
    password, birthday, age, register date, last login, profile bio, profile picture
  * userFriend 
    * friendship id (primary key), user id (foreign key to user(id)), friend id(foreign key to user(id)), 
    username, friend's username, friendship type, creation date
  * userStore
    * itemid (primary key), user id(foreign key to user(id)), item name, item cost, 
    item description, shipping date, shipping cost, product reviews
  * userPost
    * post id (primary key), user id (foreign key to user(id)), post, text field, create date, update date
  * userMessage
    * message id (primary key), user id (foreign key to user(id)), target id (foreign key to user(id)), message, create date
* Group Tables
  * group_table
    * group id (primary key), created by (foreign key to user(id)), updated by(foreign key to user(id)), 
    title, summary, create date, update date, size, status
  * groupMember
    * group id (foreign key to group(groupid)), user id (foreign key to user(id)), role (Administrator or Member)
  * groupFollower
    * group id (foreign key to group(groupid)), user id (foreign key to user(id)), follower (Following or Not Following)
  * groupMessage
    * group id (foreign key to group(groupid)), creator id (foreign key to user(id)), message, create date
  * groupPost
    * group id (foreign key to group(groupid)), creator id (foreign key to user(id)), post, message, create date


## Authors

Contributor names and contact info:

Rahul Kumar
* Email: kumarrah2002@gmail.com
* [LinkedIn](https://www.linkedin.com/in/kumarrah/)
* [GitHub](https://github.com/kumarrah2002)

Nathan Snow
* Email: nathaniel82750@gmail.com

Basel Almutawa
* Email: strongsteeldb@gmail.com

Abdullah Hussain
* Email: abdufhussain@gmail.com

## Acknowledgments

This project is for Dr. Mohammed Kamruzzaman Sarker's class at the University of Hartford.
Plagiarism of any kind from these Python files are not permitted and will not be tolerated. 
