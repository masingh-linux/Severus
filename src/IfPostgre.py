"""
IfPostgres
"""
import psycopg2
import Constants
import SeverusUtils as su
import json
import numpy

class IfPostgre:
    """
    Class for Database Interface
    All the interactions with the DB should always be done from this class
    """
    def __init__(self) -> None:
        """
        Constructor
        """
        try:
            # establishing the connection
            self.conn = psycopg2.connect(
                database=Constants.DATABASE_NAME,
                user='postgres',
                password='postgres',
                host='127.0.0.1',
                port='5432'
            )

            # Creating a cursor object using the cursor() method
            self.cursor = self.conn.cursor()

        except psycopg2.DatabaseError as error:
            print("Error: " + str(error))
        except Exception as e:
            print(e)


    def create_table(self, delete_table=True):
        """
        Create table in database severus
        
        Args:
            delete_table (bool, optional): 
                True if table is to be deleted before creating. Defaults to True.
                False if table is not to be  deleted and if already exists leave as it is
        """        
        try:    
            commands = """
                CREATE TABLE 
                    face_encoding (
                        person_id VARCHAR(255), 
                        encoding VARCHAR(4096),
                        encoding_hash VARCHAR(129) PRIMARY KEY
                    );
                """
            if delete_table:
                #Doping EMPLOYEE table if already exists.
                self.cursor.execute("DROP TABLE IF EXISTS face_encoding;")

            self.cursor.execute(commands)
            # commit the transaction
            self.conn.commit()
        except Exception as error:
            self.conn.rollback()
            print("Error: " + str(error))

    def insert_entry_face_encoding(self, encoding, name=None):
        try:
            if name is None:
                name = su.SeverusUtils.get_random_name()
            
            enc = su.SeverusUtils.get_encoding_present_in_db(self, encoding)
            if enc is None:
                # command to add values in db table
                encoding_str = IfPostgre.__get_encoding_str(encoding)
                command = """
                INSERT into face_encoding (person_id, encoding, encoding_hash)
                VALUES ('%s','%s', '%s');""" % (name,
                                                encoding_str,
                                                su.SeverusUtils.get_sha512_hash_of_str(encoding_str))
                self.cursor.execute(command)
                # commit the transaction
                self.conn.commit()
            else:
                print("Encoding already present in DB")
        except psycopg2.DatabaseError as error:
            self.conn.rollback()
            print("Error: " + str(error))
        except Exception as e:
            print(e)

    def update_person_name(self, name, encoding):
        #TODO
        try:
            command = """
            UPDATE face_encoding SET person_id='%s' 
            WHERE encoding_hash='%s';
            """ % (name,
                   su.SeverusUtils.get_sha512_hash_of_str(IfPostgre.__get_encoding_str(encoding)))
            self.cursor.execute(command)

            #commit the trasaction
            self.conn.commit()
        except psycopg2.DatabaseError as error:
            self.conn.rollback()
            print("Error:" + str(error))
        except Exception as e:
            print(e)
            
    def get_all_encodings(self):
        try:
            all_enc_lst = []
            command = """
            SELECT encoding FROM face_encoding;"""
            self.cursor.execute(command)
            data = self.cursor.fetchall()
            for row in data:
                all_enc_lst.append(numpy.array(json.loads(row[0])))
        except psycopg2.DatabaseError as error:
            self.conn.rollback()
            print("Error: " + str(error))
        except Exception as e:
            print(e)
        return all_enc_lst


    def get_face_encoding(self, name):
        """Get Face Encodings for the Name 

        Args:
            name (_type_): Person Name to be fetched data for

        Returns:
            List: List of face_encodings
        """        
        ret = []
        try:
            command = """
            SELECT encoding 
            FROM face_encoding 
            WHERE person_id='%s';""" % (name)
            self.cursor.execute(command)
            data = self.cursor.fetchall()
            for row in data:
                ret.append(numpy.array(json.loads(row[0])))
        except psycopg2.DatabaseError as error:
            self.conn.rollback()
            print("Error: " + str(error))
        except Exception as e:
            print(e)
        return ret
  
    @staticmethod
    def create_database():
        """
        Creates Database for the project
        """
        try:
            # establishing the connection to deafult database so that we have an entrypoint to DB
            conn = psycopg2.connect(
                database="postgres",
                user='postgres',
                password='postgres',
                host='127.0.0.1',
                port='5432'
            )
        except psycopg2.DatabaseError:
            print("Error: Cannot create connection to default postgres database")
            print("Please create default postgres database and try again...!!!")
            return -1

        try:
            # Creating a cursor object using the cursor() method
            cursor = conn.cursor()

            # As CREATE DATABASE cannot run under transaction we need to enable auto Commit
            conn.autocommit = True

            # Preparing query to create a database
            sql = "CREATE DATABASE " + Constants.DATABASE_NAME + ";"
            # print(sql)

            # Creating a database
            cursor.execute(sql)
            print("Database created successfully........")
        except psycopg2.DatabaseError as error:
            print("Database already Exists..!!!" + str(error))
        except Exception as e:
            print(e)
        finally:
            # Closing the connection
            conn.close()

    @staticmethod
    def __get_encoding_str(encoding):
        return  json.dumps(encoding.tolist())
