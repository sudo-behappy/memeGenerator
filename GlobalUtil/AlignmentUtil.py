def x_left(maxWidth, size):
    return 0
def x_center(maxWidth, size):
    return int(abs(maxWidth - size) / 2)
def x_right(maxWidth, size):
    return maxWidth - size
def y_top(maxHeight, size):
    return 0
def y_center(maxHeight, size):
    return int(abs(maxHeight - size) / 2)
def y_bottom(maxHeight, size):
    return maxHeight - size
def upper_left(maxWidth, maxHeight, size, box):
    return (box[0] + x_left(maxWidth, size[0]), box[1] + y_top(maxHeight, size[1]))
def center_left(maxWidth, maxHeight, size, box):
    return (box[0] + x_left(maxWidth, size[0]), box[1] + y_center(maxHeight, size[1]))
def lower_left(maxWidth, maxHeight, size, box):
    return (box[0] + x_left(maxWidth, size[0]), box[1] + y_bottom(maxHeight, size[1]))
def upper_center(maxWidth, maxHeight, size, box):
    return (box[0] + x_center(maxWidth, size[0]), box[1] + y_top(maxHeight, size[1]))
def center_center(maxWidth, maxHeight, size, box):
    return (box[0] + x_center(maxWidth, size[0]), box[1] + y_center(maxHeight, size[1]))
def lower_center(maxWidth, maxHeight, size, box):
    return (box[0] + x_center(maxWidth, size[0]), box[1] + y_bottom(maxHeight, size[1]))
def upper_right(maxWidth, maxHeight, size, box):
    return (box[0] + x_right(maxWidth, size[0]), box[1] + y_top(maxHeight, size[1]))
def center_right(maxWidth, maxHeight, size, box):
    return (box[0] + x_right(maxWidth, size[0]), box[1] + y_center(maxHeight, size[1]))
def lower_right(maxWidth, maxHeight, size, box):
    return (box[0] + x_right(maxWidth, size[0]), box[1] + y_bottom(maxHeight, size[1]))

ALIGNMENT_FUNC = {
    "ul": upper_left,
    "uc": upper_center,
    "ur": upper_right,
    "cl": center_left,
    "cc": center_center,
    "cr": center_right,
    "ll": lower_left,
    "lc": lower_center,
    "lr": lower_right
}

