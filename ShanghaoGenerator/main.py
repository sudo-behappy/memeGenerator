from PIL import Image, ImageDraw, ImageFont
import os
import re
# 变量输入
root = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
BG = Image.open(root + '/res/shanghao_empty.png')
fontSize = 30

try:
    ico = Image.open(root + '/icon.png')
except FileNotFoundError:
    exit("please put icon under the program directory and name it \"icon.png\".")
title = input('What do you want for title: ')
# 过长title处理
if len(title) >= 14:
    fontSize = int(30 * 14 / len(title))

# 将传入的icon变更为280*280
ico = ico.resize((280, 280))
# icon去除透明背景
for i in range(280):
    for j in range(280):
        if not ico.getpixel((i, j))[3]:
            ico.putpixel((i, j), value = (255, 255, 255))

# title生成图片
t = Image.new(mode = 'RGBA', size = (int(len(title) * 18 * fontSize / 30), fontSize + 0), color = 'white')
titleImage = ImageDraw.Draw(t)
font = ImageFont.truetype(font = root + '/res/font.ttf', size = fontSize)
titleImage.text(xy = (0, 0), text = title, fill = (0, 0, 0), font = font)
# 拼合图片
BG.paste(ico, (500, 50))
BG.paste(t, ((500 + int(abs((280 - t.size[0])) / 2)), 330))

title = re.sub(r'[\\/.\*$ "\'\[\]\{\}]', '', title)
BG.save(root + '/out/shanghao_' + title + '.png')
Image.open(root + '/out/shanghao_' + title + '.png').show()