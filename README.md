![](https://img.shields.io/badge/scikit--learn-1.1.2-orange)
![](https://img.shields.io/badge/seaborn-0.11.2-9cf)
# kappa
A statistic that is used to measure inter-rater reliability (and also intra-rater reliability) for qualitative (categorical) items.
- 評分者間信度(Inter-rater reliability): 不同一個人在**乙個**實例中給出的評分一致性得分
- 評估者內信度(Intra-rater reliability): 相同一個人在**多個**實例中給出的評分一致性得分
- 統計方式: Cohen's kappa, Fleiss' kappa

## § Abstract
Kappa has two type: one is Cohen's kappa, another is Fleiss's kappa.
- Cohen's kappa: 適用於兩名評估者。
- Fleiss' kappa: 適用於任何固定數量的評估者。


## § Interpretation of Kappa

| Kappa | Agreement | 一致性 |
|:---:| :---: | :---: |
|<0 | Less than chance | 幾乎沒有一致性 |
| 0.01 ~ 0.20 | Slight | 極低的一致性
| 0.21 ~ 0.40 | Fair   | 一般的一致性|
| 0.41 ~ 0.60 | Moderate | 中等的一致性|
| 0.61 ~ 0.80 | Substantial | 高度的一致性|
| 0.81 ~ 0.99 | Almost | 幾乎完全一致性|

![image](https://user-images.githubusercontent.com/32260565/190395367-1153b7a4-b678-4d5f-ae73-5ee1d70f8de8.png)


## § Kappa type
### Cohen Kappa
This function computes Cohen’s kappa. It's defined as $k = (p_o-p_e)/(1-p_e)$ where $p_o$ is the empirical probability of agreement on the label assigned to any samples (the observed agreement ratio), and $p_e$ is the expected agreement when both annotators assign labels randomly. Furthermore, $p_e$ is estimated using a per-annotator empirical prior over the class labels.
> 該函數計算 Cohen 的 kappa。 它被定義為 $k = (p_o-p_e)/(1-p_e)$ 其中 $p_o$ 是分配給任何樣本的標籤的經驗一致性概率（觀察到的一致性比率）， $p_e$ 是預期一致性 當兩個註釋者隨機分配標籤時。 此外 $p_e$ 是使用每個註釋者在類標籤上的經驗先驗估計的。


### Fleiss's kappa
Fleiss' kappa (named after Joseph L. Fleiss) is a statistical measure for assessing the reliability of agreement between a fixed number of raters when assigning categorical ratings to a number of items or classifying items.


## § Ref.
- Cohen, Jacob. “A Coefficient of Agreement for Nominal Scales.” Educational and Psychological Measurement 20 (1960): 37 - 46.
- Fleiss, J. L. (1971) "Measuring nominal scale agreement among many raters." Psychological Bulletin, Vol. 76, No. 5 pp. 378–382.
- https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html
- https://github.com/Shamya/FleissKappa
- https://blog.csdn.net/qq_31113079/article/details/76216611
- https://notebook.community/amirziai/learning/statistics/Inter-rater%20agreement%20kappas
- https://www.twblogs.net/a/5b7cf6d22b71770a43dd5451
- https://stackoverflow.com/questions/11528150/inter-rater-agreement-in-python-cohens-kappa/41028077#41028077
- https://www.nltk.org/api/nltk.metrics.agreement.html
