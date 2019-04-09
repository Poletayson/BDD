from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import random
from PIL import  Image #Подключим необходимые библиотеки.

class Example:
    filename = ""

    def __init__(self, f):
        self.filename = f

    def openFile(self):
        str = self.filename.split ('.')[-1].lower()
        if (str == "jpg" or str == "png" or str == "jpeg"):
            self.img = Image.open(self.filename)
            return str
        else:
            return '...'

    def saveFile(self, filename):
            return 'jpg'



