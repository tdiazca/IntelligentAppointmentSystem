### PHASE 1: Classifier() with a method clasificacion() that given a dataset classifies it
# Create the class Classifier() with a method clasificacion() that given a dataset classifies it

import numpy as np

class Classifier:
    """Dado un dataframe, incluye columna Classification donde se clasifican los registros segun condiciones dadas"""
    
    values = ['P1','P2','P3'] # class attribute
    
    def __init__(self, df, conditions):
        """class constructor"""
        
        #self.values = values  # instance variable
        self.df = df
        self.conditions = conditions

        
    def clasificacion(self):
        """ method that classifies dataframe registries (entries) according to some given conditions"""
        
        self.df['Classification'] = np.select(self.conditions, Classifier.values)  
        return self.df


