import psycopg2

# definitions
database = "mydb"
user = "postgres"
#password = "pass_pass_221"
password = "Ajitesh27"
#host = "localhost"
host = '127.0.0.1'
port = "5432"


# connection establishment
conn = psycopg2.connect(
    database=database,
    user=user,
    password=password,
    host=host,
    port=port
)


"""
only to connect to an existing DB and adding tables into it
"""
# # #Creating a cursor object using the cursor() method
# cursor = conn.cursor()
# #
# #Doping EMPLOYEE table if already exists.
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
#
# #Creating table as per requirement
# sql ='''CREATE TABLE TWEETS(
#    COUNTRY_OF_ORIGIN CHAR(20) NOT NULL,
#    NAME CHAR(20),
#    DATE INT
# )'''
#
# cursor.execute(sql)
# print("Table created successfully........")
# conn.commit()
# #Closing the connection
# conn.close()

#
# # Fetch a single row using fetchone() method.
# data = cursor.fetchone()
# print("Connection established to: ",data)
#
# #Closing the connection
# conn.close()



"""
create a db
"""
# conn.autocommit = True
#
# # #Creating a cursor object using the cursor() method
# cursor = conn.cursor()
#
# #Preparing query to create a database
# sql = '''CREATE database mydb''';
#
# #Creating a database
# cursor.execute(sql)
# print("Database created successfully........")
#
# #Closing the connection
# conn.close()

"""
adding values into existing tables
"""

#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL queries to INSERT a record into the database.
cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
   INCOME) VALUES ('Ramya', 'Rama priya', 27, 'F', 9000)''')
cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
   INCOME) VALUES ('Vinay', 'Battacharya', 20, 'M', 6000)''')
cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
   INCOME) VALUES ('Sharukh', 'Sheik', 25, 'M', 8300)''')
cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
   INCOME) VALUES ('Sarmista', 'Sharma', 26, 'F', 10000)''')
cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
   INCOME) VALUES ('Tripthi', 'Mishra', 24, 'F', 6000)''')

# Commit your changes in the database
conn.commit()
print("Records inserted........")

# Closing the connection
conn.close()