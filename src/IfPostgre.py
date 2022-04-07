import psycopg2
import Constants

class IfPostgre:

    def __init__(self) -> None:
        """
        Constructor
        """
        try:
            #establishing the connection
            self.conn = psycopg2.connect(
               database=Constants.DATABASE_NAME, user='postgres', password='postgres', host='127.0.0.1', port= '5432'
            )

            #Creating a cursor object using the cursor() method
            self.cursor = self.conn.cursor()

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: " + str(error))

    def create_table(self):
        """
        Creates a new table in the database severus
        """
        pass
    
    def del_table(self):
        """
        Deletes a table in the database severus
        """
        pass
    
    def create_database():
        """
        Creates Database for the project
        """
        try:
            #establishing the connection
            conn = psycopg2.connect(
               database="postgres", user='postgres', password='postgres', host='127.0.0.1', port= '5432'
            )
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: Cannot create connection to default postgres database")
            print("Please create default postgres database and try again...!!!")
            return -1
        
        try:
            #Creating a cursor object using the cursor() method
            cursor = conn.cursor()

            #As CREATE DATABASE cannot run under transaction we need to enable auto Commit
            conn.autocommit = True

            #Preparing query to create a database
            sql = "CREATE DATABASE " + Constants.DATABASE_NAME + ";"
            print(sql)

            #Creating a database
            cursor.execute(sql)
            print("Database created successfully........")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Database already Exists..!!!" + str(error))
        finally:
            #Closing the connection
            conn.close()
        