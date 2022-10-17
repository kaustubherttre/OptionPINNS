import pandas as pd
import sys
import json
sys.path.insert(0, '../../src/Optimization/')
from HestonOptimization_v1 import HestonOptimization


def GetOptimizedParams(data, c):
    json_data = {}
    for i in c:
        class_data = data.loc[data['Class'] == i]
        if(len(class_data) < 100):
            print('<100', i)
            model = HestonOptimization(data)
            result = model.res
            json_data[i] = result
        elif(len(class_data) > 100):
            print('>100', i)
            model = HestonOptimization(data.head(100))
            result = model.res
            json_data[i] = result
    return json_data



        
        
        

if __name__ == '__main__':
    data = pd.read_csv('../../data/ProcessedData/ClassAdded.csv').head(101)
    print(data)
    classes = data['Class'].unique()
    print(len(data.loc[data['Class'] == 'C11']))
    print(GetOptimizedParams(data, classes))
    
    


