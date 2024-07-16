### PHASE 1: Clasificacion() with a method clasifica() that given a dataset classifies it
# Create the class Clasificacion() with a method clasifica() that given a dataset classifies it

import numpy as np

class Classifier:
    """Dado un dataframe, incluye columna Classification donde se clasifican los registros segun condiciones dadas"""
    
    def __init__(self, df, conditions, values):
        """class constructor"""
        self.df = df
        self.conditions = conditions
        self.values = values
        
    def clasificacion(self):
        """ method that classifies dataframe registries (entries) according to some given conditions"""
        self.df['Classification'] = np.select(self.conditions,self.values)  
        return self.df


