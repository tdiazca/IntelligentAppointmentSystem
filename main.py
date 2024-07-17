
#### 'Intelligent appointment system for a health clinic'

import datetime
from datetime import timedelta

#from operator import call
import pandas as pd
import numpy as np
import Classifier as cf
import Prediction as pdt
import Optimizator as opt

#####################   MAIN FUNCTION

def main():
    """ This function allows the user to choose a date (must be a Monday) being the firt Monday 
    of the month that they want to generate a simulated appointment shcedule for."""
    
    #datasetpath = input("Please, enter path to training dataset 'historico_llamadas.xlsx': ") # C:\Users\teresa.diaz.calvo\source\repos\trainingpython\Data_ejercicio_final_python_training\historico_llamadas.xlsx
    datasetpath = r'C:\Users\teresa.diaz.calvo\source\repos\trainingpython\IntelligentAppointmentSystem\historico_llamadas.xlsx'
    
    #df = pd.read_csv(contrato_factura_datasetpath, sep=';', decimal='.')
    df = pd.read_excel(datasetpath, sheet_name='Sheet1', decimal='.')

    conditions = [
        (df['Facturación'] > float(4000)), #Facturación
        ((df['Facturación'] >= float(3000)) & (df['Facturación'] < float(4000))),
        (df['Facturación'] < float(3000))
        ]

    values = ['P1','P2','P3']

    my_classification = cf.Classifier(df, conditions, values)
    df = my_classification.clasificacion()

    # print("These is the patient classification for our current dataset: ")
    # print(df)
    # input("press key to continue")

    df['Fec. Alta'] = df['Fec. Alta'].apply(lambda x: x.strftime('%A'))
    df = df.groupby(['Classification','Fec. Alta','Contrato'], as_index=False).count()

    del df['Contrato']

    # # # df1['Fec. Alta'] = df1['Fec. Alta'].apply(lambda x: x.strftime('%A'))
    # # #     #apply() will take each cell at a time for evaluation and apply the formatting as specified in the lambda function.
    # # #         ## otra forma:
    # # #         #df1['Fec. Alta'] = df1['Fec. Alta'].dt.strftime('%A')
    # # #         #we  convert dates back to strings with df1['Fec. Alta'].dt.strftime('%Y-%m-%d') o el formato que queramos  


    ######

    ### PHASE 2: DAILY CALL PREDICTION
    ## Genera la clase: Predicci�n() which has a method to calculate the standard deviation and the mean, another to predict with that standard deviation and mean,
    ##  and you can even add a method that given a day returns the following seven.

    ## Step 1: We will count how many calls there are from each type of client on each date in the call history.
    ##  We will find the mean and standard deviation for each type of client and for each day of the week.

    ###### PREDICTION  WEEK 1

    categories=['P1_Monday','P2_Monday','P3_Monday','P1_Tuesday','P2_Tuesday','P3_Tuesday','P1_Wednesday','P2_Wednesday',
                                                            'P3_Wednesday','P1_Thursday','P2_Thursday','P3_Thursday','P1_Friday','P2_Friday','P3_Friday','P1_Saturday',
                                                            'P2_Saturday','P3_Saturday','P1_Sunday','P2_Sunday','P3_Sunday']

    my_prediction1 = pdt.Prediction(df)

    df1 = my_prediction1.mean_std()
    df1 = df1.rename(columns={'Facturación':'Calls'})
    df1 = df1.rename(columns={'Fec. Alta':'Day of the week'})

    #df1 = df.sort_values(by=['Day of the week'], key=lambda s: s.apply(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'].index), ignore_index=True)

    cols = ['Classification', 'Day of the week']
    df1['Combined'] = df1[cols].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)

    df1.Combined = pd.Categorical(df1.Combined, categories)
    df1=df1.sort_values('Combined', ignore_index=True)

    ####### PREDICTION WEEK 2

    my_prediction2 = pdt.Prediction(df)
    df2 = my_prediction2.mean_std()

    df2 = df2.rename(columns={'Facturación':'Calls'})
    df2 = df2.rename(columns={'Fec. Alta':'Day of the week'})

    cols = ['Classification', 'Day of the week']
    df2['Combined'] = df2[cols].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)

    df2.Combined = pd.Categorical(df2.Combined, categories)
    df2=df2.sort_values('Combined', ignore_index=True)

    ######## PREDICTION WEEK 3

    my_prediction3 = pdt.Prediction(df)
    df3 = my_prediction3.mean_std()

    df3 = df3.rename(columns={'Facturación':'Calls'})
    df3 = df3.rename(columns={'Fec. Alta':'Day of the week'})

    cols = ['Classification', 'Day of the week']
    df3['Combined'] = df3[cols].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)

    df3.Combined = pd.Categorical(df3.Combined, categories)
    df3=df3.sort_values('Combined', ignore_index=True)

    ######### PREDICTION WEEK 4

    my_prediction4 = pdt.Prediction(df)
    df4 = my_prediction4.mean_std()

    df4 = df4.rename(columns={'Facturación':'Calls'})
    df4 = df4.rename(columns={'Fec. Alta':'Day of the week'})

    cols = ['Classification', 'Day of the week']
    df4['Combined'] = df4[cols].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)

    df4.Combined = pd.Categorical(df4.Combined, categories)
    df4=df4.sort_values('Combined', ignore_index=True)


    #########

    try:
    
        monday_week1 = input("Please, enter a date for which the Prediction should be created. This must must correspond to a Monday and have the following format YYYY-MM-DD: ")
        assert(datetime.datetime.strptime(monday_week1, '%Y-%m-%d').strftime('%A') == 'Monday')
    
        monday_week2_date = datetime.datetime.strptime(monday_week1, '%Y-%m-%d') + timedelta(days=7)
        monday_week2 = datetime.datetime.strftime(monday_week2_date, '%Y-%m-%d')

        monday_week3_date = monday_week2_date + timedelta(days=7)
        monday_week3 = datetime.datetime.strftime(monday_week3_date, '%Y-%m-%d')

        monday_week4_date = monday_week3_date + timedelta(days=7)
        monday_week4 = datetime.datetime.strftime(monday_week4_date, '%Y-%m-%d')

        ##

        print("Dataframe for week 1 before returning week")
        print(df1)
        input("press key to continue")

        df1 = my_prediction1.return_week(df1,monday_week1) #df = my_prediction.return_week(df,datetime.datetime.today().strftime('%Y-%m-%d')) #'%d-%m-%Y'  #df = my_prediction.return_week(df,'2024/06/3')
        print("Dataframe for week 1 with dates")
        print(df1)
        input("press any key to continue")

        df2 = my_prediction2.return_week(df2,monday_week2)
        df3 = my_prediction3.return_week(df3,monday_week3)
        df4 = my_prediction4.return_week(df4,monday_week4)

        df1['Day of date'] = df1['Date'].apply(lambda x: x.strftime('%A'))
        df2['Day of date'] = df2['Date'].apply(lambda x: x.strftime('%A'))
        df3['Day of date'] = df3['Date'].apply(lambda x: x.strftime('%A'))
        df4['Day of date'] = df4['Date'].apply(lambda x: x.strftime('%A'))

        # ## Step 2: With that mean and standard deviation, we will generate a random number following a normal distribution to predict how many calls there will be
        # ##  per day and per type of patient in the next 7 days.

        df1 = my_prediction1.predict_calls(df1)
        del df1['Combined']
        del df1['Calls','mean']
        del df1['Calls','std']
        del df1['Day of date']

        print("These are the predicted calls for week 1")
        print(df1)
        input("press any key to continue")

        df2 = my_prediction2.predict_calls(df2)
        del df2['Combined']
        del df2['Calls','mean']
        del df2['Calls','std']
        del df2['Day of date']

        df3 = my_prediction3.predict_calls(df3)
        del df3['Combined']
        del df3['Calls','mean']
        del df3['Calls','std']
        del df3['Day of date']

        df4 = my_prediction4.predict_calls(df4)
        del df4['Combined']
        del df4['Calls','mean']
        del df4['Calls','std']
        del df4['Day of date']

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

        ##

        my_optimizator = opt.Optimizator(monday_week1)          

        df1['limit date'] = [my_optimizator.calculate_limit_date(df1.loc[idx, 'Classification'], df1.loc[idx, 'Date']) for idx in range(len(df1))]
        print("These are the predicted calls for week 1 with limit dates for appointments.")
        print(df1)
        input("press any key to continue")

        df2['limit date'] = [my_optimizator.calculate_limit_date(df2.loc[idx, 'Classification'], df2.loc[idx, 'Date']) for idx in range(len(df2))]
        df3['limit date'] = [my_optimizator.calculate_limit_date(df3.loc[idx, 'Classification'], df3.loc[idx, 'Date']) for idx in range(len(df3))]
        df4['limit date'] = [my_optimizator.calculate_limit_date(df4.loc[idx, 'Classification'], df4.loc[idx, 'Date']) for idx in range(len(df4))]

        # ## Step2
        # # Order calls in ascending order by deadline

        df1 = df1.sort_values('limit date', ascending=True, ignore_index=True) #ordered call prediction with deadlines (sorted by deadline)
        print("These are the predicted calls for week 1 with limit dates for appointments in ascending order.")
        print(df1)
        input("press any key to continue")

        df2 = df2.sort_values('limit date', ascending=True, ignore_index=True) #ordered call prediction with deadlines (sorted by deadline)
        df3 = df3.sort_values('limit date', ascending=True, ignore_index=True) #ordered call prediction with deadlines (sorted by deadline)
        df4 = df4.sort_values('limit date', ascending=True, ignore_index=True) #ordered call prediction with deadlines (sorted by deadline)


        # ## Step3
        # # Define slot reservation agenda for 4 weeks/7days and 30 slots/day and fill it in:
        # # Agenda recommendation: Create a data structure for the entire month, which you can easily pass from one day to another when you encounter null availability.
        #     # use ordered call prediction
        #     # start by assigning the first avail slot the following day to the call and if none avail, the day after
        #     # cannot assign a call a slot for today

        df1['Appointment date'] = df1['Date'] + timedelta(days=1) #df['Date'].to_pydatetime() + timedelta(days=1) #Appointment date= when the first appointment could be given for that call is slots were avail.
        print("These are the predicted calls for week 1 with first valid date for an appointment per call.")
        print(df1)
        input("press any key to continue")

        df2['Appointment date'] = df2['Date'] + timedelta(days=1) 
        df3['Appointment date'] = df3['Date'] + timedelta(days=1) 
        df4['Appointment date'] = df4['Date'] + timedelta(days=1) 

        agenda = my_optimizator.empty_agenda_generator()
        reserved_slots_dict = my_optimizator.empty_agenda_generator()
        avail_slots = my_optimizator.avail_slots_dict() 

        ### Fill in the same reserved_slots_dict with predictions for the 4 weeks in the month

        for idx in range(len(df1)):
            my_optimizator.reserved_slots_filler(df1.loc[idx, 'Appointment date'], df1.loc[idx, 'Classification'], df1.loc[idx, 'NumCalls (Normal dist.)'], reserved_slots_dict, avail_slots)

        for idx in range(len(df2)):
            my_optimizator.reserved_slots_filler(df2.loc[idx, 'Appointment date'], df2.loc[idx, 'Classification'], df2.loc[idx, 'NumCalls (Normal dist.)'], reserved_slots_dict, avail_slots)

        for idx in range(len(df3)):
            my_optimizator.reserved_slots_filler(df3.loc[idx, 'Appointment date'], df3.loc[idx, 'Classification'], df3.loc[idx, 'NumCalls (Normal dist.)'], reserved_slots_dict, avail_slots)

        for idx in range(len(df4)):
            my_optimizator.reserved_slots_filler(df4.loc[idx, 'Appointment date'], df4.loc[idx, 'Classification'], df4.loc[idx, 'NumCalls (Normal dist.)'], reserved_slots_dict, avail_slots)


        ### Show reserved slots agenda as a df structure

        df_reserved_slots_agenda = pd.DataFrame(reserved_slots_dict)
        df_reserved_slots_agenda = df_reserved_slots_agenda.T
        df_reserved_slots_agenda['Slots available'] = avail_slots
        df_reserved_slots_agenda.index.name = 'Date'
        df_reserved_slots_agenda.reset_index()
        #
        #df_reserved_slots_agenda['Day of week'] = df_reserved_slots_agenda['Date'].apply(lambda x: x.strftime('%A'))
        #
        print("This is the schedule of reserved slots and available slots for the month")
        print(df_reserved_slots_agenda)
        input("press any key to continue") 

        ##### PHASE 4: PATIENT CALL SIMULATION
        ## We are generating lists of simulated patient calls using the call history to randomly simulate calls per type of patient and day of the week
        ## Look at min and max n of calls for a given weekday (e.g. Monday) and randomly calculate number of calls for Mondays (Xi= random n between min and max)
        ## Generate a list of lenght Xi and randomly assigne type of client to each of that elemnts in list -> will be the simulated calls

        #my_simulation = Simulation() ### TODO define class in new module for further refactoring
        
        df_call_history = pd.read_excel(datasetpath, sheet_name='Sheet1', decimal='.')
        df_call_history['Weekday'] = df_call_history['Fec. Alta'] # df_call_history['Weekday'] = df.loc[:,'Fec. Alta']
        df_call_history['Weekday'] = df_call_history['Weekday'].apply(lambda x: x.strftime('%A'))

        call_history_dict = {'Monday':{},'Tuesday':{},'Wednesday':{},'Thursday':{},'Friday':{},'Saturday':{},'Sunday':{}}

        def call_history_counter(a, b, call_history_dict):
            """From a dataframe, fills in a dictionary of weekdays with dates of calls as keys of a nested dict and number of calls as values"""
            weekdays=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
            for d in weekdays:
                if a == d:
                    if b not in call_history_dict[d].keys():
                        call_history_dict[d][b] = 1
                    else:
                        call_history_dict[d][b] += 1
            
        for idx in range(len(df_call_history)):
            call_history_counter(df_call_history.loc[idx, 'Weekday'], df_call_history.loc[idx, 'Fec. Alta'], call_history_dict)

        #### CALL SIMULATION FOR 4 WEEKS

        weekdays=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        weekday_calls = {'Monday' : [], 'Tuesday': [], 'Wednesday':[], 'Thursday':[],'Friday':[],'Saturday':[],'Sunday':[]
            }

            #### CALL SIMULATION PER WEEK

        def generate_weekly_simulation(dic_weekdays_simulated_call):
            """Fills in a dict with day of week as keys and number of calls per type of client as values"""
            for d in weekdays:
                for day in call_history_dict:
                    if day == d:
                        for date in call_history_dict[d].keys():
                            weekday_calls[d].append(call_history_dict[d][date]) # populate list with numbers of calls received that day of the week over the call history ()
                simulated_n_calls = np.random.randint(min(weekday_calls[d]),max(weekday_calls[d]))
                dic_weekdays_simulated_call[d] = np.random.choice(['P1','P2','P3'],simulated_n_calls) # generate n random repeats between values 'P1','P2','
            return dic_weekdays_simulated_call
    
        weekdays_simulated_calls_1={}
        weekdays_simulated_calls_1 = generate_weekly_simulation(weekdays_simulated_calls_1)
        # print("Simulated calls per weekday for week 1")
        # print(weekdays_simulated_calls)
        # input("press any key to close") 
        weekdays_simulated_calls_2={}
        weekdays_simulated_calls_2 = generate_weekly_simulation(weekdays_simulated_calls_2)
        weekdays_simulated_calls_3={} 
        weekdays_simulated_calls_3 = generate_weekly_simulation(weekdays_simulated_calls_3)
        weekdays_simulated_calls_4={}
        weekdays_simulated_calls_4 = generate_weekly_simulation(weekdays_simulated_calls_4)

        ########
        #Ejemplo Outputs
   
        # Simulated calls per weekday
        # {'Monday': array(['P3', 'P3', 'P3', 'P1', 'P3', 'P1', 'P3', 'P3', 'P1', 'P2', 'P1',
        #        'P1', 'P1', 'P1', 'P3'], dtype='<U2'), 'Tuesday': array(['P1', 'P3', 'P3', 'P2', 'P2', 'P3', 'P2', 'P2', 'P1', 'P2', 'P3',
        #        'P3', 'P1', 'P2', 'P2', 'P3', 'P3', 'P2', 'P1'],

        # reserved slots dic
        # {'2024-06-17': {'P1': 0, 'P2': 0, 'P3': 0}, '2024-06-18': {'P1': 4, 'P2': 6, 'P3': 6}, 

        # agenda
        # {'2024-06-17': {'P1': 0, 'P2': 0, 'P3': 0}, '2024-06-18': {'P1': 0, 'P2': 0, 'P3': 0}, 

        ######

        def add_penalty(ele, first_app_date, call_date, penalties):
            """Adds penalties for appointments scheduled after the limit date according to each client type SLA"""
            date1 = datetime.datetime.strptime(call_date,'%Y-%m-%d')
            date2 = datetime.datetime.strptime(first_app_date,'%Y-%m-%d')
            diff = (date2 - date1).days
            if ele == 'P1':
                if diff > 2:
                    penalties +=1
                    #print("Here is a penalty: ", penalties)
            elif ele == 'P2':
                if diff > 3:
                    penalties +=1
                    #print("Here is a penalty: ", penalties)
            elif ele == 'P3':
                if diff > 4:
                    penalties +=1
                    #print("Here is a penalty: ", penalties)
            return penalties

        def agenda_filler(call, idx, call_day_idx, reserved_slots_dict, agenda, avail_slots):
            """Fills in the agenda with appointments for the simulated calls"""
            indx_range = range(0,len(reserved_slots_dict))
            penalties = 0
            if idx in indx_range:
                for index, item in enumerate(reserved_slots_dict.items()): #  The enumerate() method takes a sequence (such as a list or tuple) and returns an enumerate object, which contains pairs of the form (index, item).
                    if index == call_day_idx:
                        call_date = item[0] # date of the call
                    if index == idx: # date immediate after the call (or later if no appointments could be made on that date)
                        first_app_date = item[0] #  = '2024-06-18' (date of day after the call (key of second element in reserved_slots_dict))
                        for ele in item[1]: # e.g. ({'P1': 4, 'P2': 6, 'P3': 6}), reserved slots for date of day after the call
                            if ele == call: # simulated call (e.g. P1)
                                if reserved_slots_dict[first_app_date][ele] > 0: # if there are reserved slots for that type of client for that day
                                    reserved_slots_dict[first_app_date][ele] -=1
                                    agenda[first_app_date][ele] +=1
                                    penalties = add_penalty(ele, first_app_date, call_date, penalties)
                                    return penalties
                                else:
                                    if avail_slots[first_app_date] > 0: # if there are still avail slots for that day (not reserved)
                                        agenda[first_app_date][ele] +=1
                                        avail_slots[first_app_date] -= 1
                                        penalties = add_penalty(ele, first_app_date, call_date, penalties)
                                        return penalties
                                    else:
                                        #There are no available slots for the day right after the call, the call will be scheduled after that date.
                                        idx += 1 # the loop is repeated for new element of the enumerate (index, item) and tries to set appointment for current call on this new date
            else:
               print("An appointment could not be scheduled for this call. Wait for next month's schedule to be released.")
            return penalties

        #### AGENDA FILLING PER WEEK
        
        idx_initial_call_schedule_1 = {'Monday' : 1, 'Tuesday': 2, 'Wednesday':3, 'Thursday':4,'Friday':5,'Saturday':6,'Sunday':7
            } # for Monday calls on week 1, idx is 1 because we want to start schedulling calls from the day after the call 

        idx_initial_call_schedule_2 = {'Monday' : 8, 'Tuesday': 9, 'Wednesday':10, 'Thursday':11,'Friday':12,'Saturday':13,'Sunday':14
            } # for Monday calls on week 2, idx is 8 because we want to start schedulling calls from the day after the call

        idx_initial_call_schedule_3 = {'Monday' : 15, 'Tuesday': 16, 'Wednesday':17, 'Thursday':18,'Friday':19,'Saturday':20,'Sunday':21
            } # for Monday calls on week 3, idx is 15 because we want to start schedulling calls from the day after the call

        idx_initial_call_schedule_4 = {'Monday' : 22, 'Tuesday': 23, 'Wednesday':24, 'Thursday':25,'Friday':26,'Saturday':27,'Sunday':28
            } # for Monday calls on week 4, idx is 22 because we want to start schedulling calls from the day after the call

        ### AGENDA FILLING FOR WEEK 1

        ## TODO - REFACTORING - not quite right yet
        
        # list_weeks_simulated_calls = [weekdays_simulated_calls_1, weekdays_simulated_calls_2, weekdays_simulated_calls_3, weekdays_simulated_calls_4]
        # list_idx_initial_call_schedule = [idx_initial_call_schedule_1, idx_initial_call_schedule_2, idx_initial_call_schedule_3, idx_initial_call_schedule_4]
        
        # def agenda_filler_per_week(week, idx_initial_call_sch, reserved_slots_dict, agenda, avail_slots):
        #     """Fills the agenda for a given week and returns penalties for that week"""
        #     week_penalties = 0
        #     for d in week:
        #         for call in week[d]:   
        #             idx = idx_initial_call_sch[d] 
        #             call_day_idx = idx_initial_call_sch[d] -1
        #             penalties_for_this_call = agenda_filler(call, idx, call_day_idx, reserved_slots_dict, agenda, avail_slots)
        #             #total_penalties = total_penalties + penalties_for_this_call
        #             week_penalties = week_penalties + penalties_for_this_call
        #             return week_penalties            
        
        ##
        # total_penalties = 0
        # week_idx = 0
        # for week in list_weeks_simulated_calls:
        #     print(week)
        #     print('This is the week index: ', week_idx)
        #     input("press any key to CLOSE")  
        #     idx_initial_call_sch =  list_idx_initial_call_schedule[week_idx]
        #     print('This is the idx_initial_calls: ', idx_initial_call_sch)
        #     input("press any key to CLOSE") 
        #     this_week_penalties = agenda_filler_per_week(week, idx_initial_call_sch, reserved_slots_dict, agenda, avail_slots)
        #     total_penalties = total_penalties + this_week_penalties
        #     week_idx +=1
        #     print('These are the penalties for this week: ', this_week_penalties)
        #     input("press any key to CLOSE") 
        ##

        # total_penalties = 0
        # week_idx = 0
        # for week in list_weeks_simulated_calls:
        #     idx_initial_call_sch =  list_idx_initial_call_schedule[week_idx]
        #     this_week_penalties = agenda_filler_per_week(week, idx_initial_call_sch, reserved_slots_dict, agenda, avail_slots)
        #     total_penalties = total_penalties + this_week_penalties
        #     week_idx +=1
        #     print('These are the penalties for this week: ', this_week_penalties)
        #     input("press any key to CLOSE")
        
        # print('These are the total penalties: ', total_penalties)
        # input("press any key to CLOSE") 
    
