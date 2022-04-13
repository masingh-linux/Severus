import face_recognition

class IfFaceRecognition:        

    def get_face_encodings(image_path):
        '''
        This method returns all face encodings from an image
        @param image_path : Absolute path of an image 
        '''
        try:
            image_loading = face_recognition.load_image_file(image_path)
            return tuple(face_recognition.face_encodings(image_loading))
        except Exception as error:
            print(error)
            return None

