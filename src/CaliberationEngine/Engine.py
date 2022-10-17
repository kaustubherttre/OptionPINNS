import pandas as pd
import sys
import json
sys.path.insert(0, '../../src/Optimization/')
from HestonOptimization_v1 import HestonOptimization


def GetOptimizedParams(data, c):
    json_data = {}
    for i in c:
        class_data = data.loc[data['Class'] == i]
        if(len(class_data) > 100 and i not in ['C11', 'C14', 'C13', 'C21', 'C12']):
            print('>100', i)
            model = HestonOptimization(class_data.head(100))
            result = model.res
            json_data[i] = result
        print(json_data)
    return json_data

if __name__ == '__main__':
    data = pd.read_csv('../../data/ProcessedData/ClassAdded.csv')
    print(data)
    classes = data['Class'].unique()
    dictionary = GetOptimizedParams(data, classes)
    json_object = json.dumps(dictionary, indent=4)
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)
    
    


