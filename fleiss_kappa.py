"""
Ref.
1. https://github.com/Shamya/FleissKappa
2. https://blog.csdn.net/qq_31113079/article/details/76216611
3. https://notebook.community/amirziai/learning/statistics/Inter-rater%20agreement%20kappas
"""

import pandas as pd
import numpy as np
def checkInput(rate, n):
    """ 
    Check correctness of the input matrix
    @param rate - ratings matrix
    @return n - number of raters
    @throws AssertionError 
    """
    N = len(rate)
    k = len(rate[0])
    assert all(len(rate[i]) == k for i in range(k)), "Row length != #categories)"
    assert all(isinstance(rate[i][j], int) for i in range(N) for j in range(k)), "Element not integer" 
    assert all(sum(row) == n for row in rate), "Sum of ratings != #raters)"

def fleissKappa(rate,n):
    """ 
    Computes the Kappa value
    @param rate - ratings matrix containing number of ratings for each subject per category 
    [size - N X k where N = #subjects and k = #categories]
    @param n - number of raters   
    @return fleiss' kappa
    """

    N = len(rate)
    k = len(rate[0])
    print("#raters = ", n, ", #subjects = ", N, ", #categories = ", k)
    checkInput(rate, n)

    #mean of the extent to which raters agree for the ith subject 
    PA = sum([(sum([i**2 for i in row])- n) / (n * (n - 1)) for row in rate])/N
    print("PA = ", PA)
    
    # mean of squares of proportion of all assignments which were to jth category
    PE = sum([j**2 for j in [sum([rows[i] for rows in rate])/(N*n) for i in range(k)]])
    print("PE =", PE)
    
    kappa = -float("inf")
    try:
        kappa = (PA - PE) / (1 - PE)
        kappa = float("{:.3f}".format(kappa))
    except ZeroDivisionError:
        print("Expected agreement = 1")

    print("Fleiss' Kappa =", kappa)
    
    return kappa


def create_labeler_set(path):
    """
    (N, n, k) = (Sample, labeler, grading)
    
    """
    sample_list_arr=[]
    labeler = ['A','B','C','D','E']
    df = pd.read_csv(path,encoding = 'UTF-8')
    for i in range(len(df['Order'])):
        label_count=[0,0,0,0]
        print(i)
        for j in range(len(labeler)):
            #print(i,j)
            print('labeler:',labeler[j], df[labeler[j]][i])
            if df[labeler[j]][i]==1:
                label_count[0]=label_count[0]+1
            elif df[labeler[j]][i]==2:
                label_count[1]=label_count[1]+1
            elif df[labeler[j]][i]==3:
                label_count[2]=label_count[2]+1
            elif df[labeler[j]][i]==4:
                label_count[3]=label_count[3]+1
            else:
                print('error')
        sample_list_arr.append(label_count)
        print(label_count)
    print(sample_list_arr)
    print(len(sample_list_arr))
    return sample_list_arr


if __name__ == "__main__":
    path_csv = r'label_2022_0827.csv'
    sample_list_arr = create_labeler_set(path_csv)
    kappa = fleissKappa(sample_list_arr,5)
    assert(kappa)
