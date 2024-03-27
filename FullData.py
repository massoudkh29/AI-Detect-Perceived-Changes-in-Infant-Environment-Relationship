import numpy as np
import pandas as pd
import scipy.io
import pickle
mat = scipy.io.loadmat('C:/Users/SB00763936/Desktop/AI-Baby/DIA AI/DIA116_fullset.mat')
# print(mat['CPelvis_exists'])
print(mat['babymobMarkerNames'])
print(mat['frameRate'])
# print(mat.values())
mylist = list(mat)

# for index, key in enumerate(mat):
#     print(index, key)

jointlists = ['head_X','head_Y','head_Z',
              'CPelvis_X','CPelvis_Y','CPelvis_Z',
              'LShoulder_X','LShoulder_Y','LShoulder_Z',
              'LHand_X','LHand_Y','LHand_Z',
              'RShoulder_X','RShoulder_Y','RShoulder_Z',
              'RHand_X','RHand_Y','RHand_Z',
              'LPelvis_X','LPelvis_Y','LPelvis_Z',
              'LHip_X','LHip_Y','LHip_Z',
              'LKnee_X','LKnee_Y','LKnee_Z',
              'LAnk_X','LAnk_Y','LAnk_Z',
              'Ltoe_X','Ltoe_Y','Ltoe_Z',
              'RPelvis_X','RPelvis_Y','RPelvis_Z',
              'RHip_X','RHip_Y','RHip_Z',
              'RKnee_X','RKnee_Y','RKnee_Z',
              'RAnk_X','RAnk_Y','RAnk_Z',
              'Rtoe_X','Rtoe_Y','Rtoe_Z']

# frame_num = 25000

slots =[[26,9027], [11367,23367], [30688,61120], [62040,74040]]
slotsname =['ranB1', 'ranB2', 'ranCR', 'ranDC']

for p, slot in enumerate (slots):
    for frame_num in range(slot[0], slot[1]):
        a=1
        frame = []
        frame.append(frame_num)
        for joint in jointlists:
            if mat[joint][0][frame_num] == 0:
                a=0
                break
            frame.append(mat[joint][0][frame_num])
        if a!=0:
            with open('C:/Users/SB00763936/Desktop/AI-Baby/DIA AI/fullset/'+'DIA116_'+slotsname[p]+'.txt', 'a') as file:
                file.write(f'{frame}\n')
                file.close()

    with open('C:/Users/SB00763936/Desktop/AI-Baby/DIA AI/fullset/'+'DIA116_'+slotsname[p]+'.txt','r') as file:
        filedata = file.read()
        filedata = filedata.replace(',', '').replace('[', '').replace(']', '').replace("'", '')

    with open('C:/Users/SB00763936/Desktop/AI-Baby/DIA AI/fullset/'+'DIA116_'+slotsname[p]+'.txt', 'w') as file:
        file.write(filedata)












BODY_PARTS_NAMES = ['head_X','CPelvis_X', 'LShoulder_X', 'LHand_X', 'RShoulder_X','RHand_X',
        'LPelvis_X', 'LHip_X', 'LKnee_X', 'LAnk_X', 'Ltoe_X',
        'RPelvis_X', 'RHip_X', 'RKnee_X','RAnk_X', 'Rtoe_X']
BONE_PAIRS = [[0, 1], [0, 2], [0, 4], [1, 6], [1, 11], [2, 3], [4, 5], [6, 7],
              [7, 8], [8, 9], [9, 10], [11, 12], [12, 13], [13, 14], [14, 15]]

