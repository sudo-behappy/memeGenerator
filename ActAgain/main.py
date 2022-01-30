from PIL import Image
import sys
sys.path.append('../GlobalUtil')
# 忽略这里的报错, 因为引入了公用的util文件
import ImageUtil
# 获取变量
BG = Image.open('../res/ActAgainEmpty.png')
# max: 225
# 上侧: (5, 475)
# 下侧: (5, 685)
# 为了降低重构压力, 这里等写好了添加文字的util之后再开始写