
#Plot Tools
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

#Data Tools
import numpy as np
import pandas as pd
from scipy.stats import linregress

#Models
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.neural_network import MLPClassifier




#Utility
import os
import random
import math
import itertools as itools
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix #import confusion_matrix

from sklearn.metrics import classification_report #import classification_report

from sklearn import tree

import time

from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

start_time = time.time()



#--------------------------------------------------------------------

def Average(lst):
    return float("{:.3f}".format(sum(lst) / len(lst)))


def getFeature(S_path,F_path,W_path):


    #List For Return Result
    #[AccX_Max, AccX_Min, AccX_Avg, AccY_Max, AccY_Min, AccY_Avg, AccZ_Max, AccZ_Min, AccZ_Avg, AccX/AccY, AccX/AccZ, AccY/AccZ]
    fea_result = []

    #Read Path
    data = pd.DataFrame(pd.read_excel(S_path)).to_numpy()

    #Tmp Var
    aX = []
    aY = []
    aZ = []

    cc_xy = 0
    cc_xz = 0
    cc_yz = 0


    #Obtain each accX, accY, accZ
    for unitTime in data:
        aX.append(unitTime[5])
        aY.append(unitTime[6])
        aZ.append(unitTime[7])

        tmp_cc_xy = unitTime[5]*unitTime[6]
        tmp_cc_xz = unitTime[5]*unitTime[7]
        tmp_cc_yz = unitTime[6]*unitTime[7]

        cc_xy += tmp_cc_xy
        cc_xz += tmp_cc_xz
        cc_yz += tmp_cc_yz

    fea_result.append(max(aX))
    fea_result.append(min(aX))
    fea_result.append(Average(aX))
    fea_result.append(max(aY))
    fea_result.append(min(aY))
    fea_result.append(Average(aY))
    fea_result.append(max(aZ))
    fea_result.append(min(aZ))
    fea_result.append(Average(aZ))
    fea_result.append(float("{:.3f}".format(cc_xy)))
    fea_result.append(float("{:.3f}".format(cc_xz)))
    fea_result.append(float("{:.3f}".format(cc_yz)))

    #Read Path
    data = pd.DataFrame(pd.read_excel(F_path)).to_numpy()

    #Tmp Var
    aX = []
    aY = []
    aZ = []

    cc_xy = 0
    cc_xz = 0
    cc_yz = 0


    #Obtain each accX, accY, accZ
    for unitTime in data:
        aX.append(unitTime[5])
        aY.append(unitTime[6])
        aZ.append(unitTime[7])

        tmp_cc_xy = unitTime[5]*unitTime[6]
        tmp_cc_xz = unitTime[5]*unitTime[7]
        tmp_cc_yz = unitTime[6]*unitTime[7]

        cc_xy += tmp_cc_xy
        cc_xz += tmp_cc_xz
        cc_yz += tmp_cc_yz

    fea_result.append(max(aX))
    fea_result.append(min(aX))
    fea_result.append(Average(aX))
    fea_result.append(max(aY))
    fea_result.append(min(aY))
    fea_result.append(Average(aY))
    fea_result.append(max(aZ))
    fea_result.append(min(aZ))
    fea_result.append(Average(aZ))
    fea_result.append(float("{:.3f}".format(cc_xy)))
    fea_result.append(float("{:.3f}".format(cc_xz)))
    fea_result.append(float("{:.3f}".format(cc_yz)))

    #Read Path
    data = pd.DataFrame(pd.read_excel(W_path)).to_numpy()

    #Tmp Var
    aX = []
    aY = []
    aZ = []

    cc_xy = 0
    cc_xz = 0
    cc_yz = 0


    #Obtain each accX, accY, accZ
    for unitTime in data:
        aX.append(unitTime[5])
        aY.append(unitTime[6])
        aZ.append(unitTime[7])

        tmp_cc_xy = unitTime[5]*unitTime[6]
        tmp_cc_xz = unitTime[5]*unitTime[7]
        tmp_cc_yz = unitTime[6]*unitTime[7]

        cc_xy += tmp_cc_xy
        cc_xz += tmp_cc_xz
        cc_yz += tmp_cc_yz

    fea_result.append(max(aX))
    fea_result.append(min(aX))
    fea_result.append(Average(aX))
    fea_result.append(max(aY))
    fea_result.append(min(aY))
    fea_result.append(Average(aY))
    fea_result.append(max(aZ))
    fea_result.append(min(aZ))
    fea_result.append(Average(aZ))
    fea_result.append(float("{:.3f}".format(cc_xy)))
    fea_result.append(float("{:.3f}".format(cc_xz)))
    fea_result.append(float("{:.3f}".format(cc_yz)))

    return fea_result


