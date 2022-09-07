#-*- coding:utf-8 -*-
# https://www.cnblogs.com/kirito-c/p/5971988.html
# opencv-python用来读取视频和图片
# numpy  bumpy是一个矩阵运算库，图像处理需要用到，opencv-python依赖于它
import os
import pickle
import numpy as np
import cv2
import time
from pathlib import Path

# 按帧读取视频
def video2imgs(video_name,size):
    img_list=[]
    # 读取视频并截取成图片
    cap = cv2.VideoCapture(video_name)
    while cap.isOpened():
        # ret表示是否读取到对象，frame为图像矩阵，类型为numpy.ndarry
        ret, frame = cap.read()
        if ret:
            # 转换为灰度图，或不做这一步，转换为彩色字符视频
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # resize图片，保证图片能完整地在命令行中显示
            img = cv2.resize(gray, size, interpolation=cv2.INTER_AREA)
            # 分帧保存转换结果
            img_list.append(img)
        else:
            break
    # 结束时记得释放空间
    cap.release()
    return img_list




# 用于生成字符画的像素字符
pixels = " .,-'`:!1+*abcdefghijklmnopqrstuvwxyz<>()\/{}[]?234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ%&@#$"
# 将一帧图像转换为字符画
def img2chars(img):
    res=[]
    percents = img / 255
    # 将灰度值转换到0～（len(pixels)-1）之间，便于与pixels中的字符对应，并用其中的字符来表示图片
    indexes = (percents * (len(pixels) - 1)).astype(np.int)
    # shape返回行数，列数
    height, width = img.shape
    for row in range(height):
        line=''
        for col in range(width):
            index = indexes[row][col]
            # 添加字符像素
            line += pixels[index] + ' '
        res.append(line)
    return res


# 接受多帧为参数
def imgs2chars(imgs):
    video_chars = []
    for img in imgs:
        video_chars.append(img2chars(img))
    return video_chars




# 播放字符视频
def play_video(video_chars):
    # 获取字符画的尺寸
    width, height = len(video_chars[0][0]), len(video_chars[0])
    for pic_i in range(len(video_chars)):
        # 显示pic_i,即第i帧字符画
        for line_i in range(height):
            # 将pic_i的第i行写入第i列
            print(video_chars[pic_i][line_i])
        time.sleep(1/24) #粗略控制播放速度
        # 清屏
        os.system('cls')




# 将对象保存到本地
def save(obj, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(obj, f)
    return

# 从指定文件中加载对象
def load(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)


# 从文件路径中提取出不带扩展名的文件名
def get_file_name(path):
    # 获取文件名
    path,file_name_with_extension = os.path.split(path)
    # 获取文件名前缀
    file_name,file_extension = os.path.splitext(file_name_with_extension)
    return file_name



# 判断指定目录下是否有该文件
def has_file(path, file_name):
    return file_name in os.listdir(path)



# 返回对应的字符视频
def get_video_chars(video_path,size):
    # pickle模块保存转换过的video_chars
    video = get_file_name(video_path) + '.pickle'
    # video_dump = Path(video_path).with_suffix('.pickle').name
    # 如果有，则直接读取，不需要再次转换
    if has_file('.',video):
        video_chars = load(video)
    else:
        print('开始逐帧读取')
        # 视频转字符动画
        imgs = video2imgs(video_path,size)
        print('视频已全部转换为图像，开始逐帧转换为字符动画')
        video_chars = imgs2chars(imgs)
        print('转换完成，开始缓存结果')
        # 把转换结果保存下来
        save(video_chars,video)
        print('缓存完毕')
    return video_chars

if __name__ == "__main__":
    file_path = input('请输入要转换的文件地址')
    # 宽 高
    size = (64,48)
    # 视频路径
    # video_path = 'BadApple.mp4'
    video_path = file_path
    # 转换成字符
    video_chars = get_video_chars(video_path,size)
    # 播放
    play_video(video_chars)



# 打开一个新的终端，调整窗口大小
# 进入文件目录下,运行python video_char.py即可看到效果