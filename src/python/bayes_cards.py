#import
import os
import sys
import numpy as np 

#------------------------------------------------------------------
def bayes(pA,pB,pBA):

    pAB = (pBA * pA) / pB
    return pAB

#------------------------------------------------------------------
if __name__ == '__main__':

    #What is the probability of a facecard, given its a king

    #Parameters
    pA = 12.0/52.0 #Probability of a facecard
    pBA = 1.0/3.0 #Probability of a king, given its a facecard
    pB = 4.0/52.0 #Probability of a king

    #Run Bayes and
    pAB = bayes(pA,pB,pBA)
    print('Probability of a facecard given its a king test: ' + str(pAB))

    