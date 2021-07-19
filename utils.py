import numpy as np 
import joblib 


def preprocessdata(open_,high,low,volume):
    test_data = [[open_,high,low,volume] ]
    trained_model = joblib.load("model.pkl") 
    prediction = trained_model.predict(test_data) 

    return prediction 
