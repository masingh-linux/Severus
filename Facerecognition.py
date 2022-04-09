from distutils.log import error
from logging import exception
import face_recognition
import os
import Constants

list_encoding = []
list_all_encodings = []
class Facerecognition:
    def __init__(self) -> None:
        try:
            for images in os.listdir(Constants.IMAGE_PATH):
                Image_loading = face_recognition.load_image_file(Constants.IMAGE_PATH + "/" + images)
                list_encoding.append(face_recognition.face_encodings(Image_loading))
            self.list_all_encodings = list_encoding
            print(self.list_all_encodings)
        except exception as error:
            print(error)         
