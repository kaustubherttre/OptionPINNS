import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier  
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix


    


if __name__ == '__main__':
    data = pd.read_csv('../../data/ProcessedData/ClassAdded.csv')
    print(data.tail())
    test = pd.read_csv('../../data/ProcessedData/Testing_Enigne.csv')
    X_test = test[['Moneyness','Days']].values
    print(X_test)
    X = data[['Moneyness','Days']].values
    y = data[['Class']].values
    print(y)
    x_train, x_test, y_train, y_test= train_test_split(X, y, test_size= 0.25, random_state=0)
    st_x= StandardScaler()    
    x_train= st_x.fit_transform(x_train)    
    x_test= st_x.transform(x_test)
    classifier= RandomForestClassifier(n_estimators= 24, criterion="entropy")  
    classifier.fit(x_train, y_train)
    y_pred= classifier.predict(X_test)
    print(y_pred)