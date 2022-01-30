# 这是个常用工具的集合
from PIL import Image, ImageDraw, ImageFont
from alignment_util import ALIGNMENT_FUNC


# 给定颜色元组(RGBA), 返回反相的元组(fin)
def reverseColor(color: tuple):
    t = list(color)
    for i in range(3):
        t[i] = 255 - t[i]
    return tuple(t)

# 给定一个图片的list, 返回拼合好的图片, 默认透明背景, 可指定颜色元组和排布方式(默认顶部居中)(fin)
def mergeImages(images: list, bgColor = (255, 255, 255, 0), alignment = 'uc'):
    x, y = 0, 0
    # 寻找最大值
    for i in images:
        x = max(x, i.size[0])
        print(i.size, x)
        y += i.size[1]
    t = Image.new(mode = 'RGBA', size = (x, y), color = bgColor)
    y = 0
    for i in images:
        t.paste(i, ALIGNMENT_FUNC[alignment](t.size[0], t.size[1], i.size, (x, y)))
        y += i.size[1]
    return t

# 给定文字, 返回生成的文字的图片, 可指定单背景色元组(默认黑底白字), 可指定大小(默认12) (fin)
def makeTextImage(text, maxWidth, bgColor: tuple = (0, 0, 0, 255), size=12):
    font = ImageFont.truetype('../res/font.ttf', size, 0)
    # 常规
    ans = None
    if font.getsize(text)[0] <= maxWidth:
        ans = Image.new(mode='RGBA',
                        size=font.getsize(text),
                        color=reverseColor(bgColor))
        t = ImageDraw.Draw(ans)
        t.text(xy=(0, 0), text=text, fill=bgColor, font=font)
    # 文字长度大于maxWidth
    else:
        textSliced = []
        lastSlice = 0
        # 寻找适合的切点
        for i in range(len(text)):
            if font.getsize(text[lastSlice: i])[0] >= maxWidth:
                # 切片
                textSliced.append(text[lastSlice: text.rfind(' ', lastSlice, i)].strip())
                lastSlice = text.rfind(' ', lastSlice, i)
                if font.getsize(text[lastSlice: len(text)])[0] <= maxWidth:
                    break
        textSliced.append(text[lastSlice: len(text)].strip())
        #合并图像
        t = []
        for i in textSliced:
            t.append(makeTextImage(i, maxWidth, bgColor, size))
        ans = mergeImages(t)      
    return ans



# TODO: 在图片中添加文字, 返回添加完的图片
def addText(text, position: tuple, size: int, alignment: int):
    pass




