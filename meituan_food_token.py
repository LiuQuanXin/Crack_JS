#!/usr/bin/python
# -*- coding: utf-8 -*-
# time: 18/7/31


'''美团美食token获取
思路：根据get请求的params生成一个列表(待完成),根据列表来生成token，token生成2次，逐渐完整'''

url = 'http://gz.meituan.com/meishi/'

'''print("十进制数为：", dec)
print("转换为二进制为：", bin(dec))
print("转换为八进制为：", oct(dec))
print("转换为十六进制为：", hex(dec))
'''


def get_token():
    '''
    与或运算
    :return:
    '''
    s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    l = [120, 156, 37, 141, 77, 138, 194, 64, 16, 70, 239, 226, 162, 119, 49, 137, 137, 9, 17, 122, 33, 89, 9, 226, 110, 14, 80, 164, 203, 88, 152, 254, 161, 186, 90, 152, 57, 140, 215, 24, 102, 53, 167, 201, 61, 166, 71, 119, 143, 143, 199, 251, 54, 192, 8, 39, 163, 43, 53, 129, 224, 27, 72, 62, 47, 96, 81, 175, 63, 191, 235, 247, 83, 25, 114, 14, 121, 244, 201, 201, 81, 132, 179, 163, 124, 16, 178, 41, 142, 222, 160, 174, 149, 103, 154, 201, 125, 240, 162, 111]
    ih = []
    dy = 0
    bs = len(l)
    for i in range(bs):
        dy += 1
        if dy == 3:
            dy = 0
        dg = l[i]
        if dy == 0:
            index1 = ((l[i-1] << 2) | (dg >> 6)) & 0x3F
            index2 = dg & 0x3F
            ih.append(s[index1])
            ih.append(s[index2])
        elif dy == 1:
            ih.append(s[(dg >> 2) & 0x3F])
        else:
            index1 = ((l[i-1] << 4) | (dg >> 4)) & 0x3F
            ih.append(s[index1])
        if i == bs - 1 and dy > 0:
            index1 = (dg << ((3 - dy) << 1)) & 0x3F
            ih.append(s[index1])
    if dy:
        while dy < 3:
            dy += 1
            ih.append('=')
    print ''.join(ih)


if __name__ == '__main__':
    get_token()