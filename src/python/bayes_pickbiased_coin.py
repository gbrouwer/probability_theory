#import
import os
import sys
import numpy as np 

#------------------------------------------------------------------
if __name__ == '__main__':

    #Parameters
    nCoins = 100
    nBiased = 1
    bias = 1.0
    fair = 0.5
    nTosses = 10

    #Probability of a biased/fair coin
    probBiasedCoin = nBiased / nCoins
    probFairCoint = 1.0  - probBiasedCoin
    print(probBiasedCoin)
    print(probFairCoint)

    #Number of expected heads for a biased/fair coin
    nHeadBiased = bias ** nTosses
    nHeadFair = fair ** nTosses
    print(nHeadBiased)
    print(nHeadFair)

    #Probability of getting the unfair coin
    probGettingFairCoin = probFairCoint * nHeadFair
    probBiasedCoin = probBiasedCoin * nHeadBiased
    probBiasedCoin = probBiasedCoin / (probGettingFairCoin + probBiasedCoin)
    print(probBiasedCoin)