# -*- coding: utf-8 -*-
from __future__ import print_function

import matplotlib.pyplot as plt
import numpy as np
import operator
import random

from scipy.spatial import ConvexHull

# 随机数据
n = random.randrange(10,20)
# points = [
#     (
#         random.randrange(0, 20),
#         random.randrange(0, 20),
#         #random.randrange(-100, 100),
#         #random.randrange(-100, 100),
#     ) for _ in range(n)
# ]
n = 13
points=[(7,-11),(-1,-3),(7,-20),(19,7),(-2,-11),(-16,1),(1,16),(10,-19),(14,-10),(18,-1),(-20,2),(-17,-19),(-19,-3)]

# 保存输入文件
with open('unsorted.txt', 'w') as f:
    print(n, file=f)
    for x, y in points:
        print(x, y, file=f)
points.sort(key=operator.itemgetter(0))
with open('sorted.txt', 'w') as f:
    print(n, file=f)
    for x, y in points:
        print(x, y, file=f)

# 计算凸包
points = np.array(points, dtype=np.int64)
hull = ConvexHull(points)
hullpoints = points[hull.vertices]

# 找起始点
start = 0
for i, (x, y) in enumerate(hullpoints):
    if y < hullpoints[start][1] or \
            y == hullpoints[start][1] and \
            x < hullpoints[start][0]:
        start = i

# 输出参考答案文件
hullpoints = np.concatenate((hullpoints[start:, :], hullpoints[:start, :]))
with open('answer.txt', 'w') as f:
    for x, y in hullpoints:
        print(x, y, file=f)

# 画图
plt.plot(points[:, 0], points[:, 1], 'o')
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'r-')
plt.show()
