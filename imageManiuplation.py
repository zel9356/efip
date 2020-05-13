from PIL import Image  # module that makes this code possible
from PIL import ImageEnhance

import os  # Miscellaneous operating system interfaces

"""
os.listdir(path='.')
Return a list containing the names of the entries in the directory given by path.
The list is in arbitrary order, and does not include the special entries '.' and '..' 
even if they are present in the directory.
"""


def saveing():
    for f in os.listdir("images"):  # for each image in the folder images f is equal to the file name
        text = f  # String of the name of file we are on in the loop
        print(f)  # prints the name
        image1 = Image.open("images\\" + f)  # open gives var image1 the value of the image f
        image1.show()  # displays image1/f
        image1.save(r"C:\Users\zobok\OneDrive\Desktop\E-FIP\\" + text)  # saves image 1 to location


def enhancingContrast():  # function to contrast preform enhancing
    image1 = Image.open("images\XC16.tiff")  # image 1 is our original image
    image1.show()  # show original image
    temp = ImageEnhance.Contrast(image1)  # temp is a var we can perform a contrast enhancement on
    image2 = temp.enhance(1.6)  # Preform enhancement with a factor of 1.6 and set that new enhance image
    # equal to image two
    image2.show()  # display image 2


def enhancingColor():  # function to preform color enhancing
    image1 = Image.open("images\IMG8208.jpg")  # image 1 is our original image
    image1.show()  # show original image
    temp = ImageEnhance.Color(image1)  # temp is a var we can perform a color enhancement on
    image2 = temp.enhance(1.6)  # Preform enhancement with a factor of 1.6 and set that new enhance image
    # equal to image two
    image2.show()  # display image 2


def enhancingBrightness():  # function to preform brightness enhancing
    image1 = Image.open("images\XC16.tiff")  # image 1 is our original image
    image1.show()  # show original image
    temp = ImageEnhance.Brightness(image1)  # temp is a var we can perform a brightness enhancement on
    image2 = temp.enhance(1.6)  # Preform enhancement with a factor of 1.6 and set that new enhance image
    # equal to image two
    image2.show()  # display image 2


def enhancingSharpness():  # function to preform sharpness enhancing
    image1 = Image.open("images\XC16.tiff")  # image 1 is our original image
    image1.show()  # show original image
    temp = ImageEnhance.Sharpness(image1)  # temp is a var we can perform a sharpness enhancement on
    image2 = temp.enhance(1.6)  # Preform enhancement with a factor of 1.6 and set that new enhance image
    # equal to image two
    image2.show()  # display image 2

def main():
    # call to enhancing methods so it runs
    enhancingContrast()
    enhancingBrightness()
    enhancingColor()
    enhancingSharpness()


if __name__ == '__main__':
    main()
