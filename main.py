import Constants
import IfPostgre as psql
import IfFaceRecognition as frc
import os 

psql.IfPostgre.create_database()
postgres = psql.IfPostgre()
postgres.create_table()

for (root,dirs,files) in os.walk(Constants.IMAGE_DIR_PATH):
    for file in files:
        img_path = os.path.abspath(os.path.join(root, file))
        enc = frc.IfFaceRecognition.get_face_encodings(img_path)


# print(face_rc)

# psql.IfPostgre.create_database()

# postgres = psql.IfPostgre() #init call
# vold = psql.IfPostgre()

# postgres.del_table()
# postgres.create_table()

# print(postgres)






