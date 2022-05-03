import os
import Constants
import IfPostgre as psql
import IfFaceRecognition as frc
import SeverusUtils as su
import time

# postgres =  psql.IfPostgre.create_database()
# postgres = psql.IfPostgre()
# postgres.create_table(False)

for (root, dirs, files) in os.walk(Constants.IMAGE_DIR_PATH):
    for file in files:
        img_path = os.path.abspath(os.path.join(root, file))
        enc = frc.IfFaceRecognition.get_face_encodings(img_path)
        fd = open("../temp/" + file + ".txt",
                  mode='a',
                  encoding='utf-8')
        fd.write(str(enc))
# print(face_rc)

# psql.IfPostgre.create_database()

# postgres = psql.IfPostgre() #init call
# vold = psql.IfPostgre()

# postgres.del_table()
# postgres.create_table()

# print(postgres)
