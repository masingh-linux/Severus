import random
import string
import hashlib
import IfFaceRecognition as frc

import IfPostgre


class SeverusUtils:
    """
    Generate random integer value
    """
    @staticmethod
    def get_random_name():
        """This method generate random name

        Args:
            None (_type_): _description_

        Returns:
            _type_: return random length integer value
        """
        length = random.randint(10, 15)
        return ''.join(
            random.choices(
                string.ascii_uppercase,
                k=length
            )
        )

    @staticmethod
    def get_sha512_hash_of_image(image_path):
        """calculate sha512 hash of an image

        Args:
            image_path (str): aboslute path of an image
        """
        # get sha512 object
        hasher = hashlib.sha512()

        # Open Image file in RO Mode
        fd = open(image_path, mode="rb")

        # Read Data from file descriptor
        buffer = fd.read()

        # update hasher with data
        hasher.update(buffer)

        # get hash
        return hasher.hexdigest()

    @staticmethod
    def get_sha512_hash_of_str(data):
        """calculate sha512 hash of an str

        Args:
            data (str): str containig data
        """
        # get sha512 object
        hasher = hashlib.sha512()

        # update hasher with data
        hasher.update(data.encode("utf8"))

        # get hash
        return hasher.hexdigest()

    def get_encoding_present_in_db(postgres: IfPostgre, encoding):
        db_encodings  = postgres.get_all_encodings()
        matches = frc.face_recognition.compare_faces(db_encodings, encoding)
        try:
            index = matches.index(True)
        except ValueError as e:
            return 
        return db_encodings[index]