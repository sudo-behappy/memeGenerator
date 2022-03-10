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
    t = Image.new(mode = 'RGBA', size = (x, y), color = ColorUtil.reverseColor(bgColor))
    y = 0
    for i in images:
        pos = ALIGNMENT_FUNC[alignmentModified[alignment]](t.size[0], t.size[1], i.size)
        t.paste(i, (pos[0], pos[1] + y))
        y += i.size[1]
    return t

# textSize = [0]
# 给定文字, 返回生成的文字的图片, 可指定单背景色元组(默认黑底白字), 可指定大小(默认12)
def makeTextImage(text, maxWidth, bgColor: tuple = (0, 0, 0, 255), size=12):
    font = ImageFont.truetype('../res/font.ttf', size, 0)
    # 常规
    if font.getsize(text[0: len(text) - 1])[0] <= maxWidth:
        ans = Image.new(mode='RGBA',
                        size=font.getsize(text),
                        color=ColorUtil.reverseColor(bgColor))
        t = ImageDraw.Draw(ans)
        t.text(xy=(0, 0), text=text, fill=bgColor, font=font)
        
    # 文字长度大于maxWidth
    else:
        for i in range(len(text) - 3):
            if font.getsize(text[i: i + 3])[0] > maxWidth:
                raise Exception("The max width is too small")
            textSliced = ['']
        for i in text:
            textSliced[len(textSliced) - 1] += i
            # textSize[len(textSize) - 1] = font.getsize(textSliced[len(textSliced) - 1])[0]
            if font.getsize(textSliced[len(textSliced) - 1].strip())[0] > maxWidth:
                # print("new line with space")
                # textSize.append(0)
                pos = textSliced[len(textSliced) - 1].rfind(' ')
                if pos != -1:
                    textSliced.append(textSliced[len(textSliced) - 1][pos: len(textSliced[len(textSliced) - 1])].strip())
                    textSliced[len(textSliced) - 2] = textSliced[len(textSliced) - 2].removesuffix(textSliced[len(textSliced) - 1]).strip()
                else:
                    # print("new line without space")
                    textSliced.append('')
            # input(str(textSliced) + " " + str(textSize) + ' ')
        t = []
        for i in textSliced:
            t.append(makeTextImage(i, maxWidth, bgColor, size))
        ans = mergeImages(t, bgColor, 'c')
    ans.show()
    return ans

# 去除文件中的非法字符
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

# TODO: 在图片中添加文字, 返回添加完的图片
def addText(text, position: tuple, size: int, alignment: int):
    pass


#-----------------------------------------------------------------训练靶场-----------------------------------------------------------------
# testImagePath = "E:\\temp\O%RWTHOTULE1LH{@[MC_Q}B.png"
# removeBackgroundColor(Image.open(testImagePath), (255, 255, 255, 255), (255, 255, 255, 0)).save('./test.png')
