""" extended file for fulldata 1 - all subjects """

import numpy as np
import pandas as pd
import scipy.io
import pickle
import xlrd


# mat = scipy.io.loadmat('C:/Users/SB00763936/Desktop/AI-Baby/DIA AI/FullData/DIA124/full_set_S1.mat')


# jointlists = ['Head_X', 'Head_Y', 'Head_Z',
#               'CPelvis_X', 'CPelvis_Y', 'CPelvis_Z',
#               'LShoulder_X', 'LShoulder_Y', 'LShoulder_Z',
#               'LHand_X', 'LHand_Y', 'LHand_Z',
#               'RShoulder_X', 'RShoulder_Y', 'RShoulder_Z',
#               'RHand_X', 'RHand_Y', 'RHand_Z',
#               'LPelvis_X', 'LPelvis_Y', 'LPelvis_Z',
#               'LHip_X', 'LHip_Y', 'LHip_Z',
#               'LKnee_X', 'LKnee_Y', 'LKnee_Z',
#               'LAnk_X', 'LAnk_Y', 'LAnk_Z',
#               'LToe_X', 'LToe_Y', 'LToe_Z',
#               'RPelvis_X', 'RPelvis_Y', 'RPelvis_Z',
#               'RHip_X', 'RHip_Y', 'RHip_Z',
#               'RKnee_X', 'RKnee_Y', 'RKnee_Z',
#               'RAnk_X', 'RAnk_Y', 'RAnk_Z',
#               'RToe_X', 'RToe_Y', 'RToe_Z']

#no Head-Hand
jointlists = ['CPelvis_X', 'CPelvis_Y', 'CPelvis_Z',
              'LShoulder_X', 'LShoulder_Y', 'LShoulder_Z',
              'RShoulder_X', 'RShoulder_Y', 'RShoulder_Z',
              'LPelvis_X', 'LPelvis_Y', 'LPelvis_Z',
              'LHip_X', 'LHip_Y', 'LHip_Z',
              'LKnee_X', 'LKnee_Y', 'LKnee_Z',
              'LAnk_X', 'LAnk_Y', 'LAnk_Z',
              'LToe_X', 'LToe_Y', 'LToe_Z',
              'RPelvis_X', 'RPelvis_Y', 'RPelvis_Z',
              'RHip_X', 'RHip_Y', 'RHip_Z',
              'RKnee_X', 'RKnee_Y', 'RKnee_Z',
              'RAnk_X', 'RAnk_Y', 'RAnk_Z',
              'RToe_X', 'RToe_Y', 'RToe_Z']

file_location = 'C:/Users/SB00763936/Desktop/AI-Baby/DIA AI/FullData/'
workbook = xlrd.open_workbook(file_location + 'clip times.xlsx')
StartTimes = workbook.sheet_by_name('StartTimes')
StopTimes = workbook.sheet_by_name('StopTimes')
SessionNumber = workbook.sheet_by_name('SessionNumber')
# range (1,17):
# for row in range (16,17):
row = 16
SubjectNumber = SessionNumber.cell(row, 0).value
print('--------------------------------------------------------------')
print(SubjectNumber)
for column in range (1,6):
# for column in range (5,6):
    slotsname = SessionNumber.cell(0, column).value
    print (slotsname)
    Session = SessionNumber.cell(row, column).value
    print(Session)
    print(file_location+'DIA'+str(int(SubjectNumber))+'/full_set_S'+str(int(Session))+'.mat')
    mat = scipy.io.loadmat(file_location+'DIA'+str(int(SubjectNumber))+'/full_set_S'+str(int(Session))+'.mat')

    slot1 = StartTimes.cell(row, column).value
    print(slot1)
    slot2 = StopTimes.cell(row, column).value
    print (slot2)
    address = file_location + 'DIA' + str(int(SubjectNumber))+'/DIA' + str(int(SubjectNumber))+'_'+ slotsname + '.txt'
    print (address)
    for frame_num in range(int(slot1)*100, int(slot2)*100):
        a = 1
        frame = []
        frame.append(frame_num)
        for joint in jointlists:
            if mat[joint][0][frame_num] == 0:
                a = 0
                break
            frame.append(mat[joint][0][frame_num])
        if a != 0:
            with open(address,'a') as file:
                file.write(f'{frame}\n')
                file.close()

    with open(address, 'r') as file:
        filedata = file.read()
        filedata = filedata.replace(',', '').replace('[', '').replace(']', '').replace("'", '')

    with open(address, 'w') as file:
        file.write(filedata)

address1 = file_location + 'DIA' + str(int(SubjectNumber))
filenames = [address1+'/DIA' + str(int(SubjectNumber)) + '_B1.txt', address1+'/DIA' + str(int(SubjectNumber)) + '_B2.txt',
             address1+'/DIA' + str(int(SubjectNumber)) + '_CR1.txt',address1+'/DIA' + str(int(SubjectNumber)) + '_CR2.txt',
             address1+'/DIA' + str(int(SubjectNumber)) + '_DC.txt']
with open(address1+'/DIA' + str(int(SubjectNumber)) + '_All.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)






# BODY_PARTS_NAMES = ['head_X', 'CPelvis_X', 'LShoulder_X', 'LHand_X', 'RShoulder_X', 'RHand_X',
#                     'LPelvis_X', 'LHip_X', 'LKnee_X', 'LAnk_X', 'Ltoe_X',
#                     'RPelvis_X', 'RHip_X', 'RKnee_X', 'RAnk_X', 'Rtoe_X']
# BONE_PAIRS = [[0, 1], [0, 2], [0, 4], [1, 6], [1, 11], [2, 3], [4, 5], [6, 7],
#               [7, 8], [8, 9], [9, 10], [11, 12], [12, 13], [13, 14], [14, 15]]
