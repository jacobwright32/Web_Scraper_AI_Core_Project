'''
- load in the [pima dataset](https://www.kaggle.com/uciml/pima-indians-diabetes-database)
            - don't be scared to read the docs
            - find the unique values and replace the missing ones with np.nan
            - use df.isna() or df.isnull() to count how many values are missing in 
                - the whole dataset
                - each column
            - `import msno` and visualise the missing data using `msno.matrix`
            - use `msno.heatmap` to compute the correlation between each of the features having missing data
            - drop the rows of the glucose column which are missing values. This column seems to have data missing completely at random (very small correlation between missing values here and in other columns)
            - now imagine that through domain expertise, we knew that pregnancies are not an important feature for predicting diabetes outcome, and drop the entire column (remove the entire column at once, without referencing any rows)
'''
import pandas as pd

pd.open('diabetes.csv')