##### PHASE 3: PREDICTION OPTIMIZATION
## We are optimizing a reservation system filling in reserved slots in a slot reservation agenda according to predicted calls and deadlines
## To develop the optimizer and know how well it works, we will use deadlines and/or penalties to ensure that clients receive the attention 
#### they are entitled to based on their billing.
## Penalties will come into play in PHASE 4 when we assign a client a date beyond the maximum date.

## IMP! - on phase 4 (next), each week, a new prediction and a new schedule with that weekly prediction will need to be created.
## IMP! - Optimizador() This class should store the schedules of free slots and the algorithm to fill the schedule based on the Prediction() object

# ## Step1
# # Calculate deadlines for expected calls per date and type of client 

# Add limit date column and populate it (2d for P1, 3d for P2, 4d for P3)
    # create a fx that according to value of ['Classification'] calculates date for limit date column; 
    # apply it for each val of Classification

import datetime
from datetime import timedelta
import pandas as pd

class Optimizator:
    """Clase que almacena el calendario de citas disponibles y el algoritmo que rellena el calendario
en base a la prediccion generada previamente"""

    def __init__(self, monday_week1):
        """class constructor"""
        self.monday_week1 = monday_week1

    def calculate_limit_date(self,a,b):
        """Calculates limit date for appointment according to the category of the clients of the predicted calls
       and adds limit date column to dataframe"""
        if a.item() == 'P1':
            limit_date = b.item().to_pydatetime() + timedelta(days=2)
        elif a.item() == 'P2':
            limit_date = b.item().to_pydatetime() + timedelta(days=3)
        elif a.item() == 'P3':
            limit_date = b.item().to_pydatetime() + timedelta(days=4)
        return limit_date

    def empty_agenda_generator(self):
        """Generates the empty agenda for a month"""
        start = datetime.datetime.strptime(self.monday_week1,'%Y-%m-%d')
        end = start + timedelta(days=30)
        month_dates = pd.date_range(start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'), freq='D')
        month_dates_list = []
        for date in month_dates.strftime('%Y-%m-%d'):
            month_dates_list.append(date)
        values = [{'P1':0,'P2':0,'P3':0} for n in range(30)]   
        # values = [{'P1':0,'P2':0,'P3':0}] * 30 NO! esto hace que el dict tome los valores como el mismo para todas las llaves. Si cambias uno los actualiza todos.
        agenda = {k: v for (k, v) in zip(month_dates_list, values)}
        return agenda 
    
    def avail_slots_dict(self):
        """"Generates a dictionary of available slots for a month with dates as keys and available slots as values"""
        start = datetime.datetime.strptime(self.monday_week1,'%Y-%m-%d')
        end = start + timedelta(days=30)
        month_dates = pd.date_range(start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'), freq='D')
        avail_slots={}
        value = 30
        for date in month_dates.strftime('%Y-%m-%d'):
            avail_slots[date] = value    
        return avail_slots

        ## IMPORTANTE !!!! el mismo reserved slot filler debe coger las predicciones de 4 semanas
            ## debemos hacer predicciones para 4 semanas

    def reserved_slots_filler(self,a, b, c, reserved_slots_dict, avail_slots):
        """Fills in the agenda with allocated slots per patient type and updates the available slots"""
        appointment_date = a.item().strftime('%Y-%m-%d')
        if appointment_date in reserved_slots_dict.keys():
            if avail_slots[appointment_date] > 0:
                if b.item() == 'P1':
                    ### if avail_slots[appointment_date] >= c.item():
                    reserved_slots_dict[appointment_date]['P1'] += c.item() #reserved_slots_empty[df['Date']]['P1'] + 1
                    avail_slots[appointment_date] -= c.item()
                elif b.item() == 'P2':
                    reserved_slots_dict[appointment_date]['P2'] = reserved_slots_dict[appointment_date]['P2'] + c.item()
                    avail_slots[appointment_date] -= c.item()
                elif b.item() == 'P3':
                    reserved_slots_dict[appointment_date]['P3'] = reserved_slots_dict[appointment_date]['P3'] + c.item()
                    avail_slots[appointment_date] -= c.item()                
            else:
                print('No slots available for that date, we will try the next available date')
                input("press any key to close")
        else:
            print('We cannot schedule your apponitment yet, please call back in X days')
       
##########