############

        ### AGENDA FILLING FOR WEEK 1        
        
        # idx_initial_call_schedule_1 = {'Monday' : 1, 'Tuesday': 2, 'Wednesday':3, 'Thursday':4,'Friday':5,'Saturday':6,'Sunday':7
        #     } # for Monday calls, idx is 1 because we want to start schedulling calls from the day after the call 

        total_penalties = 0
        for d in weekdays_simulated_calls_1: # for each key (day of week), e.g. d = Monday
            for call in weekdays_simulated_calls_1[d]: # for each simulated call # for call in weekdays_simulated_calls['Tuesday']  
                idx = idx_initial_call_schedule_1[d]  # index of date after the call: means the second ele of reserved_slots_dict (for a call on Monday, the date would be that of the first Tuesday on the dict)
                call_day_idx = idx_initial_call_schedule_1[d] -1 # index of the date of the call
                #print("This is the call day: ", call_day_idx)
                #agenda_filler(call, idx, call_day_idx reserved_slots_dict, agenda, avail_slots)
                penalties_for_this_call = agenda_filler(call, idx, call_day_idx, reserved_slots_dict, agenda, avail_slots)
                total_penalties = total_penalties + penalties_for_this_call

        ### AGENDA FILLING FOR WEEK 2
        
        # idx_initial_call_schedule_2 = {'Monday' : 8, 'Tuesday': 9, 'Wednesday':10, 'Thursday':11,'Friday':12,'Saturday':13,'Sunday':14
        #     } # for Monday calls, idx is 8 because we want to start schedulling calls from the day after the call

        for d in weekdays_simulated_calls_2:
            for call in weekdays_simulated_calls_2[d]:  
                idx = idx_initial_call_schedule_2[d] ####
                call_day_idx = idx_initial_call_schedule_2[d] -1
                penalties_for_this_call = agenda_filler(call, idx, call_day_idx, reserved_slots_dict, agenda, avail_slots)
                total_penalties = total_penalties + penalties_for_this_call

        ### AGENDA FILLING FOR WEEK 3
        
        # idx_initial_call_schedule_3 = {'Monday' : 15, 'Tuesday': 16, 'Wednesday':17, 'Thursday':18,'Friday':19,'Saturday':20,'Sunday':21
        #     } # for Monday calls, idx is 15 because we want to start schedulling calls from the day after the call

        for d in weekdays_simulated_calls_3:
            for call in weekdays_simulated_calls_3[d]:  
                idx = idx_initial_call_schedule_3[d] ####
                call_day_idx = idx_initial_call_schedule_3[d] -1
                penalties_for_this_call = agenda_filler(call, idx, call_day_idx, reserved_slots_dict, agenda, avail_slots)
                total_penalties = total_penalties + penalties_for_this_call

        ### AGENDA FILLING FOR WEEK 4
        
        # idx_initial_call_schedule_4 = {'Monday' : 22, 'Tuesday': 23, 'Wednesday':24, 'Thursday':25,'Friday':26,'Saturday':27,'Sunday':28
        #     } # for Monday calls, idx is 22 because we want to start schedulling calls from the day after the call

        for d in weekdays_simulated_calls_4:
            for call in weekdays_simulated_calls_4[d]:  
                idx = idx_initial_call_schedule_4[d] ####
                call_day_idx = idx_initial_call_schedule_4[d] -1
                penalties_for_this_call = agenda_filler(call, idx, call_day_idx, reserved_slots_dict, agenda, avail_slots)
                total_penalties = total_penalties + penalties_for_this_call
      
        ### Show filled agenda as a df structure

        df_final_output = pd.DataFrame(agenda)
        df_final_output = df_final_output.T
        df_final_output['Slots available'] = avail_slots
        df_final_output.index.name = 'Date'
        df_final_output.reset_index()
        print("Output of Phase 4 (monthly schedule - filled agenda)  (starting Monday : ", monday_week1)
        print(df_final_output, "\n")
        print("These are the penalties incurred for this period: ", total_penalties, "\n")
    
        input("press any key to close")
  
    except AssertionError:
        print('Invalid date entered.')
        input('Press any key to try again')
       # print('Please, try again: the date entered must correspond to a Monday and have the following format YYYY-MM-DD') ## chequear que esa fecha corresponde con un lunes!
        main()
        #input('Press any key to try again')
        
    except Exception as ex:
        print('Ha habido una excepcion: ', ex)
        input('Press any key to close the programm')

if __name__ == '__main__':
    main()

##################################################################################################################################
### My final notes

## Convert this to 'main' module - create and refactor class Simulation() TODO
## Predicci�n() - OJO, normal distribution with those std gives some negative numbers for predicted calls! - some reserved slots become a negative number!

##################################################################################################################################