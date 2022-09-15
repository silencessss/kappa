"""
Ref.
https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html

sklearn.metrics.cohen_kappa_score(y1, y2, *, labels=None, weights=None, sample_weight=None)
Args:
    y1, 由第一個註釋者分配的標籤
    y2, 由第二個註釋者分配的標籤
    labels, default=None , 索引矩陣的標籤列表。這可用於選擇標籤的子集。如果，則使用或中None至少出現一次的所有標籤
    weights{‘linear’, ‘quadratic’}, default=None, 加權類型來計算分數。None表示沒有加權；“線性”是指線性加權；“二次”是指二次加權。
    sample_weight, default=None, 樣本權重

"""
import pandas as pd
from sklearn.metrics import cohen_kappa_score
import numpy as np
import itertools
import seaborn as sns
import matplotlib.pyplot as plt
rater_num = 5
def count_cohen_kappa(y1,y2):
    kappa_value = cohen_kappa_score(
        y1,
        y2,
        labels = None,
        weights = None,
        sample_weight = None
    )
    return kappa_value
def create_labeler_set(path):
    df = pd.read_csv(path,encoding = 'UTF-8')
    labeler_a = []
    labeler_b = []
    for i in range(len(df['Order'])):
        labeler_a.append(df['A'][i])
        labeler_b.append(df['B'][i])
    return labeler_a, labeler_b

def Calculate_Cohen_Kappa_more_raters(raters):
    data = np.zeros((len(raters), len(raters)))
    for j, k in list(itertools.combinations(range(len(raters)), r=2)):
        data[j, k] = cohen_kappa_score(raters[j], raters[k])
    fig, ax = plt.subplots(figsize=(10,8)) 
    sns.heatmap(
        data, 
        mask=np.tri(len(raters)),
        annot=True, 
        linewidths=0.5,
        vmin=0, 
        vmax=1,
        xticklabels=[f"Dermatologist {k + 1}" for k in range(len(raters))],
        yticklabels=[f"Dermatologist {k + 1}" for k in range(len(raters))],
        cmap="YlGnBu",
        ax=ax
    )
    plt.xticks(rotation=30) 
    plt.yticks(rotation=30)
    plt.savefig('result.png')
    plt.show()
    

def create_raters_set(path):
    df = pd.read_csv(path,encoding = 'UTF-8')
    rater_A, rater_B, rater_C, rater_D, rater_E = [],[],[],[],[]
    for i in range(len(df['Order'])):
        rater_A.append(df['A'][i])
        rater_B.append(df['B'][i])
        rater_C.append(df['C'][i])
        rater_D.append(df['D'][i])
        rater_E.append(df['E'][i])
    raters_table = [rater_A, rater_B, rater_C, rater_D, rater_E]
    return raters_table  

if __name__=='__main__':
    path_csv = r'annoaction_2022_0827.csv'
    labeler_a, labeler_b = create_labeler_set(path_csv)
    raters_table = create_raters_set(path_csv)
    print(labeler_a)
    print()
    print(labeler_b)
    kappa_result = count_cohen_kappa(labeler_a,labeler_b)
    print(kappa_result)
    print()
    #print(raters_table)
    Calculate_Cohen_Kappa_more_raters(raters_table)

