# DAA

*Insert Description Here*

## Instructions
As the code is split into two notebooks, to run the program, 2 steps need to be followed:
- Run the project.ipynb file, where the data treatment is executed. This should generate a train_data.csv file and a test_data.csv file, under the data directory. For the current version, these files are already generated and can be found in the data directory.
- Run the models.ipynb file, where the models are trained and tested. This should generate a test_predictions_modelname.csv file (where modelname is the chosen model) under the results directory. Most models are commented, however, users are free to uncomment them and test them. 

## General Info
There are a couple more files worth explaining:
- results.xlsx: This file contains the results of the models that were tested. Since this project was developed for a kaggle competition, where we had only 3 submissions per day, it was essential for us to keep track of the results of each model. This file contains the results of the models that were tested, as well as the hyperparameters that were used and a detailed description of the data treatment steps applied. When developing the project, one of the main goals was to get a consistent score locally and on the kaggle competition, to guarantee that the model was not overfitting the training data. Although the model, unfortunately, ended up overfitting, this might help explaining the steps that were taken and the results that were obtained.
- project_statement.pdf: This file was given by the professors and contains the instructions for the project.
- project_report.pdf: This file contains a detailed explanation of the steps that were taken, the models that were tested, the results that were obtained and the conclusions that were drawn. It also contains a detailed explanation of the data treatment steps that were applied.