# 这是个常用工具的集合
from PIL import Image, ImageDraw, ImageFont
from AlignmentUtil import ALIGNMENT_FUNC
import ColorUtil
import re



# 给定一个图片的list, 返回拼合好的图片, 默认透明背景, 可指定颜色元组和排布方式(默认顶部居中)(fin)
def mergeImages(images: list, bgColor = (255, 255, 255, 0), alignment = 'l'):
    alignmentModified = {
        "l": "ul",
        "c": "uc",
        "r": "ur"
    }
    x, y = 0, 0
    # 寻找最大值
    for i in images:
        x = max(x, i.size[0])
        y += i.size[1]
    t = Image.new(mode = 'RGBA', size = (x, y), color = bgColor)
    y = 0
    for i in images:
        pos = ALIGNMENT_FUNC[alignmentModified[alignment]](t.size[0], t.size[1], i.size)
        t.paste(i, (pos[0], pos[1] + y))
        y += i.size[1]
    return t

# textSize = [0]
# 给定文字, 返回生成的文字的图片, 可指定单背景色元组(默认黑底白字), 可指定大小和字体(默认12, 苹方)
def makeTextImage(text: str, maxWidth = 0, maxHeight = 0, bgColor: tuple = (0, 0, 0, 255), size = 12, auto = 0, font = None):
    if font is None:
        font = ImageFont.truetype('../res/font.ttf', size, encoding = 'utf-8')
    # 常规
    if not auto:
        if font.getsize(text[0: len(text) - 1])[0] <= maxWidth or maxWidth == 0 or maxHeight == 0:
            ans = Image.new(mode='RGBA',
                            size=font.getsize(text),
                            color=ColorUtil.reverseColor(bgColor))
            t = ImageDraw.Draw(ans)
            t.text(xy=(0, 0), text=text, fill=bgColor, font=font)
            
        # 文字长度大于maxWidth
        else:
            for i in range(len(text) - 3):
                # 给出的maxWidth连三个字都放不下
                if font.getsize(text[i: i + 3])[0] > maxWidth:
                    raise Exception("The max width is too small")
            # 存切分的文字
            textSliced = ['']
            for i in text:
                # 一个一个字符加
                textSliced[len(textSliced) - 1] += i
                # textSize[len(textSize) - 1] = font.getsize(textSliced[len(textSliced) - 1])[0]
                # 如果大了, 添加一个元素
                if font.getsize(textSliced[len(textSliced) - 1].strip())[0] > maxWidth:
                    # print("new line with space")
                    # textSize.append(0)
                    # 反向寻找空格
                    pos = textSliced[len(textSliced) - 1].rfind(' ')
                    # 找到了就切开, 把空格后的字符放到下一个元素中
                    if pos != -1:
                        textSliced.append(textSliced[len(textSliced) - 1][pos: len(textSliced[len(textSliced) - 1])].strip())
                        textSliced[len(textSliced) - 2] = textSliced[len(textSliced) - 2].removesuffix(textSliced[len(textSliced) - 1]).strip()
                    # 没有空格的部分就直接切
                    else: 
                        # print("new line without space")
                        textSliced.append('')
                # input(str(textSliced) + " " + str(textSize) + ' ')
            # 生成的图片数组
            t = []
            for i in textSliced:
                t.append(makeTextImage(i, maxWidth, bgColor, size))
            # 生成拼好的图片
            ans = mergeImages(t, bgColor, 'c')
    else:
        # 利用二分逼近期望的size(后来发现是初始size太大了, 2<<10应该差不多)()
        size = 2<<10
        lst = 0
        while True:
            font = ImageFont.truetype(font.path, size)
            width = font.getsize(text)[0]
            height = font.getsize(text)[1]
            if (width > maxWidth and auto == 1) or (height > maxHeight and auto == 2):
                size -= int(abs(lst - size)>>1)
            elif(width < maxWidth and auto == 1) or (height < maxHeight and auto == 2):
                t = size
                size += int(abs(lst - size)>>1)
                lst = t
            if (maxWidth - 20 <= width <= maxWidth and auto == 1) or (maxHeight - 20 <= height <= maxHeight and auto == 2):
                break
        ans = makeTextImage(text, maxWidth, maxHeight, bgColor, size, 0, font)
    return ans

# 利用正则去除文件中的非法字符
def normalizeString(str):
    return re.sub(r'[^a-zA-Z0-9]+', '', str)

# 图片颜色替换, 返回操作完的图片(支持RGBA, A要么0要么255)
def removeBackgroundColor(t: Image, bgColor: tuple, replacementColor: tuple, bgThreshold = [0, 0, 0, 0]):
    image = t.convert('RGBA')
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            # 判断是否在threshold内
            if ColorUtil.compareColor(image.getpixel((i, j)), bgColor, threshold = bgThreshold):
                image.putpixel((i, j), replacementColor)
    return image

# 将图片中的透明部分替换成你想要的颜色, 默认白色
def removeTransparent(t: Image, replacementColor: tuple = (255, 255, 255, 255)):
    return removeBackgroundColor(t, (0, 0, 0, 0), replacementColor, [255, 255, 255, 0])

# TODO: 仅去除背景




#-----------------------------------------------------------------训练靶场-----------------------------------------------------------------
# removeBackgroundColor(Image.open(testImagePath), (255, 255, 255, 255), (255, 255, 255, 0)).save('./test.png')
#makeTextImage('1145141919810', 800, auto = True).save('./test.png')

