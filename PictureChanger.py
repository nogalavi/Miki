import os
import shutil


class PictureChanger:

    def __init__(self):
        self.project_path = "/Users/nogalavi/Documents/MikiProject"
        self.picture_file_name = "Tair.jpeg"

    def change_picture(self, new_picture_path):
        if not os.path.isfile(new_picture_path):
            print "no such file: %s" %new_picture_path
            raise IOError
            return
        shutil.copy(new_picture_path, new_picture_path+"1")
        os.rename(new_picture_path+"1", os.path.join(self.project_path,self.picture_file_name))
