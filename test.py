class1 = [[-15,12], [-15,3], [-15, -1], [-5,0], [-10,3], [2,10]]  # first class of the training data
class2 = [[-3,13], [6,15], [15,12], [5,1], [1,-1]]  # second class of the training data
point = [0,0]  # test data
k = 3

from KNN import KNN
from distance import distance as dis

print(KNN(point, k, class1, class2))
# print(dis(point, [1,2,3]))