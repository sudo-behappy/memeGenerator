from PIL import ImageSequence, Image
import ImageUtil
import ColorUtil
from AlignmentUtil import ALIGNMENT_FUNC

# gif拆帧, 返回所有帧图像数组
def extractFrame(image):
    ans = []
    for i in ImageSequence.Iterator(image):
        ans.append(i.copy())
        
    return ans


# ----------------------------------------------------------------训练靶场--------------------------------------------------------
import os
images = extractFrame(Image.open('../test/test.gif'))
for i in range(len(images)):
    
    images[i].save('.。/test/gif/' + str(i) + '.png')
    