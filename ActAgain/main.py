from PIL import Image
import sys
sys.path.append('../GlobalUtil')
import ImageUtil
BG = Image.open('../res/ActAgainEmpty.png')

# box: (5, 475) - (230, 490)
wordsAbove = input('Enter words you wish to put above:')
wordsBelow = input('Enter words you wish to put bottom:')
imageAbove = ImageUtil.makeTextImage(wordsAbove, maxHeight = 25, auto = 2)
imageBottom = ImageUtil.makeTextImage(wordsBelow, maxHeight = 25, auto = 2)
BG.paste(imageAbove, ImageUtil.ALIGNMENT_FUNC['cc'](225, 15, size = imageAbove.size, box =  (5, 475)))
BG.paste(imageBottom, ImageUtil.ALIGNMENT_FUNC['cc'](225, 15, size = imageBottom.size, box = (5, 675)))
BG.save('./out/ActAgain.png')