def td_Append(Max_aX_list,Max_aY_list,Max_aZ_list,
              Min_aX_list,Min_aY_list,Min_aZ_list,
              Avg_aX_list,Avg_aY_list,Avg_aZ_list,
              CC_XY_list,CC_XZ_list,CC_YZ_list,
              aX, aY, aZ, cc_xy, cc_xz, cc_yz):

    Max_aX_list.append(max(aX))
    Max_aY_list.append(max(aY))
    Max_aZ_list.append(max(aZ))
    Min_aX_list.append(min(aX))
    Min_aY_list.append(min(aY))
    Min_aZ_list.append(min(aZ))
    Avg_aX_list.append(Average(aX))
    Avg_aY_list.append(Average(aY))
    Avg_aZ_list.append(Average(aZ))
    CC_XY_list.append(float("{:.3f}".format(cc_xy)))
    CC_XZ_list.append(float("{:.3f}".format(cc_xz)))
    CC_YZ_list.append(float("{:.3f}".format(cc_yz)))


def td_add2_YES_Container(Max_aX_list,Max_aY_list,Max_aZ_list,
              Min_aX_list,Min_aY_list,Min_aZ_list,
              Avg_aX_list,Avg_aY_list,Avg_aZ_list,
              CC_XY_list,CC_XZ_list,CC_YZ_list):
    
    YESList_Container.append(Max_aX_list)
    YESList_Container.append(Max_aY_list)
    YESList_Container.append(Max_aZ_list)
    YESList_Container.append(Min_aX_list)
    YESList_Container.append(Min_aY_list)
    YESList_Container.append(Min_aZ_list)
    YESList_Container.append(Avg_aX_list)
    YESList_Container.append(Avg_aY_list)
    YESList_Container.append(Avg_aZ_list)
    YESList_Container.append(CC_XY_list)
    YESList_Container.append(CC_XZ_list)
    YESList_Container.append(CC_YZ_list)

def td_add2_NO_Container(Max_aX_list,Max_aY_list,Max_aZ_list,
              Min_aX_list,Min_aY_list,Min_aZ_list,
              Avg_aX_list,Avg_aY_list,Avg_aZ_list,
              CC_XY_list,CC_XZ_list,CC_YZ_list):
    
    NOList_Container.append(Max_aX_list)
    NOList_Container.append(Max_aY_list)
    NOList_Container.append(Max_aZ_list)
    NOList_Container.append(Min_aX_list)
    NOList_Container.append(Min_aY_list)
    NOList_Container.append(Min_aZ_list)
    NOList_Container.append(Avg_aX_list)
    NOList_Container.append(Avg_aY_list)
    NOList_Container.append(Avg_aZ_list)
    NOList_Container.append(CC_XY_list)
    NOList_Container.append(CC_XZ_list)
    NOList_Container.append(CC_YZ_list)


def chopList(list, targetLen):
    
    resultList = []

    for sublist in list:
        sublist = sublist[0:targetLen]
        resultList.append(sublist)
       

    return resultList

    
#-------------------------------------------------------------------- 

S_YES_Max_aX_list = []
S_YES_Max_aY_list = []
S_YES_Max_aZ_list = []

