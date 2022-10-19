import pandas as pd
import numpy as np

def classification(data):
    for index, row in data.iterrows():
        m = row['Moneyness']
        t = row['Days']
        print(index)

        if(t > 0.0 and t < 25.0):
            f_c = "C1"
            if(m < 1.1):
                f_c = f_c + '1'
            elif(m > 1.1 and m <= 1.2):
                f_c = f_c + '2'
            elif(m > 1.2 and m <= 1.3):
                f_c = f_c + '3'
            elif(m > 1.3):
                f_c = f_c + '4'
            else:
                f_c = f_c + ' Unclassified'
        elif(t > 25 and t< 60):
            f_c = "C2"
            if(m < 1.1):
                f_c =f_c + '1'
            elif(m > 1.1 and m <= 1.2):
                f_c =f_c + '2'
            elif(m > 1.2 and m <= 1.3):
                f_c =f_c + '3'
            elif(m > 1.3):
                f_c =f_c + '4'
            else:
                f_c =f_c + ' Unclassified'
        elif(t > 60 and t < 88):
            f_c = "C3"
            if(m < 1.1):
                f_c = f_c + '1'
            elif(m > 1.1 and m <= 1.2):
                f_c = f_c + '2'
            elif(m > 1.2 and m <= 1.3):
                f_c = f_c + '3'
            elif(m > 1.3):
                f_c = f_c + '4'
            else:
                f_c = f_c + ' Unclassified'
        elif(t > 88 and t < 116):
            f_c = "C4"
            if(m < 1.1):
                f_c = f_c + '1'
            elif(m > 1.1 and m <= 1.2):
                f_c = f_c + '2'
            elif(m > 1.2 and m <= 1.3):
                f_c = f_c + '3'
            elif(m > 1.3):
                f_c = f_c + '4'
            else:
                f_c = f_c + ' Unclassified'
        elif( t > 116 and t<144):
            f_c = "C5"
            if(m < 1.1):
                f_c = f_c + '1'
            elif(m > 1.1 and m <= 1.2):
                f_c = f_c + '2'
            elif(m > 1.2 and m <= 1.3):
                f_c = f_c + '3'
            elif(m > 1.3):
                f_c = f_c + '4'
            else:
                f_c = f_c + ' Unclassified'
        elif(t > 400 and t < 476):
            f_c = "C6"
            if(m < 1.1):
                f_c = f_c + '1'
            elif(m > 1.1 and m <= 1.2):
                f_c = f_c + '2'
            elif(m > 1.2 and m <= 1.3):
                f_c = f_c + '3'
            elif(m > 1.3):
                f_c = f_c + '4'
            else:
                f_c = f_c + ' Unclassified'
        elif(t > 800 and t < 839):
            f_c = "C7"
            if(m < 1.1):
                f_c = f_c + '1'
            elif(m > 1.1 and m <= 1.2):
                f_c = f_c + '2'
            elif(m > 1.2 and m <= 1.3):
                f_c = f_c + '3'
            elif(m > 1.3):
                f_c = f_c + '4'
            else:
                f_c = f_c + ' Unclassified'
        data.loc[index, 'Class'] = f_c
    return data
if __name__ == '__main__':
    df = pd.read_csv("../../data/ProcessedData/Testing_Enigne.csv")
    classification(df).to_csv('ClassAdded_test.csv')