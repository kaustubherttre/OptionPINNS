from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_optionValue(data):

    data_43 = data[data["DaysToExpire"]].sort_values(by=["Last"], ascending=True)

    plt.plot(data_43["Error_of_BS"], data["DaysToExpire"] , color = "black", label = "line1")
    #plt.plot(data_43["Mid"], color = "yellow", label = "line2")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    csv_set = pd.read_csv('../data/ProcessedData/ProcessedData.csv')
    data = csv_set.sort_values(by=['DaysToExpire'], ascending=True)
    print(data.info)
    plot_optionValue(data)
    