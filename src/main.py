from calendar import c
import Constants
import IfPostgre as psql

psql.IfPostgre.create_database()

postgres = psql.IfPostgre() #init call
vold = psql.IfPostgre()

postgres.del_table()
postgres.create_table()

print(postgres)







