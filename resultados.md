# resultados DAA


# second batch of tests - dimonesionality + more models

Here we're testing the methods to do dimensionality and feature selection 
all these are with outlier treatment, data standardization

- v1: ANOVA feature selection (100) and dimensionality reduction with PCA (5) -> NOT CONSISTENT
- v2: ANOVA feature selection (100) and dimensionality reduction with PCA (20) -> doesn't seem good but a little better, test with other values 

|model        | v1  | v2     
|----         |---- |----     
RF local      |0.360|0.340
RF kaggle     |0.249|0.297      
XGB local     |0.398|0.
XGB kaggle    |0.308|0.
SVM local     |0.328|0.
SVM kaggle    |---- |----     
LogReg local  |0.325|0.
LogReg kaggle |---- |----
lgbm local    |0.336|0.
lgbm kaggle   |---- |----




## first batch of tests - data treatment

bunch of stuff in there, basically only relevant thing to note is that the only data treatment thing worth doing is outlier treatment
and oversampling, if done right

### versions
- v1:nada
- v2:dropping non-target cols with high corr (>0.95)
- v3:dropping non-target cols with high corr (>0.92)

[looks like its better to not drop these columns]

- v4:dropping cols with low corr with target (<0.005)
- v5:dropping cols with low corr with target (<0.01)

[looks like its better to not drop these columns as well]

- v6 : treating outliers
- v7: everything
- v8: v3+v6
- v9: v6 + dropping columns with same info (corr >= 1)
- v10 : v6 + normalizing values
- v11 : v6 + oversampling minority class by 0.3 of majority class

- v12 : v11 but outlier treatment used median instaed of closest bound

v13: oversampling minority class by 0.3 of majority class

|model      | v1    | v2    | v3    | v4    | v5    | v6    | v7    | v8    | v9    | v10   | v11   | v12   | v13
|----       |----   |----   |----   |----   |----   | ----  | ----  | ----  | ----  | ----  | ----  | ----  | ----
RF local    | 0.341 | 0.352 | 0.342 | 0.337 | 0.312 | 0.344 | 0.334 | 0.332 | 0.339 | 0.343 | 0.488 | 0.335 | 0.451
RF kaggle   |----   |----   |----   |----   |----   | 0.354 |----   |----   |----   |----   | 0.383 | ----  | 0.328
XGB local   | 0.359 | 0.314 | 0.329 | 0.324 | 0.331 | 0.367 | 0.331 | 0.312 | 0.367 | 0.359 | 0.454 | 0.340 | 0.439
XGB kaggle  |----   |----   |----   |----   |----   | 0.366 |----   |----   |----   |----   | 0.332 | ----  | 0.289
Stck local  |----   |----   |----   |----   |----   | 0.346 |----   |----   |----   |----   | 0.460 | ----  | ----
Stck kaggle |----   |----   |----   |----   |----   | 0.366 |----   |----   |----   |----   | 0.245 | ----  | ----