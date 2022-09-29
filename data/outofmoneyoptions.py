import pandas as pd 


if __name__ == "__main__":
    # data = pd.read_csv("ProcessedData/PureOptionData.csv")
    # for index, row in data.iterrows():
    #     data.loc[index, "Value"] = max(row["S"] - row["K"], 0)
    #     print(index)
    # pricing_data = data[data["Value"] > 0]

    # pricing_data.to_csv("ValueAddedOptions.csv")

    #remove values from main ds of testing ds
    
    pd.read_csv("ProcessedData/ValueAddedOptions.csv").sample(10000).to_csv('Testing.csv')