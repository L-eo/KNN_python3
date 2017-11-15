# study KNN
# this thought from https://www.cnblogs.com/ybjourney/p/4702562.html
# 2017-11-14 08:38:50
#
# input parameter: test data, k value, training data
# output parameter: the number of the training data's order number

from distance import distance as dis
import sys 

def KNN(point, k, *classify):  # check input parameter
    if(type(point)==list and type(k)==int and type(classify[0])==list):
        1
    else:
        print("Error, invalid input parameter")
        sys.exit(-1)

    NumClass = len(classify)
    EachPointDis = []
    ClassSub = []
    for i in range(NumClass):  # calculate the distance between the test data and the training data
        for j in range(len(classify[i])):
            EachPointDis.append(dis(point, classify[i][j]))
            ClassSub.append(i)
    if(k > len(EachPointDis)):  # check input parameter
        print("Error, k must be less than size of training data.")
        sys.exit(1)

    dataSize = len(EachPointDis)  # Sort according to the increasing relation of distance
    for i in range(dataSize):
        for j in range(dataSize-1, i-1, -1):
            if(EachPointDis[j] < EachPointDis[j-1]):
                EachPointDis[j], EachPointDis[j-1] = EachPointDis[j-1], EachPointDis[j]
                ClassSub[j], ClassSub[j-1] = ClassSub[j-1], ClassSub[j]
    
    CounterClassify = []
    for i in range(NumClass):
        CounterClassify.append(0)
    for i in range(k):
        CounterClassify[ClassSub[i]] += 1
    return CounterClassify.index(max(CounterClassify)) + 1