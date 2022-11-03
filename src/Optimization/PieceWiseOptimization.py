import pandas as pd
import numpy as np
from math import log

class PieceWiseOptimization:
    def __init__(self, data):
        self.data = data
        def getLogReturns(data):
            for index, row in data.iterrows():
                index = index + 1
                if(index < len(data)):
                    prev = data._get_value(index -1, "S")
                    curr = data._get_value(index, "S")
                    data.loc[index, "Return"] = log(curr/prev)*100
            return data
                
        self.ret = getLogReturns(self.data)
                


if __name__ == "__main__":
    classdata = pd.read_csv('../../data/ProcessedData/ClassAdded.csv')
    data = classdata.loc[classdata['Class'] == 'C11'].sample(200).reset_index()
    print(data[['S']])
    model = PieceWiseOptimization(data)
    # print(data[['S']])
    
    print(model.ret[['S', 'Return']])
    

