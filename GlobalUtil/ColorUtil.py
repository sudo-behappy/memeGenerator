# 给定颜色元组(RGBA), 返回反相的元组(fin)
def reverseColor(color: tuple):
    t = list(color)
    for i in range(3):
        t[i] = 255 - t[i]
    return tuple(t)

# 比对颜色是否一致, 支持threshold
def compateColor(color1: tuple, color2: tuple, type: str = 'RGBA', threshold: list = [0, 0, 0, 0]):
    for k in range():
        if not color1[k] in range(int(color2[k] - threshold[k] - 1), int(color2[k] + threshold[k] + 1)):
            return False
    return True