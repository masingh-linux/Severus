import face_recognition

class IfFaceRecognition:
    """_summary_

    Returns:
        _type_: _description_
    """
    @staticmethod
    def get_face_encodings(image_path):
        '''
        This method returns all face encodings from an image
        @param image_path : Absolute path of an image 
        '''
        try:
            image_loading = face_recognition.load_image_file(image_path)
            # enc = tuple(face_recognition.face_encodings(image_loading))
            # for entry in enc:

            # face_recognition.compare_faces()
            return tuple(face_recognition.face_encodings(image_loading))
        except Exception as error:
            print(error)
            return None