S_YES_Min_aX_list = []
S_YES_Min_aY_list = []
S_YES_Min_aZ_list = []

S_YES_Avg_aX_list = []
S_YES_Avg_aY_list = []
S_YES_Avg_aZ_list = []

S_YES_CC_XY_list = []
S_YES_CC_XZ_list = []
S_YES_CC_YZ_list = []

S_NO_Max_aX_list = []
S_NO_Max_aY_list = []
S_NO_Max_aZ_list = []

S_NO_Min_aX_list = []
S_NO_Min_aY_list = []
S_NO_Min_aZ_list = []

S_NO_Avg_aX_list = []
S_NO_Avg_aY_list = []
S_NO_Avg_aZ_list = []

S_NO_CC_XY_list = []
S_NO_CC_XZ_list = []
S_NO_CC_YZ_list = []

#-------------------------------------------------------------------- 

F_YES_Max_aX_list = []
F_YES_Max_aY_list = []
F_YES_Max_aZ_list = []

F_YES_Min_aX_list = []
F_YES_Min_aY_list = []
F_YES_Min_aZ_list = []

F_YES_Avg_aX_list = []
F_YES_Avg_aY_list = []
F_YES_Avg_aZ_list = []

F_YES_CC_XY_list = []
F_YES_CC_XZ_list = []
F_YES_CC_YZ_list = []

F_NO_Max_aX_list = []
F_NO_Max_aY_list = []
F_NO_Max_aZ_list = []

F_NO_Min_aX_list = []
F_NO_Min_aY_list = []
F_NO_Min_aZ_list = []

F_NO_Avg_aX_list = []
F_NO_Avg_aY_list = []
F_NO_Avg_aZ_list = []

F_NO_CC_XY_list = []
F_NO_CC_XZ_list = []
F_NO_CC_YZ_list = []


#--------------------------------------------------------------------  


W_YES_Max_aX_list = []
W_YES_Max_aY_list = []
W_YES_Max_aZ_list = []

W_YES_Min_aX_list = []
W_YES_Min_aY_list = []
W_YES_Min_aZ_list = []

W_YES_Avg_aX_list = []
W_YES_Avg_aY_list = []
W_YES_Avg_aZ_list = []

W_YES_CC_XY_list = []
W_YES_CC_XZ_list = []
W_YES_CC_YZ_list = []

W_NO_Max_aX_list = []
W_NO_Max_aY_list = []
W_NO_Max_aZ_list = []

W_NO_Min_aX_list = []
W_NO_Min_aY_list = []
W_NO_Min_aZ_list = []

W_NO_Avg_aX_list = []
W_NO_Avg_aY_list = []
W_NO_Avg_aZ_list = []

W_NO_CC_XY_list = []
W_NO_CC_XZ_list = []
W_NO_CC_YZ_list = []

#----------------------------Program Starts Here----------------------------------------  

#1. Traverse Raw Data Folder to obtain each observation's path
RootFolder_Path = 'e:/Project_Workspace/MocapSport/Court_Data/'

Observation_Path_List = []

for root,dirs,files in os.walk(RootFolder_Path):

    #root - Current Root Path
    #files - all file list under the 'root' path
    

    for file in files:

        curr_path = os.path.join(root,file)
        unixTime = os.path.getmtime(curr_path)
        

        Observation_Path_List.append(curr_path)
        #print(os.path.join(root,file))
        # print()
       

#--------------------------------------------------------------------        

#2. Read Path and Record Features

S_YES_matches = ['Shoulder','YES']
S_NO_matches = ['Shoulder','NO']
F_YES_matches = ['Forearm','YES']
F_NO_matches = ['Forearm','NO']
W_YES_matches = ['Wrist','YES']
W_NO_matches = ['Wrist','NO']


YESList_Container = [] #For future list chopping
NOList_Container = []


