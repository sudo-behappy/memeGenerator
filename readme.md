# 随便写的一些生成器
随便拿去用, 记得标明原作者, 遵循MIT协议

随缘更新, 本身也就是个整活的repo

## 现有生成器
### [上号生成器](.\ShanghaoGenerator)
[manual](.\ShanghaoGenerator\manual.md)
#### todo:
- ~~寻找中文等宽字体~~
- ~~优化长文本显示~~
- ~~去除透明底板~~
- 对于icon主要部分只占一点点的图片的resize
- 用新的util重写方法
    - 图片添加文字
    - ~~去除透明背景~~
    - 拼合图片
    - ~~文字直接生成图片~~
### [再说一遍生成器](ActAgain\main.py)
#### todo:
- 新坑...

## 图片工具箱 [ImageUtil.py](GlobalUtil\ImageUtil.py)
封装了一些会经常用到的方法
### todo:
- 完善这个文档
- 在图片中添加文字, 返回添加完的图片
- ~~去掉图片的透明背景(针对RGBA格式)~~
- 多张图片生成gif, 支持自定义帧率
- 清除背景函数多进程优化
### 方法:
```py
mergeImages(images: list, bgColor = (255, 255, 255, 0), alignment = 'uc')
```
- list: 给定的图片列表
- bgColor: RGBA格式的背景颜色元组, 默认透明
- alignment: 图片如何排布, 默认居中
可用的alignment字符串:
```py
'l': left,
'c': center,
'r': right
```

## 布局工具箱 [AlignmentUtil.py](GlobalUtil\ColorUtil.py)
为了让ImageUtil不那么臃肿而写的

### 方法: 
```py
ALIGNMENT_FUNC[alignment_method](maxWidth, maxHeight, size)
```
将各种alignment方法封装好的一个字典
- maxWidth: 布局方框x方向的长度
- maxHeight: 布局方框y方向的长度
- size: 图片的(x, y)大小元组
可用的alignment_method字符串:
```py
"ul": upper_left
"uc": upper_center
"ur": upper_right
"cl": center_left
"cc": center_center
"cr": center_right
"ll": lower_left
"lc": lower_center
"lr": lower_right
```


## 颜色工具箱 [ColorUtil.py](GlobalUtil\ColorUtil.py)
颜色处理相关的都放在这里
### 方法
- 施工中