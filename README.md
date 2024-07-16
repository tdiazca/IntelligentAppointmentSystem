# ## 'Intelligent appointment system for a health clinic'

# This training project creates a simple intelligent appointment system for a health clinic. 
# Currently, the method followed to schedule patient appointments is a manual and suboptimal process. 
# With a bit of organization, this situation will improve, and patient satisfaction will increase significantly. 
# The process consists of 4 parts: classification, prediction, optimizer, and simulator, in that order.

# ## Instructions followed 

# General explanation: The purpose of the exercise is to create a simulation of client calls to a health clinic. 
# Since we have the historical dataset of calls, we will use it to make a prediction based on this data, following a normal distribution of the number of calls we will receive each day from each client. 
# We will prioritize this prediction to reserve slots in a schedule primarily based on patient classification. 
# Once the slots are reserved, we will simulate patient calls, separate from the prediction, and add the patients to the appointment schedule based on the reserved slots from the prediction. 
# When a patient is scheduled with a penalty (beyond their deadline), a penalty of 1 will be counted. 
# If the prediction has been accurate and the daily availability is sufficient, we will have fewer penalties at the end of the month.

# ## Recommended

# Program with OOP. Program the classes:
# • Classifier() with a method clasifica() that given a dataset classifies it
# • Prediction() which has a method to calculate the standard deviation and the mean, another to predict with that standard deviation and mean, and you can even add a method that given a day returns the following seven.
# • Optimizator() This class should store the schedules of free slots and the algorithm to fill the schedule based on the Prediction() object
# • Simulator() You can create a Simulator class or simply make the simulator the main of your program, as it is the last phase.
# • Agenda recommendation: Create a data structure for the entire month, which you can easily pass from one day to another when you encounter null availability.

# Main function that runs the app is = main() function in the main module.
