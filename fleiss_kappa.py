#https://github.com/Shamya/FleissKappa

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

if __name__ == "__main__":
    
    print("Example run to calculate Fleiss' Kappa")
    
    print("\nTest case 1 - Fleiss 1971")
    #Fleiss, 1971 example

    '''
    rate = \
    [
        [0,0,0,6,0],
        [0,3,0,0,3],
        [0,1,4,0,1],
        [0,0,0,0,6],
        [0,3,0,3,0],
        [2,0,4,0,0],
        [0,0,4,0,2],
        [2,0,3,1,0],
        [2,0,0,4,0],
        [0,0,0,0,6],
        [1,0,0,5,0],
        [1,1,0,4,0],
        [0,3,3,0,0],
        [1,0,0,5,0],
        [0,2,0,3,1],
        [0,0,5,0,1],
        [3,0,0,1,2],
        [5,1,0,0,0],
        [0,2,0,4,0],
        [1,0,2,0,3],
        [0,0,0,0,6],
        [0,1,0,5,0],
        [0,2,0,1,3],
        [2,0,0,4,0],
        [1,0,0,4,1],
        [0,5,0,1,0],
        [4,0,0,0,2],
        [0,2,0,4,0],
        [1,0,5,0,0],
        [0,0,0,0,6]
    ]
    kappa = fleissKappa(rate,6)
    assert(kappa==0.43)
    '''

    rate = \
        [
            [0, 1,  4,  0],
            [3,	1,	1,	0],
            [0,	0,	2,	3],
            [0,	2,	3,	0],
            [0,	5,	0,	0],
            [2,	2,	1,	0],
            [2,	1,	2,	0],
            [1,	3,	1,	0],
            [5,	0,	0,	0],
            [1,	3,	1,	0],
            [0,	2,	3,	0],
            [2,	2,	1,	0],
            [1,	2,	2,	0],
            [0,	2,	3,	0],
            [0,	3,	2,	0],
            [0,	1,	4,	0],
            [0,	1,	4,	0],
            [2,	2,	1,	0],
            [2,	3,	0,	0],
            [0,	0,	5,	0]

        ]
    kappa = fleissKappa(rate,5)
    assert(kappa)
