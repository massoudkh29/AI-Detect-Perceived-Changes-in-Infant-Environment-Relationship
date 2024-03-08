import numpy as np
import math
import pandas as pd
import re
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import matplotlib
# from newHOJ3D_master import GP_algorithm as gp


def getMagnitude(vec):
    return math.sqrt(vec[0] * vec[0] + vec[1] * vec[1] + vec[2] * vec[2])


def dotProduct(vec1, vec2):
    return vec1[0] * vec2[0] + vec1[1] * vec2[1] + vec1[2] * vec2[2]


def scalarMult(s, vec):
    return [s * vec[0], s * vec[1], s * vec[2]]


def getData(filename):
    table = pd.read_table(filename, header=None, delim_whitespace=True)
    data = {'frame': table[0],
            'hip center': [table[1], table[2], table[3]],
            'left hip': [table[13], table[14], table[15]],
            'right hip': [table[28], table[29], table[30]],
            'left elbow': [table[4], table[5], table[6]],
            'right elbow': [table[7], table[8], table[9]],
            'left knee': [table[16], table[17], table[18]],
            'right knee': [table[31], table[32], table[33]],
            'left foot': [table[19], table[20], table[21]],
            'right foot': [table[34], table[35], table[36]]}
    return data


def getLabels(person):
    labels = 5 * [0]
    lineNo = 0
    sperson = str(int(person) + 1)
    pattern = re.compile(r"s" + sperson + "$")
    with open('BABYstages7Label.txt', 'rt') as in_file:
        j = 0
        for line in in_file:
            if ((lineNo >= 6 * person) & (lineNo < 6 * person + 6)):
                if (pattern.search(line) == None):
                    if (line.split(" ")[1] != "NaN"):
                        labels[j] = [line.split(" ")[0], int(line.split(" ")[1]), int(line.split(" ")[2])]
                    j += 1
            lineNo += 1
    return labels


def prepData(data, person, joints):
    # print('joints==', joints)
    labels = getLabels(person)
    angleData = 5 * [0]
    for j in range(0, 5):
        index = 0
        if (index < len(data['frame'])):
            # lowFrame = labels[j][1]
            # highFrame = labels[j][2]

            # lowFrame = labels[j][1] + 1200
            # highFrame = labels[j][1] + 1800

            # lowFrame = labels[j][1] + 0
            # highFrame = labels[j][1] + 5000

            D = labels[j][2] - labels[j][1]
            d = D // 2
            lowFrame = labels[j][1] + d - 500
            highFrame = lowFrame + 1000

            print('lowFrame - highFrame:', lowFrame, '-', highFrame)
            frameData = []
            q = True
            while (q & (data['frame'][index] < lowFrame)):
                index += 1
                if (index == len(data['frame'])):
                    index -= 1
                    q = False
            index2 = index
            while ((data['frame'][index] <= highFrame) & q):
                x0 = data[joints][0][index]
                y0 = data[joints][1][index]
                z0 = data[joints][2][index]
                # frameData.append([])
                frameData.append([x0, y0, z0])
                index += 1
                if (index == len(data['frame'])):
                    index -= 1
                    q = False
            angleData[j] = frameData
    return angleData
    # return frameData


