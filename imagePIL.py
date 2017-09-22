'PIL'
'PIL:Python Imaging Library,已经是Python平台上的图像标准库了,但是只支持到2.7,加上年久失修'
'于是一群志愿者在PIL的基础上创建了兼容版本,名字叫 pillow 支持最新Python 3.X,又加入了许多新特性'

# from PIL import Image
#
# # 打开一个jpg图像文件
# im = Image.open('/Users/aishangsaisai/Desktop/照片/0b55b319ebc4b7456c8d4c8ecffc1e178a821508.jpg')
# # 获取图像尺寸
# w,h = im.size
# print('图像的尺寸为: %sx%s' % (w,h))
# # 缩放到50%
# im.thumbnail((w//2,h//2)) # // --> 地板除 地板除只取结果的整数部分
# print('图像的尺寸为: %sx%s' % (w//2,h//2))
# # 把缩放的图像保存下来
# # im.save('thumbnail.jpg','jpeg')

'其他功能如切片,旋转,滤镜,输出文字,调色板等一应俱全'
# from PIL import Image,ImageFilter
#
# im = Image.open('/Users/aishangsaisai/Desktop/learningPython/thumbnail.jpg')
# # 应用模糊
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('blur.png')

'PIL 的 ImageDraw 提供了一系列绘图方法,让我们可以直接绘图.比如要生成字母验证码图片'
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

# 随机字母
def randChar():
    return chr(random.randint(65,90))
# 随机颜色
def randColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
# 随机颜色2
def randColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

print('字母:%s \n颜色%s \n颜色2%s' % (randChar(),randColor(),randColor2()))

# 240 x 60
width = 60 * 4
height = 60
image = Image.new('RGB',(width,height),(255,255,255))
# 创建Font对象
font = ImageFont.truetype('Arial.ttf',36)
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill = randColor())
# 输出文字
for t in range(4):
    draw.text((60 * t + 10,10),randChar(),font = font,fill = randColor2())
# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')
