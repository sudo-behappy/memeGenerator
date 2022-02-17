from PIL import Image
import sys
sys.path.append('../GlobalUtil')
# 忽略这里的报错, 因为引入了公用的util文件
import ImageUtil
# 变量输入
BG = Image.open('../res/ShangHaoEmpty.png')
fontSize = 30

try:
    ico = Image.open('./icon.png')
except FileNotFoundError:
    exit("please put icon under the program directory and name it \"icon.png\".")
title = input('What do you want for title: ')

# 将传入的icon变更为280*280
ico = ico.resize((280, 280), resample=Image.BICUBIC, box = (0, 0, ico.size[0], ico.size[1]))
# icon去除透明背景
ico = ImageUtil.removeTransparent(ico)

# title生成图片
t = ImageUtil.makeTextImage(title, 280, (0, 0, 0, 255), fontSize)
# 拼合图片(准备利用util的工具重写)
BG.paste(ico, (500, 50))
BG.paste(t, ((500 + int(abs((280 - t.size[0])) / 2)), 330))

title = ImageUtil.normalizeString(title)
BG.save('./out/shanghao_' + title + '.png')
Image.open('./out/shanghao_' + title + '.png').show()