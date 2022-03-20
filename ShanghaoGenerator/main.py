from PIL import Image
import sys
sys.path.append('../GlobalUtil')
# 忽略这里的报错, 因为引入了公用的util文件
# 这里如果用debug的话会报错
import ImageUtil
# 变量输入
BG = Image.open('../res/ShangHaoEmpty.png')
fontSize = 30
try:
    ico = Image.open('e:\\temp\\icon_sekiro.png')
except FileNotFoundError:
    print('路径不存在, 将使用./icon.png作为icon')
    ico = Image.open('./icon.png')
title = input('图片标题: ')

# 将传入的icon变更为280*280
ico = ico.resize((280, 280), resample=Image.BICUBIC, box = (0, 0, ico.size[0], ico.size[1]))
# icon去除透明背景
ico = ImageUtil.removeTransparent(ico)

# title生成图片
try:
    t = ImageUtil.makeTextImage(title, 280, (0, 0, 0, 255), fontSize)
except Exception:
    exit("the title is too long")
iconAndWords = ImageUtil.mergeImages([ico, t], (255, 255, 255, 255), 'c')
iconAndWords.save('test.png')
BG.paste(iconAndWords, (500, 50))
title = ImageUtil.normalizeString(title)
print('./out/shanghao_' + title + '.png')
BG.save('./out/shanghao_' + title + '.png')
Image.open('./out/shanghao_' + title + '.png').show()