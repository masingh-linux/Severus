import random
import string
import hashlib


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
    def get_sha512_hash(image_path):
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
