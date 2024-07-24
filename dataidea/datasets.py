import os
import numpy as np
import pandas as pd

def loadDataset(name:str=None, inbuilt=True, file_type:str=None):
    '''
    Easily load datasets that are inbuit in DATAIDEA

    parameters:
    name: this is the name of the dataset, eg demo, fpl, music, titanic etc
    inbuilt: boolean to specify whether data is from DATAIDEA or custom data
    type: specifies the type of the dataset eg 'csv', 'excel' etc

    '''

    if inbuilt:
        package_dir = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(package_dir, 'datasets', f'{name}.csv')
        return pd.read_csv(data_path)

    if file_type == None:
        raise TypeError('The file type was not specified')
    
    if file_type == 'csv':
        return pd.read_csv(name)
    
    if file_type == 'excel':
        return pd.read_excel(name)


def subsetData(data:pd.DataFrame=None, columns:list=[]):
    '''
    Pick only the selected columns from the dataset
    '''
    subsetted_data = data[columns].copy()
    return subsetted_data
