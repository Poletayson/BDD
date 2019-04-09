from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import random
from PIL import  Image #Подключим необходимые библиотеки.

class Example:
    filename = ""
    img = Image.new("RGB", (0, 0))

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
        str = filename.split('.')[-1].lower()
        if (str == "jpg" or str == "png" or str == "jpeg"):
            self.img.save(filename)
            return str
        else:
            return "..."

    def resiseW (self):
        str = self.filename.split('.')[-1].lower()
        if (str == "jpg" or str == "png" or str == "jpeg"):
            W, H = self.img.size
            self.img = self.img.resize((W, W))
            return self.img.size
        else:
            return (0,0)


    def resiseH (self):
        #print(self.filename)

        str = self.filename.split('.')[-1].lower()
        if (str == "jpg" or str == "png" or str == "jpeg"):
            W, H = self.img.size
            self.img = self.img.resize((H, H))
            return self.img.size
        else:
            return (0,0)



def main():
    Tk().withdraw()  # Openfile Window
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file

    ex = Example (filename)
    print(ex.openFile())

    mode = '0'
    if (mode == 'W'):
        print(ex.resiseW())
    elif (mode == 'H'):
        print(ex.resiseH())

    str = filename.split('.')[-1].lower()
    filename = asksaveasfilename(defaultextension='.' + str)
    print(ex.saveFile(filename))


if __name__ == '__main__':
    main()

