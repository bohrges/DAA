# resultados DAA

- dropping non-target cols with high corr
- dropping columns with low corr with target
- treating outliers

## versions
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
- v11 : v6 + oversampling all classes but the majority one

(I also tested just oversampling the minority class, same result. Seems like oversampling does nothing)

- v12 : v11 but outlier treatment used median instaed of closest bound


|model      | v1    | v2    | v3    | v4    | v5    | v6    | v7    | v8    | v9    | v10   | v11   | v12
|----       |----   |----   |----   |----   |----   | ----  | ----  | ----  | ----  | ----  | ----  | ----
RF local    | 0.341 | 0.352 | 0.342 | 0.337 | 0.312 | 0.344 | 0.334 | 0.332 | 0.339 | 0.343 | 0.344 | 0.335
RF kaggle   |----   |----   |----   |----   |----   | 0.354 |----   |----   |----   |----   | ----  | ----
XGB local   | 0.359 | 0.314 | 0.329 | 0.324 | 0.331 | 0.367 | 0.331 | 0.312 | 0.367 | 0.359 | 0.367 | 0.340
XGB kaggle  |----   |----   |----   |----   |----   | 0.366 |----   |----   |----   |----   | ----- | ----
