# -------------------------------------------
# Mirror Image 만들기
# -------------------------------------------
from PIL import Image

def mirror(original):
    image1 = Image.new('RGB', original.size, 'white')

    for i in range(original.width):
        for j in range(original.height):
            image1.putpixel((-i, j), original.getpixel((i, j)))
    image1.save('newyork-mirror.jpg')
    image1.show()


def rotate(original):
    image2 = Image.new('RGB', (original.height, original.width), 'white')
    for i in range(original.width):
        for j in range(original.height):
            image2.putpixel((j, -i), original.getpixel((i, j)))
    image2.save('newyork-ccw90.jpg')
    image2.show()

original = Image.open('img/newyork.jpg')
mirror(original)
rotate(original)