if __name__ == '__main__':
    # joints0 = ['right foot', 'left foot', 'right elbow', 'left elbow']
    # D = []
    # DD = []
    # for joints in joints0:
    #     for kk in range(5):
    #         i = 0
    #         aa = []
    #         bb = []
    #         cc = []
    #         sperson = str(int(i + 1))
    #         filename = 'BABYjoints/Test 7 Labels/joints_' + sperson + '.txt'
    #         datas = prepData(getData(filename), i, joints)
    #         print(f'{joints}-stage {kk + 1} samples:', len(datas[kk]))
    #         for k in range(0, len(datas[kk])):
    #             a = datas[kk][k][0]
    #             b = datas[kk][k][1]
    #             c = datas[kk][k][2]
    #             aa.append(a)
    #             bb.append(b)
    #             cc.append(c)
    #         npa = np.asarray(aa, dtype=np.float32)
    #         npb = np.asarray(bb, dtype=np.float32)
    #         npc = np.asarray(cc, dtype=np.float32)
    #         emb_dim = 3
    #         time_delay = 20
    #         timeseries0 = npa
    #         timeseries1 = npb
    #         timeseries2 = npc
    #         D0 = gp.grassberg_procaccia(timeseries0, emb_dim, time_delay, plot=False)
    #         D1 = gp.grassberg_procaccia(timeseries1, emb_dim, time_delay, plot=False)
    #         D2 = gp.grassberg_procaccia(timeseries2, emb_dim, time_delay, plot=False)
    #         d = np.average([D0, D1, D2])
    #         D.append(d)
    #     print ('D=',D)
    #     DD.append(D)
    # print('DD=', DD)

    # ['right foot']
    St1_rf = np.average([1.422, 1.6349419831816012, 1.1356283781164316, 1.9266291720696611, 1.2396507880710175])
    St2_rf = np.average([1.516, 1.0407417769440082, 1.4856746997384354, 1.1280057451225602, 1.215390098201406])
    St3_rf = np.average([1.451, 1.5205952128731937, 1.7573714297764749, 1.8404243266467246, 1.5501850286081977])
    St4_rf = np.average([1.646, 1.6139953944012202, 1.1698929930604285, 1.6802351868850625, 1.405787097382995])
    St5_rf = np.average([1.500, 1.305061053115791, 1.6699510427776598, 1.325459469698509, 1.3611595612732055])

    # [ 'left foot']
    St1_lf = np.average([1.317, 1.8262431339590666, 1.1165851789996772, 1.8100501889629255, 1.5222345351726165])
    St2_lf = np.average([1.676, 0.9163399091292558, 1.4148663018449745, 1.9102835239007412, 1.0679389255173006])
    St3_lf = np.average([1.532, 1.617686812400331, 1.8014948692260742, 1.9139897681756655, 1.3854871160856348])
    St4_lf = np.average([1.475, 1.4064765407033202, 1.3479090309657995, 1.7306520012422097, 1.474857065466656])
    St5_lf = np.average([1.827, 1.6967309960596044, 2.0586897877536465, 1.3038306648093467, 1.2324282589941788])

    # ['right elbow']
    St1_re = np.average([1.587, 1.8771574260551602, 1.8378568737944085, 2.245367343014653, 1.646439658261851])
    St2_re = np.average([2.196, 1.7515194051884235, 1.9577325290268057, 1.928740542860484, 1.7199610516231756])
    St3_re = np.average([1.727, 2.0182072426615485, 1.6398887963296007, 2.0415147324593987, 1.8521054135507462])
    St4_re = np.average([1.598, 1.8898609812173401, 1.7694186966740668, 1.9486633086864444, 1.932312937678936])
    St5_re = np.average([1.876, 1.865629012624467, 1.796976281521344, 1.3514679721018972, 1.623970272795712])

    # [' 'left elbow']
    St1_le = np.average([1.344, 1.885276473538319, 1.7472022243218752, 2.1474067560778862, 1.7397134072481464])
    St2_le = np.average([1.834, 1.7363906621692131, 1.5847513968251075, 2.057871603573336, 1.5653621628196959])
    St3_le = np.average([2.073, 1.7636276815257312, 1.7781816747745651, 2.1573425497499468, 1.630641659870706])
    St4_le = np.average([1.981, 1.5784255928972255, 1.5811207105778937, 1.936793740427505, 1.5650776609871169])
    St5_le = np.average([1.897, 1.840796593926002, 1.8776876664098108, 1.3493263996620213, 1.6169960603658666])

    N = 5
    ind = np.arange(N)  # the x locations for the groups
    width = 0.15  # the width of the bars
    fig = plt.figure()
    ax = fig.add_subplot(111)
    X_rf = [St1_rf, St2_rf, St3_rf, St4_rf, St5_rf]
    rects1 = ax.bar(ind, X_rf, width, color='r', label='right foot')
    X_lf = [St1_lf, St2_lf, St3_lf, St4_lf, St5_lf]
    rects2 = ax.bar(ind + width, X_lf, width, color='g', label='left foot')
    X_re = [St1_re, St2_re, St3_re, St4_re, St5_re]
    rects3 = ax.bar(ind + width * 2, X_re, width, color='b', label='right elbow')
    X_le = [St1_le, St2_le, St3_le, St4_le, St5_le]
    rects4 = ax.bar(ind + width * 3, X_le, width, color='c' , label='left elbow')

    ax.set_ylabel('correlation dimensions D ', fontsize=15)
    ax.set_xlabel('Stages ', fontsize=15)
    ax.set_xticks(ind + width)
    ax.set_xticklabels(('B1', 'B2', 'CR1', 'CR2', 'DC'), fontsize=15)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),
          fancybox=True, shadow=True, ncol=5)
    plt.show()

    # X_rf = [St1_rf,St2_rf,St3_rf,St4_rf,St5_rf]
    # plt.bar(np.arange(len(X_rf)), X_rf)
    # X_lf = [St1_lf, St2_lf, St3_lf, St4_lf, St5_lf]
    # plt.bar(np.arange(len(X_lf)), X_lf)
    # X_re = [St1_re, St2_re, St3_re, St4_re, St5_re]
    # plt.bar(np.arange(len(X_re)), X_re)
    # X_le = [St1_le, St2_le, St3_le, St4_le, St5_le]
    # plt.bar(np.arange(len(X_le)), X_le)
    # plt.title('left elbow', fontsize=15)
    # plt.ylabel('correlation dimensions D', fontsize=15)
    # plt.xlabel('Stages', fontsize=15)
    # plt.xticks(size=15)
    # plt.yticks(size=15)
    # plt.show()

    print('v')

    # #----------------------------------------------Lorenze Equation
    # plt.rcParams['figure.figsize'] = [5, 5]
    #
    # def lorenz(x, y, z, s=10, r=28, b=2.667):
    #     '''Given:
    #        x, y, z: a point of interest in three dimensional space
    #        s, r, b: parameters defining the lorenz attractor
    #     Returns:
    #        x_dot, y_dot, z_dot: values of the lorenz attractor's partial derivatives at the point x, y, z'''
    #     x_dot = s * (y - x)
    #     y_dot = r * x - y - x * z
    #     z_dot = x * y - b * z
    #     return x_dot, y_dot, z_dot
    # dt = 0.01
    # num_steps = 10000
    #
    # # Need one more for the initial values
    # xs = np.empty(num_steps + 1)
    # ys = np.empty(num_steps + 1)
    # zs = np.empty(num_steps + 1)
    #
    # # Set initial values
    # xs[0], ys[0], zs[0] = (0., 1., 1.05)
    #
    # # Step through "time", calculating the partial derivatives at the current point and using them to estimate the next point
    # for i in range(num_steps):
    #     x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
    #     xs[i + 1] = xs[i] + (x_dot * dt)
    #     ys[i + 1] = ys[i] + (y_dot * dt)
    #     zs[i + 1] = zs[i] + (z_dot * dt)
    #
    # emb_dim = 3
    # # Arbitrary time delay
    # time_delay = 20
    # timeseries = xs[:1500]
    #
    # # Algortuhm execution to get the dimension
    # D = gp.grassberg_procaccia(timeseries, emb_dim, time_delay, plot=True)
    # d=1
