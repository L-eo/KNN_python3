# solve two point's distance

import math
import sys 

def distance(p1, p2):
    Dis = 0
    if(len(p1) == len(p2)):
        for i in range(len(p1)):
            Dis += (p1[i]-p2[i]) * (p1[i]-p2[i])
        return math.sqrt(Dis)
    else:
        print("Error, the two point's dimension are not agreement!")
        sys.exit(1)