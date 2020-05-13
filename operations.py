from PIL import Image  # module that makes this code possible
from PIL import ImageOps

image = "images\XC16.tiff";


def autoContrast():
    image1 = Image.open(image)
    image2 = ImageOps.autocontrast(image1, 10, 0)
    image1.show()
    image2.show()


def colorize():
    image1 = Image.open(image)
    image2 = ImageOps.colorize(image1, "yellow", "blue")
    image1.show()
    image2.show()


def crop():
    image1 = Image.open(image)
    image2 = ImageOps.crop(image1, image1.size[1] // 4)  # dividing height of image by 4
    image1.show()
    image2.show()


def equalize():
    image1 = Image.open(image)
    image2 = ImageOps.equalize(image1)
    image1.show()
    image2.show()


def solar():
    image1 = Image.open(image)
    image2 = ImageOps.crop(image1, image1.size[1] // 4)  # dividing height of image by 4
    image1.show()
    image2.show()
    image3 = ImageOps.solarize(image2, 4)  # dividing height of image by 4
    image3.show()


def fit():
    image1 = Image.open(image)
    image2 = ImageOps.fit(image1, (200, 200))
    image1.show()
    image2.show()


def main():
    fit()
    #solar()
    # equalize()
    # crop()
    # colorize()
    # autoContrast()


if __name__ == '__main__':
    main()