for path in Observation_Path_List:

    #Read Path
    data = pd.DataFrame(pd.read_excel(path)).to_numpy()

    #Tmp Var
    aX = []
    aY = []
    aZ = []

    cc_xy = 0
    cc_xz = 0
    cc_yz = 0

    #Obtain each accX, accY, accZ
    for unitTime in data:
        aX.append(unitTime[5])
        aY.append(unitTime[6])
        aZ.append(unitTime[7])

        tmp_cc_xy = unitTime[5]*unitTime[6]
        tmp_cc_xz = unitTime[5]*unitTime[7]
        tmp_cc_yz = unitTime[6]*unitTime[7]

        cc_xy += tmp_cc_xy
        cc_xz += tmp_cc_xz
        cc_yz += tmp_cc_yz


    if all([c in path for c in S_YES_matches]):

        td_Append(S_YES_Max_aX_list,S_YES_Max_aY_list,S_YES_Max_aZ_list,
                  S_YES_Min_aX_list,S_YES_Min_aY_list,S_YES_Min_aZ_list,
                  S_YES_Avg_aX_list,S_YES_Avg_aY_list,S_YES_Avg_aZ_list,
                  S_YES_CC_XY_list,S_YES_CC_XZ_list,S_YES_CC_YZ_list,
                  aX,aY,aZ,cc_xy,cc_xz,cc_yz)
        

    
    elif all([c in path for c in S_NO_matches]):

        td_Append(S_NO_Max_aX_list,S_NO_Max_aY_list,S_NO_Max_aZ_list,
                  S_NO_Min_aX_list,S_NO_Min_aY_list,S_NO_Min_aZ_list,
                  S_NO_Avg_aX_list,S_NO_Avg_aY_list,S_NO_Avg_aZ_list,
                  S_NO_CC_XY_list,S_NO_CC_XZ_list,S_NO_CC_YZ_list,
                  aX,aY,aZ,cc_xy,cc_xz,cc_yz)
        
    elif all([c in path for c in F_YES_matches]):

        td_Append(F_YES_Max_aX_list,F_YES_Max_aY_list,F_YES_Max_aZ_list,
                  F_YES_Min_aX_list,F_YES_Min_aY_list,F_YES_Min_aZ_list,
                  F_YES_Avg_aX_list,F_YES_Avg_aY_list,F_YES_Avg_aZ_list,
                  F_YES_CC_XY_list,F_YES_CC_XZ_list,F_YES_CC_YZ_list,
                  aX,aY,aZ,cc_xy,cc_xz,cc_yz)
        


    elif all([c in path for c in F_NO_matches]):

        td_Append(F_NO_Max_aX_list,F_NO_Max_aY_list,F_NO_Max_aZ_list,
                  F_NO_Min_aX_list,F_NO_Min_aY_list,F_NO_Min_aZ_list,
                  F_NO_Avg_aX_list,F_NO_Avg_aY_list,F_NO_Avg_aZ_list,
                  F_NO_CC_XY_list,F_NO_CC_XZ_list,F_NO_CC_YZ_list,
                  aX,aY,aZ,cc_xy,cc_xz,cc_yz)

    elif all([c in path for c in W_YES_matches]):

        td_Append(W_YES_Max_aX_list,W_YES_Max_aY_list,W_YES_Max_aZ_list,
                  W_YES_Min_aX_list,W_YES_Min_aY_list,W_YES_Min_aZ_list,
                  W_YES_Avg_aX_list,W_YES_Avg_aY_list,W_YES_Avg_aZ_list,
                  W_YES_CC_XY_list,W_YES_CC_XZ_list,W_YES_CC_YZ_list,
                  aX,aY,aZ,cc_xy,cc_xz,cc_yz)
        

        

    elif all([c in path for c in W_NO_matches]):

        td_Append(W_NO_Max_aX_list,W_NO_Max_aY_list,W_NO_Max_aZ_list,
                  W_NO_Min_aX_list,W_NO_Min_aY_list,W_NO_Min_aZ_list,
                  W_NO_Avg_aX_list,W_NO_Avg_aY_list,W_NO_Avg_aZ_list,
                  W_NO_CC_XY_list,W_NO_CC_XZ_list,W_NO_CC_YZ_list,
                  aX,aY,aZ,cc_xy,cc_xz,cc_yz)
        

