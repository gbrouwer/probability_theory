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

    #Parameters
    pA = 0.002 #prevelance
    pBA = 0.85 #probability of a postive if the disease is present
    pB = 0.8 #probability of of a positive, regardless of distease presence

    #Run Bayes and
    pAB = bayes(pA,pB,pBA)
    print('Probability of disease given a positive test: ' + str(pAB))

    