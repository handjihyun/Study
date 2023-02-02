# ------------------------------------------------
# 이미지 처리
# - 픽셀
# - 이미지 변환
# - 필로우 라이브러리 (Pillow library)
# ------------------------------------------------
import PIL
from PIL import Image

# ------------------------------------------------
# 이미지 표시 간단 예제
# ------------------------------------------------
img = Image.open('img/lenna.png')
print(img.size)
print(img.format)

img.show()

# ------------------------------------------------
# 이미지 잘라내기 : crop() 메서드
# ------------------------------------------------
area = (100, 100, 320, 320)
cropImage = img.crop(area)

cropImage.show()

# ------------------------------------------------
# Thumbnail 이미지 생성
# - 큰 이미지의 파일의 thumbnail 이미지 생성
# - thumbnail() 호출
# ------------------------------------------------
size = (64, 64)
img.thumbnail(size)
img.save('lenna-thumb.png')
img.show()

# ------------------------------------------------
# 이미지 회전 및 resize
# ------------------------------------------------
img2 = img.resize((300, 300))       # tuple 형태의 크기(가로, 세로)
img2.save('lenna_300.png')

img3 = img.rotate(90)               # counter-clockwise (반시계방향)
img3.save('lenna_rotate.png')
img3.show()

# ------------------------------------------------
# 이미지 회전 및 flip
# ------------------------------------------------
# y축을 기준으로 x값 이동
mirrorImage = img.transpose(Image.FLIP_LEFT_RIGHT)
mirrorImage.show()

# x축을 기준으로 y값 이동
undownImage = img.transpose(Image.FLIP_TOP_BOTTOM)
undownImage.show()

# ------------------------------------------------
# 이미지 필터링
# ------------------------------------------------
from PIL import ImageFilter

# Contour
contourImage = img.filter(ImageFilter.CONTOUR)
contourImage.show()

# Blur
blurImage = img.filter(ImageFilter.BLUR)
blurImage.show()

# Emboss
embossImage = img.filter(ImageFilter.EMBOSS)
embossImage.show()

# ------------------------------------------------
# 이미지에서 R, G, B 분리
# - (red, green, blue) = split() 메서드 사용
# ------------------------------------------------
new_york = Image.open('img/newyork.jpg')
print(new_york.mode)

r, g, b = new_york.split()
r.show()
g.show()
b.show()

# ------------------------------------------------
# 그레이 스케일 이미지로 변환하기
# ------------------------------------------------
def convert_grayscale(image):
    width, height = image.size
    new_image = Image.new("RGB", (width, height), "white")

    for i in range(width):
        for j in range(height):
            pixel = image.getpixel((i, j))

            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]

            gray = (red*0.299) + (green*0.587) + (blue*0.114)

            new_image.putpixel((i, j), (int(gray), int(gray), int(gray)))
    return new_image

original = Image.open('img/lenna.png')
output = convert_grayscale(original)
output.show()