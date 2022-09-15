# kappa
- 評分者間信度(Inter-rater reliability): 不同一個人在**乙個**實例中給出的評分一致性得分
- 評估者內信度(Intra-rater reliability): 相同一個人在**多個**實例中給出的評分一致性得分
- 統計方式: Cohen's kappa, Fleiss' kappa

## § Abstract
Kappa has two type: one is Cohen's kappa, another is Fleiss's kappa.
- Cohen's kappa: 適用於兩名評估者。
- Fleiss' kappa: 適用於任何固定數量的評估者。


## § Interpretation of Kappa

| Kappa | Agreement |
|:---:| :---: |
|<0 | Less than chance |
| 0.01 ~ 0.20 | Slight |
| 0.21 ~ 0.40 | Fair |
| 0.41 ~ 0.60 | Moderate |
| 0.61 ~ 0.80 | Substantial |
| 0.81 ~ 0.99 | Almost |

![image](https://user-images.githubusercontent.com/32260565/190395367-1153b7a4-b678-4d5f-ae73-5ee1d70f8de8.png)


## § Kappa type
### Cohen Kappa


### Flessis's kappa

## § Implement detail
Env.:
1. skleran 1.1.2: 


## § Ref.
- https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html
- https://github.com/Shamya/FleissKappa
- https://blog.csdn.net/qq_31113079/article/details/76216611
- https://notebook.community/amirziai/learning/statistics/Inter-rater%20agreement%20kappas
- https://www.twblogs.net/a/5b7cf6d22b71770a43dd5451
