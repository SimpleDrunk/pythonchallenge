# http://www.pythonchallenge.com/pc/rock/arecibo.html


import urllib
from PIL import Image

def getdata(url):
    f = urllib.urlopen(url)
    flag = -1
    size = []
    hor = []
    ver = []
    temp = [size, hor, ver]
    for i in f.readlines():
        if i[0] == '#':
            flag += 1
        elif i[0] == '\n':
            pass
        else:
            temp[flag].append(map(int, i.split()))
    return (size[0][0], size[0][1], hor, ver)


def candidate(num, maxlen):
    '''针对给出的排列方式，递归获得所有的备选排列 点亮为# '''
    candi = []
    for i in range(maxlen + 2 - sum(num) - len(num)):
        cans = 'O' * i + '#' * num[0]
        if len(num) == 1:
            tail = 'O' * (maxlen - len(cans))
            candi.append(cans + tail)
        else:
            tail = ['O' + j for j in candidate(num[1:], maxlen - len(cans) - 1)]
            candi.extend([cans + j for j in tail])
    return candi


def findinit(x, y, hnum, vnum):
    '''找出每一行和每一列的备选排列'''
    candidateH = []
    candidateV = []
    for i in range(y):
        candidateH.append(candidate(hnum[i], x))
    for i in range(x):
        candidateV.append(candidate(vnum[i], y))
    return candidateH, candidateV


def check(candi, pos, flag):
    '''对某一行（列）在给定位置和给定状态选择不冲突的备选方案'''
    newcandi = []
    for i in candi:
        if i[pos] == flag:
            newcandi.append(i)
    return newcandi


def solver(url):
    xsize, ysize, hnum, vnum = getdata(url)
    candiH, candiV = findinit(xsize, ysize, hnum, vnum)
    result = []
    for i in range(xsize):
        result.append([' ' for j in range(ysize)])
    count = 0
    target = xsize * ysize
    while count < target:
        for index in range(xsize):  # 先针对每一行
            i = candiH[index]
            if i == 'done':
                continue
            elif len(i) == 1:
                for j in range(ysize):
                    if result[index][j] == ' ':
                        count += 1
                        result[index][j] = i[0][j]
                        candiV[j] = check(candiV[j], index, i[0][j])
                i = 'done'
            else:
                for j in range(ysize):
                    if result[index][j] != ' ':
                        continue
                    for k in i[1::]:
                        if k[j] != i[0][j]:
                            break
                    else:
                        result[index][j] = i[0][j]
                        count += 1
                        candiV[j] = check(candiV[j], index, i[0][j])

        for index in range(ysize):  # 再针对每一列，除个别变量外，代码相同
            i = candiV[index]
            if i == 'done':
                continue
            elif len(i) == 1:
                for j in range(xsize):
                    if result[j][index] == ' ':
                        count += 1
                        result[j][index] = i[0][j]
                        candiH[j] = check(candiH[j], index, i[0][j])
                i = 'done'
            else:
                for j in range(xsize):
                    if result[j][index] != ' ':
                        continue
                    for k in i[1::]:
                        if k[j] != i[0][j]:
                            break
                    else:
                        result[j][index] = i[0][j]
                        count += 1
                        candiH[j] = check(candiH[j], index, i[0][j])
    s = []
    for i in range(xsize):
        s.extend([1 if j == 'O' else 0 for j in result[i]])
    img = Image.new('1', (ysize, xsize))
    img.putdata(s)
    img.save('out31.png')
    return result


# solver('http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/warmup.txt')
solver('http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/up.txt')
