from PIL import Image, ImageDraw, ImageFont
# 变量输入
BG = Image.open('shanghao_empty.png')
fontSize = 30
try:
    ico = Image.open('icon.png')
except FileNotFoundError:
    exit("please put icon under the program directory and name it \"icon.png\".")
title = input('What do you want for title: ')
# 过长title处理
if len(title) >= 14:
    fontSize = int(30 * 14 / len(title))

# 将传入的icon变更为280*280
ico = ico.resize((280, 280))
# title生成图片
t = Image.new(mode = 'RGBA', size = (int(len(title) * 18 * fontSize / 30), fontSize + 0), color = 'white')
titleImage = ImageDraw.Draw(t)
font = ImageFont.truetype(font = 'font.ttf', size = fontSize)
titleImage.text(xy = (0, 0), text = title, fill = (0, 0, 0), font = font)
t.show()
# 拼合图片
BG.paste(ico, (500, 50))
BG.paste(t, ((500 + int(abs((280 - t.size[0])) / 2)), 330))
BG.save('./out/shanghao_' + title + '.png')
Image.open('./out/shanghao_' + title + '.png').show()