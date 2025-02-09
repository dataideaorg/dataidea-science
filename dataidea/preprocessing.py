import pandas as pd


def getLowerAndUpperBounds(data:pd.DataFrame=None, column:pd.core.series.Series|str=None):
    '''
    Returns the upper and lower bounds of a continuous numeric variable
    '''
    if data:
        # Calculate Q1, Q3, and IQR
        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)
    else:
        # Calculate Q1, Q3, and IQR
        Q1 = column.quantile(0.25)
        Q3 = column.quantile(0.75)

    IQR = Q3 - Q1
    # Calculate outlier bounds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    return lower_bound, upper_bound
        

def getColumnsWithMissingData(data:pd.DataFrame=None, return_list:bool=False):
    '''
    Returns columns with missing data in the a provided Pandas DataFrame
    '''
    # columns with missing values
    missing_values = data.isna().sum()
    columns_with_missing_values = missing_values[missing_values > 0]

    # where missing values are greater than 0
    if return_list:
        return columns_with_missing_values.index.tolist()
    
    return columns_with_missing_values
