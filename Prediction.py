### PHASE 2: DAILY CALL PREDICTION
## Genera la clase: Predicción() which has a method to calculate the standard deviation and the mean, another to predict with that standard deviation and mean,
##  and you can even add a method that given a day returns the following seven.

## Step 1: We will count how many calls there are from each type of client on each date in the call history.
##  We will find the mean and standard deviation for each type of client and for each day of the week.

#from datetime import date, time, datetime, timedelta
### PHASE 2: DAILY CALL PREDICTION
## Genera la clase: Predicción() which has a method to calculate the standard deviation and the mean, another to predict with that standard deviation and mean,
##  and you can even add a method that given a day returns the following seven.

## Step 1: We will count how many calls there are from each type of client on each date in the call history.
##  We will find the mean and standard deviation for each type of client and for each day of the week.


## Predicción() - OJO, normal distribution with those std gives some negative numbers for predicted calls! - some reserved slots become a negative number!


#from datetime import timedelta
import numpy as np
import pandas as pd

class Prediction: 
    """Class used to generate a prediction of the calls expected per type of patient and day of the week for a week"""
    
    def __init__(self, df):
        """class constructor"""
        self.df = df
        #self.initial_date = initial_date 
        
    def mean_std(self):
        """Calculates mean and std for the calls count in a dataset for each type of client and day of the week"""
        self.df = self.df.groupby(['Classification','Fec. Alta'], as_index=False).agg(['mean','std'])
         #df.mean()
        return self.df

    def return_week(self,df,initial_date):
        """Given a date, returns the df with a new column 'Date' containing the dates of a whole week starting on that date, 
        with each date repeated three times (one per type of client)"""
        s_dates = pd.date_range(start=initial_date, periods=len(df)/3, freq='D') 
        s_dates_repeated = s_dates.repeat(3)
        df['Date'] = s_dates_repeated 
        return df

    def predict_calls(self,df):
        """Using the mean and std of the number of call per type of client and day of week,
        generates a prediction of calls per type of client and day of the week for a week following a normal distribution"""
        #df['NumCalls (Normal dist.)'] = pd.Series(np.random.normal(df['Calls','mean'],df['Calls','std'],len(df)), index=df.index).astype(int)
        df['NumCalls (Normal dist.)'] = pd.Series(np.random.normal(df['Calls','mean'],1,len(df)), index=df.index).astype(int)
        return df
    
## Predicción() - OJO, normal distribution with those std gives some negative numbers for predicted calls! - some reserved slots become a negative number!