td_add2_YES_Container(S_YES_Max_aX_list,S_YES_Max_aY_list,S_YES_Max_aZ_list,
        S_YES_Min_aX_list,S_YES_Min_aY_list,S_YES_Min_aZ_list,
        S_YES_Avg_aX_list,S_YES_Avg_aY_list,S_YES_Avg_aZ_list,
        S_YES_CC_XY_list,S_YES_CC_XZ_list,S_YES_CC_YZ_list)

td_add2_YES_Container(F_YES_Max_aX_list,F_YES_Max_aY_list,F_YES_Max_aZ_list,
        F_YES_Min_aX_list,F_YES_Min_aY_list,F_YES_Min_aZ_list,
        F_YES_Avg_aX_list,F_YES_Avg_aY_list,F_YES_Avg_aZ_list,
        F_YES_CC_XY_list,F_YES_CC_XZ_list,F_YES_CC_YZ_list)

td_add2_YES_Container(W_YES_Max_aX_list,W_YES_Max_aY_list,W_YES_Max_aZ_list,
        W_YES_Min_aX_list,W_YES_Min_aY_list,W_YES_Min_aZ_list,
        W_YES_Avg_aX_list,W_YES_Avg_aY_list,W_YES_Avg_aZ_list,
        W_YES_CC_XY_list,W_YES_CC_XZ_list,W_YES_CC_YZ_list)


td_add2_NO_Container(S_NO_Max_aX_list,S_NO_Max_aY_list,S_NO_Max_aZ_list,
        S_NO_Min_aX_list,S_NO_Min_aY_list,S_NO_Min_aZ_list,
        S_NO_Avg_aX_list,S_NO_Avg_aY_list,S_NO_Avg_aZ_list,
        S_NO_CC_XY_list,S_NO_CC_XZ_list,S_NO_CC_YZ_list)

td_add2_NO_Container(F_NO_Max_aX_list,F_NO_Max_aY_list,F_NO_Max_aZ_list,
        F_NO_Min_aX_list,F_NO_Min_aY_list,F_NO_Min_aZ_list,
        F_NO_Avg_aX_list,F_NO_Avg_aY_list,F_NO_Avg_aZ_list,
        F_NO_CC_XY_list,F_NO_CC_XZ_list,F_NO_CC_YZ_list)

td_add2_NO_Container(W_NO_Max_aX_list,W_NO_Max_aY_list,W_NO_Max_aZ_list,
        W_NO_Min_aX_list,W_NO_Min_aY_list,W_NO_Min_aZ_list,
        W_NO_Avg_aX_list,W_NO_Avg_aY_list,W_NO_Avg_aZ_list,
        W_NO_CC_XY_list,W_NO_CC_XZ_list,W_NO_CC_YZ_list)
        
#Combine YES+NO Features for Shoulder, Forearm, Wrist, repectively

# OneBodyPart AccX || OneBodyPart AccY || ... || OneBody
# obs1
# obs2


#Chop to the min len
min_YES_len = min([len(S_YES_Avg_aX_list),len(F_YES_Avg_aX_list),len(W_YES_Avg_aX_list)])
min_NO_len = min([len(S_NO_Avg_aX_list),len(F_NO_Avg_aX_list),len(W_NO_Avg_aX_list)])


YESList_Container = chopList(YESList_Container,min_YES_len)
NOList_Container = chopList(NOList_Container,min_NO_len)

#Join YES+NO list
S_Max_aX_list = YESList_Container[0] + NOList_Container[0]
S_Max_aY_list = YESList_Container[1] + NOList_Container[1]
S_Max_aZ_list = YESList_Container[2] + NOList_Container[2]

