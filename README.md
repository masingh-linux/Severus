# Severus

Commit Commands

# Create a new branch
git checkout -b <branch_name>

# Check which branch you are on
git branch

#####  Make Your Changes #####

# check Status of repo
git status

# add files to be  committed
git add [file1 file2 ...]

# check Status of repo
git status

# commit to the local repo
git commit -m "<Commit message>"

#  Push to the server
git push --set-upstream origin <branch_name>




# SQL Queries
INSERT into <table_name> (column1,  coloumn2,  coloumn 3) VALUE (value1,  value2,  value3);

INSERT into face_encoding (person_id, encoding,  encoding_hash) VALUES ('MUKESH', 'json.dump(data)', 'encoding hash')

SELECT encodings FROM face_encoding WHERE person_id='QHLSRJLGCEQJPQ';