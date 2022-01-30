from PIL import Image, ImageDraw, ImageFont
import os, re, sys
sys.path.append('../GlobalUtil')
# 忽略这里的报错, 因为引入了公用的util文件
import util as ImageUtil
# 变量输入
root = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
BG = Image.open('../res/ShangHaoEmpty.png')
fontSize = 30

try:
    ico = Image.open(root + '/icon.png')
except FileNotFoundError:
    exit("please put icon under the program directory and name it \"icon.png\".")
title = input('What do you want for title: ')

# 将传入的icon变更为280*280
ico = ico.resize((280, 280))
# icon去除透明背景
for i in range(280):
    for j in range(280):
        if not ico.getpixel((i, j))[3]:
            ico.putpixel((i, j), value = (255, 255, 255))

# title生成图片
t = ImageUtil.makeTextImage(title, 280, (0, 0, 0, 255), fontSize)
# 拼合图片(准备利用util的工具重写)
BG.paste(ico, (500, 50))
BG.paste(t, ((500 + int(abs((280 - t.size[0])) / 2)), 330))

title = re.sub(r'[\\/.\*$ "\'\[\]\{\}]', '', title)
BG.save(root + '/out/shanghao_' + title + '.png')
Image.open(root + '/out/shanghao_' + title + '.png').show()