S_Min_aX_list = YESList_Container[3] + NOList_Container[3]
S_Min_aY_list = YESList_Container[4] + NOList_Container[4]
S_Min_aZ_list = YESList_Container[5] + NOList_Container[5]

S_Avg_aX_list = YESList_Container[6] + NOList_Container[6]
S_Avg_aY_list = YESList_Container[7] + NOList_Container[7]
S_Avg_aZ_list = YESList_Container[8] + NOList_Container[8]

S_CC_XY_list = YESList_Container[9] + NOList_Container[9]
S_CC_XZ_list = YESList_Container[10] + NOList_Container[10]
S_CC_YZ_list = YESList_Container[11] + NOList_Container[11]

F_Max_aX_list = YESList_Container[12] + NOList_Container[12]
F_Max_aY_list = YESList_Container[13] + NOList_Container[13]
F_Max_aZ_list = YESList_Container[14] + NOList_Container[14]

F_Min_aX_list = YESList_Container[15] + NOList_Container[15]
F_Min_aY_list = YESList_Container[16] + NOList_Container[16]
F_Min_aZ_list = YESList_Container[17] + NOList_Container[17]

F_Avg_aX_list = YESList_Container[18] + NOList_Container[18]
F_Avg_aY_list = YESList_Container[19] + NOList_Container[19]
F_Avg_aZ_list = YESList_Container[20] + NOList_Container[20]

F_CC_XY_list = YESList_Container[21] + NOList_Container[21]
F_CC_XZ_list = YESList_Container[22] + NOList_Container[22]
F_CC_YZ_list = YESList_Container[23] + NOList_Container[23]

W_Max_aX_list = YESList_Container[24] + NOList_Container[24]
W_Max_aY_list = YESList_Container[25] + NOList_Container[25]
W_Max_aZ_list = YESList_Container[26] + NOList_Container[26]

W_Min_aX_list = YESList_Container[27] + NOList_Container[27]
W_Min_aY_list = YESList_Container[28] + NOList_Container[28]
W_Min_aZ_list = YESList_Container[29] + NOList_Container[29]

W_Avg_aX_list = YESList_Container[30] + NOList_Container[30]
W_Avg_aY_list = YESList_Container[31] + NOList_Container[31]
W_Avg_aZ_list = YESList_Container[32] + NOList_Container[32]

W_CC_XY_list = YESList_Container[33] + NOList_Container[33]
W_CC_XZ_list = YESList_Container[34] + NOList_Container[34]
W_CC_YZ_list = YESList_Container[35] + NOList_Container[35]


YES_response = []
NO_response = []

for re_len in range(min_YES_len):
    YES_response.append(1)

for re_len in range(min_NO_len):
    NO_response.append(0)

response_List = np.array(YES_response + NO_response)




features = pd.DataFrame({'S_AccX_Max': S_Max_aX_list,
                   'S_AccX_Min': S_Min_aX_list,
                    'S_AccX_Avg': S_Avg_aX_list,
                    'S_AccY_Max': S_Max_aY_list,
                    'S_AccY_Min': S_Min_aY_list,
                    'S_AccY_Avg': S_Avg_aY_list,
                    'S_AccZ_Max': S_Max_aZ_list,
                    'S_AccZ_Min': S_Min_aZ_list,
                    'S_AccZ_Avg': S_Avg_aZ_list,
                    'S_AccX/AccY':S_CC_XY_list,
                    'S_AccX/AccZ':S_CC_XZ_list,
                    'S_AccY/AccZ': S_CC_YZ_list,

                    'F_AccX_Max': F_Max_aX_list,
                    'F_AccX_Min': F_Min_aX_list,
                    'F_AccX_Avg': F_Avg_aX_list,
                    'F_AccY_Max': F_Max_aY_list,
                    'F_AccY_Min': F_Min_aY_list,
                    'F_AccY_Avg': F_Avg_aY_list,
                    'F_AccZ_Max': F_Max_aZ_list,
                    'F_AccZ_Min': F_Min_aZ_list,
                    'F_AccZ_Avg': F_Avg_aZ_list,
                    'F_AccX/AccY':F_CC_XY_list,
                    'F_AccX/AccZ':F_CC_XZ_list,
                    'F_AccY/AccZ':F_CC_YZ_list,

                    'W_AccX_Max': W_Max_aX_list,
                    'W_AccX_Min': W_Min_aX_list,
                    'W_AccX_Avg': W_Avg_aX_list,
                    'W_AccY_Max': W_Max_aY_list,
                    'W_AccY_Min': W_Min_aY_list,
                    'W_AccY_Avg': W_Avg_aY_list,
                    'W_AccZ_Max': W_Max_aZ_list,
                    'W_AccZ_Min': W_Min_aZ_list,
                    'W_AccZ_Avg': W_Avg_aZ_list,
                    'W_AccX/AccY':W_CC_XY_list,
                    'W_AccX/AccZ':W_CC_XZ_list,
                    'W_AccY/AccZ':W_CC_YZ_list,
                    })

TD_path = 'e:/Project_Workspace/MocapSport/'
#features.to_csv(TD_path+'file1.csv',index=False)
features = features.to_numpy()
#print(response_List)

# print(features.shape)


X_train,X_test,y_train,y_test = train_test_split(features,response_List,test_size=0.8,random_state=42, stratify=response_List)


neighborsAmt = np.arange(1,min_YES_len+min_NO_len+1)
train_accuracy =np.empty(len(neighborsAmt))
test_accuracy =np.empty(len(neighborsAmt))

for i,k in enumerate(neighborsAmt):
    #Setup a knn classifier with k neighbors
    knn = KNeighborsClassifier(n_neighbors=k)
    
    #Fit the model
    # knn.fit(features, response_List)
    knn.fit(features, response_List)

    
    #Compute accuracy on the training set
    train_accuracy[i] = knn.score(features, response_List)

    #Compute accuracy on the test set
    test_accuracy[i] = knn.score(X_test, y_test) 

#Generate plot
plt.title('k-NN Varying number of neighbors')
plt.plot(neighborsAmt, test_accuracy, label='Testing Accuracy')
plt.plot(neighborsAmt, train_accuracy, label='Training accuracy')
plt.legend()
plt.xlabel('Number of neighbors')
plt.ylabel('Accuracy')

# plt.show()

# plt.show()


# y_pred = knn.predict(X_test)
# mc = confusion_matrix(y_test,y_pred)
# tb = pd.crosstab(y_test, y_pred, rownames=['True'], colnames=['Predicted'], margins=True)
# rp = classification_report(y_test,y_pred)
# # print(mc)


# knn = KNeighborsClassifier(n_neighbors=2)
# knn.fit(features,response_List)



# #Decison Tree 
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,response_List)



# dt_pred = clf.predict(X_test)
y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)

print(tree.plot_tree(clf))
plt.show()

print("--- %s seconds ---" % (time.time() - start_time))




#MLP
# mlp_clf = MLPClassifier(solver='lbfgs',alpha=1e-5, hidden_layer_sizes=(5,2),random_state=1)
# mlp_clf.fit(features,response_List)




s = 'e:/Project_Workspace/MocapSport/Court_Data/Shoulder_YES_1.xlsx'
f = 'e:/Project_Workspace/MocapSport/Court_Data/Forearm_YES_1.xlsx'
w = 'e:/Project_Workspace/MocapSport/Court_Data/Wrist_NO_2.xlsx'
# print(len(getFeature(s,f,w)))

# print("KNN prediction: ",knn.predict([getFeature(s,f,w)]))
# print(knn.score(features,response_List))
# print("DT Prediction: ", clf.predict([getFeature(s,f,w)]), " Algorithm Prob: ", clf.predict_proba([getFeature(s,f,w)]))
# print("DT Prediction: ", clf.predict([getFeature(s,f,w)]))
# print("MLP Prediction: ", mlp_clf.predict([getFeature(s,f,w)]))

