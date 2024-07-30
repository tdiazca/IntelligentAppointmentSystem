
#### 'Intelligent appointment system for a health clinic'

import datetime
from datetime import timedelta
from doctest import OutputChecker

import pandas as pd
#import numpy as np
import Classifier as cf
import Prediction as pdt
import Optimizator as opt
import Simulation as smlt

#####################   MAIN FUNCTION

def main():
    """ This function allows the user to choose a date (must be a Monday) being the firt Monday 
    of the month that they want to generate a simulated appointment shcedule for."""
    
    datasetpath = r'.\historico_llamadas.xlsx'
    #datasetpath = r'C:\Users\teresa.diaz.calvo\source\repos\trainingpython\IntelligentAppointmentSystem\historico_llamadas.xlsx'
    #datasetpath = input("Please, enter path to training dataset 'historico_llamadas.xlsx': ") # C:\Users\teresa.diaz.calvo\source\repos\trainingpython\Data_ejercicio_final_python_training\historico_llamadas.xlsx

    df = pd.read_excel(datasetpath, sheet_name='Sheet1', decimal='.')
    
    ### PHASE 1: CLASSIFICATION
    
    ## START CLASSIFICATION ##
    
    conditions = [
        (df['Facturación'] > float(4000)), #Facturación
        ((df['Facturación'] >= float(3000)) & (df['Facturación'] < float(4000))),
        (df['Facturación'] < float(3000))
        ]

    my_classification = cf.Classifier(df, conditions)
    df = my_classification.clasificacion()

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
    
    ## Step 1: We will count how many calls there are from each type of client on each date in the call history.
    ##  We will find the mean and standard deviation for each type of client and for each day of the week.

    ## START PREDICTION ##
    
    ###### PREDICTION  WEEK 1
    
    my_prediction1 = pdt.Prediction(df)

    df1 = my_prediction1.mean_std()
    df1 = df1.rename(columns={'Facturación':'Calls'})
    df1 = df1.rename(columns={'Fec. Alta':'Day of the week'})

    cols = ['Classification', 'Day of the week']
    df1['Combined'] = df1[cols].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)

    categories=['P1_Monday','P2_Monday','P3_Monday','P1_Tuesday','P2_Tuesday','P3_Tuesday','P1_Wednesday','P2_Wednesday',
                                                            'P3_Wednesday','P1_Thursday','P2_Thursday','P3_Thursday','P1_Friday','P2_Friday','P3_Friday','P1_Saturday',
                                                            'P2_Saturday','P3_Saturday','P1_Sunday','P2_Sunday','P3_Sunday']

    df1.Combined = pd.Categorical(df1.Combined, categories)
    df1=df1.sort_values('Combined', ignore_index=True)
    
    #df1 = df.sort_values(by=['Day of the week'], key=lambda s: s.apply(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'].index), ignore_index=True)

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
        # ## Step1
        # # Calculate deadlines for expected calls per date and type of client 

        ## START OPTIMIZATION ##

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
        # # Define slot reservation agenda for 4 weeks/7days and 30 slots/day and fill it in.
        
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
        
        df_call_history = pd.read_excel(datasetpath, sheet_name='Sheet1', decimal='.')
        df_call_history['Weekday'] = df_call_history['Fec. Alta'] # df_call_history['Weekday'] = df.loc[:,'Fec. Alta']
        df_call_history['Weekday'] = df_call_history['Weekday'].apply(lambda x: x.strftime('%A'))

        ## START SIMULATION ##
                
        my_simulation = smlt.Simulation()
        
        # Count calls from call history
        
        call_history_dict = {'Monday':{},'Tuesday':{},'Wednesday':{},'Thursday':{},'Friday':{},'Saturday':{},'Sunday':{}}
            
        for idx in range(len(df_call_history)):
            my_simulation.call_history_counter(df_call_history.loc[idx, 'Weekday'], df_call_history.loc[idx, 'Fec. Alta'], call_history_dict)

        #### CALL SIMULATION FOR 4 WEEKS

        weekday_calls = {'Monday' : [], 'Tuesday': [], 'Wednesday':[], 'Thursday':[],'Friday':[],'Saturday':[],'Sunday':[]
            }

            #### CALL SIMULATION PER WEEK
    
        weekdays_simulated_calls_1={}
        weekdays_simulated_calls_1 = my_simulation.generate_weekly_simulation(call_history_dict, weekday_calls, weekdays_simulated_calls_1)
        # print("Simulated calls per weekday for week 1")
        # print(weekdays_simulated_calls)
        # input("press any key to close") 
        weekdays_simulated_calls_2={}
        weekdays_simulated_calls_2 = my_simulation.generate_weekly_simulation(call_history_dict, weekday_calls, weekdays_simulated_calls_2)
        weekdays_simulated_calls_3={} 
        weekdays_simulated_calls_3 = my_simulation.generate_weekly_simulation(call_history_dict, weekday_calls, weekdays_simulated_calls_3)
        weekdays_simulated_calls_4={}
        weekdays_simulated_calls_4 = my_simulation.generate_weekly_simulation(call_history_dict, weekday_calls, weekdays_simulated_calls_4)

        #### AGENDA FILLING PER WEEK
        
        idx_initial_call_schedule_1 = {'Monday' : 1, 'Tuesday': 2, 'Wednesday':3, 'Thursday':4,'Friday':5,'Saturday':6,'Sunday':7
            } # for Monday calls on week 1, idx is 1 because we want to start schedulling calls from the day after the call 

        idx_initial_call_schedule_2 = {'Monday' : 8, 'Tuesday': 9, 'Wednesday':10, 'Thursday':11,'Friday':12,'Saturday':13,'Sunday':14
            } # for Monday calls on week 2, idx is 8 because we want to start schedulling calls from the day after the call

        idx_initial_call_schedule_3 = {'Monday' : 15, 'Tuesday': 16, 'Wednesday':17, 'Thursday':18,'Friday':19,'Saturday':20,'Sunday':21
            } # for Monday calls on week 3, idx is 15 because we want to start schedulling calls from the day after the call

        idx_initial_call_schedule_4 = {'Monday' : 22, 'Tuesday': 23, 'Wednesday':24, 'Thursday':25,'Friday':26,'Saturday':27,'Sunday':28
            } # for Monday calls on week 4, idx is 22 because we want to start schedulling calls from the day after the call
        
        list_weeks_simulated_calls = [weekdays_simulated_calls_1, weekdays_simulated_calls_2, weekdays_simulated_calls_3, weekdays_simulated_calls_4]
        list_idx_initial_call_schedule = [idx_initial_call_schedule_1, idx_initial_call_schedule_2, idx_initial_call_schedule_3, idx_initial_call_schedule_4]
                
        total_penalties = 0
        week_idx = 0
        for week in list_weeks_simulated_calls:
            idx_initial_call_sch =  list_idx_initial_call_schedule[week_idx]            
            this_week_penalties = my_simulation.agenda_filler_per_week(week, idx_initial_call_sch, reserved_slots_dict, agenda, avail_slots)
            total_penalties = total_penalties + this_week_penalties
            week_idx +=1
            
        #     print('These are the penalties for this week: ', this_week_penalties)
        #     input("press any key to CLOSE") 
        
        # print('These are the total penalties: ', total_penalties)
        # input("press any key to CLOSE") 
    
        ### Show filled agenda as a df structure

        df_final_output = pd.DataFrame(agenda)
        df_final_output = df_final_output.T
        df_final_output['Slots available'] = avail_slots
        df_final_output.index.name = 'Date'
        df_final_output.reset_index()
        print("Output of Phase 4 (monthly schedule - filled agenda)  (starting Monday : ", monday_week1)
        print("This dataframe shows the scheduled calls per day and the slots that ramain available.")
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
# ##Ejemplo outputs
   
# # Simulated calls per weekday
# # {'Monday': array(['P3', 'P3', 'P3', 'P1', 'P3', 'P1', 'P3', 'P3', 'P1', 'P2', 'P1',
# #        'P1', 'P1', 'P1', 'P3'], dtype='<U2'), 'Tuesday': array(['P1', 'P3', 'P3', 'P2', 'P2', 'P3', 'P2', 'P2', 'P1', 'P2', 'P3',
# #        'P3', 'P1', 'P2', 'P2', 'P3', 'P3', 'P2', 'P1'],...

# # reserved slots dic
# # {'2024-06-17': {'P1': 0, 'P2': 0, 'P3': 0}, '2024-06-18': {'P1': 4, 'P2': 6, 'P3': 6},... 

# # agenda
# # {'2024-06-17': {'P1': 0, 'P2': 0, 'P3': 0}, '2024-06-18': {'P1': 0, 'P2': 0, 'P3': 0}, ...
##################################################################################################################################

# ## EXAMPLE main() OUTPUT
    
# # Please, enter a date for which the Prediction should be created. This must must correspond to a Monday and have the following format YYYY-MM-DD: 2024-06-17
# # Dataframe for week 1 before returning week
# #    Classification Day of the week     Calls                Combined
# #                                        mean       std
# # 0              P1          Monday  4.200000  5.094660     P1_Monday
# # 1              P2          Monday  4.666667  6.889179     P2_Monday
# # 2              P3          Monday  5.317422  8.651241     P3_Monday
# # 3              P1         Tuesday  3.600000  5.501515    P1_Tuesday
# # 4              P2         Tuesday  4.743243  6.886677    P2_Tuesday
# # 5              P3         Tuesday  5.736077  9.158294    P3_Tuesday
# # 6              P1       Wednesday  4.500000  5.681354  P1_Wednesday
# # 7              P2       Wednesday  5.013889  7.172901  P2_Wednesday
# # 8              P3       Wednesday  5.464891  8.829664  P3_Wednesday
# # 9              P1        Thursday  4.000000  7.094599   P1_Thursday
# # 10             P2        Thursday  4.688312  7.178659   P2_Thursday
# # 11             P3        Thursday  5.721805  8.958323   P3_Thursday
# # 12             P1          Friday  3.900000  5.782156     P1_Friday
# # 13             P2          Friday  4.573770  6.206070     P2_Friday
# # 14             P3          Friday  5.142473  7.973245     P3_Friday
# # 15             P1        Saturday  1.666667  1.154701   P1_Saturday
# # 16             P2        Saturday  1.153846  0.375534   P2_Saturday
# # 17             P3        Saturday  1.630952  1.588966   P3_Saturday
# # 18             P1          Sunday  1.000000  0.000000     P1_Sunday
# # 19             P2          Sunday  2.071429  1.384768     P2_Sunday
# # 20             P3          Sunday  1.702970  2.156592     P3_Sunday
# # press key to continue
    
# # C:\Users\teresa.diaz.calvo\source\repos\trainingpython\IntelligentAppointmentSystem\Prediction.py:36: FutureWarning: Non-integer 'periods' in pd.date_range, pd.timedelta_range, pd.period_range, and pd.interval_range are deprecated and will raise in a future version.
# #   s_dates = pd.date_range(start=initial_date, periods=len(df)/3, freq='D')
    
# # Dataframe for week 1 with dates
# #    Classification Day of the week     Calls                Combined       Date
# #                                        mean       std
# # 0              P1          Monday  4.200000  5.094660     P1_Monday 2024-06-17
# # 1              P2          Monday  4.666667  6.889179     P2_Monday 2024-06-17
# # 2              P3          Monday  5.317422  8.651241     P3_Monday 2024-06-17
# # 3              P1         Tuesday  3.600000  5.501515    P1_Tuesday 2024-06-18
# # 4              P2         Tuesday  4.743243  6.886677    P2_Tuesday 2024-06-18
# # 5              P3         Tuesday  5.736077  9.158294    P3_Tuesday 2024-06-18
# # 6              P1       Wednesday  4.500000  5.681354  P1_Wednesday 2024-06-19
# # 7              P2       Wednesday  5.013889  7.172901  P2_Wednesday 2024-06-19
# # 8              P3       Wednesday  5.464891  8.829664  P3_Wednesday 2024-06-19
# # 9              P1        Thursday  4.000000  7.094599   P1_Thursday 2024-06-20
# # 10             P2        Thursday  4.688312  7.178659   P2_Thursday 2024-06-20
# # 11             P3        Thursday  5.721805  8.958323   P3_Thursday 2024-06-20
# # 12             P1          Friday  3.900000  5.782156     P1_Friday 2024-06-21
# # 13             P2          Friday  4.573770  6.206070     P2_Friday 2024-06-21
# # 14             P3          Friday  5.142473  7.973245     P3_Friday 2024-06-21
# # 15             P1        Saturday  1.666667  1.154701   P1_Saturday 2024-06-22
# # 16             P2        Saturday  1.153846  0.375534   P2_Saturday 2024-06-22
# # 17             P3        Saturday  1.630952  1.588966   P3_Saturday 2024-06-22
# # 18             P1          Sunday  1.000000  0.000000     P1_Sunday 2024-06-23
# # 19             P2          Sunday  2.071429  1.384768     P2_Sunday 2024-06-23
# # 20             P3          Sunday  1.702970  2.156592     P3_Sunday 2024-06-23
# # press any key to continue

# # These are the predicted calls for week 1
# #    Classification Day of the week       Date NumCalls (Normal dist.)

# # 0              P1          Monday 2024-06-17                       9
# # 1              P2          Monday 2024-06-17                       6
# # 2              P3          Monday 2024-06-17                      14
# # 3              P1         Tuesday 2024-06-18                       0
# # 4              P2         Tuesday 2024-06-18                       0
# # 5              P3         Tuesday 2024-06-18                       5
# # 6              P1       Wednesday 2024-06-19                       6
# # 7              P2       Wednesday 2024-06-19                      17
# # 8              P3       Wednesday 2024-06-19                      14
# # 9              P1        Thursday 2024-06-20                       5
# # 10             P2        Thursday 2024-06-20                       0
# # 11             P3        Thursday 2024-06-20                      11
# # 12             P1          Friday 2024-06-21                       8
# # 13             P2          Friday 2024-06-21                       2
# # 14             P3          Friday 2024-06-21                       0
# # 15             P1        Saturday 2024-06-22                       0
# # 16             P2        Saturday 2024-06-22                       0
# # 17             P3        Saturday 2024-06-22                       0
# # 18             P1          Sunday 2024-06-23                       1
# # 19             P2          Sunday 2024-06-23                       1
# # 20             P3          Sunday 2024-06-23                       0
# # press any key to continue

# # These are the predicted calls for week 1 with limit dates for appointments.
# #    Classification Day of the week       Date NumCalls (Normal dist.) limit date

# # 0              P1          Monday 2024-06-17                       9 2024-06-19
# # 1              P2          Monday 2024-06-17                       6 2024-06-20
# # 2              P3          Monday 2024-06-17                      14 2024-06-21
# # 3              P1         Tuesday 2024-06-18                       0 2024-06-20
# # 4              P2         Tuesday 2024-06-18                       0 2024-06-21
# # 5              P3         Tuesday 2024-06-18                       5 2024-06-22
# # 6              P1       Wednesday 2024-06-19                       6 2024-06-21
# # 7              P2       Wednesday 2024-06-19                      17 2024-06-22
# # 8              P3       Wednesday 2024-06-19                      14 2024-06-23
# # 9              P1        Thursday 2024-06-20                       5 2024-06-22
# # 10             P2        Thursday 2024-06-20                       0 2024-06-23
# # 11             P3        Thursday 2024-06-20                      11 2024-06-24
# # 12             P1          Friday 2024-06-21                       8 2024-06-23
# # 13             P2          Friday 2024-06-21                       2 2024-06-24
# # 14             P3          Friday 2024-06-21                       0 2024-06-25
# # 15             P1        Saturday 2024-06-22                       0 2024-06-24
# # 16             P2        Saturday 2024-06-22                       0 2024-06-25
# # 17             P3        Saturday 2024-06-22                       0 2024-06-26
# # 18             P1          Sunday 2024-06-23                       1 2024-06-25
# # 19             P2          Sunday 2024-06-23                       1 2024-06-26
# # 20             P3          Sunday 2024-06-23                       0 2024-06-27
# # press any key to continue
    
# # These are the predicted calls for week 1 with limit dates for appointments in ascending order.
# #    Classification Day of the week       Date NumCalls (Normal dist.) limit date

# # 0              P1          Monday 2024-06-17                       9 2024-06-19
# # 1              P2          Monday 2024-06-17                       6 2024-06-20
# # 2              P1         Tuesday 2024-06-18                       0 2024-06-20
# # 3              P3          Monday 2024-06-17                      14 2024-06-21
# # 4              P2         Tuesday 2024-06-18                       0 2024-06-21
# # 5              P1       Wednesday 2024-06-19                       6 2024-06-21
# # 6              P3         Tuesday 2024-06-18                       5 2024-06-22
# # 7              P2       Wednesday 2024-06-19                      17 2024-06-22
# # 8              P1        Thursday 2024-06-20                       5 2024-06-22
# # 9              P1          Friday 2024-06-21                       8 2024-06-23
# # 10             P2        Thursday 2024-06-20                       0 2024-06-23
# # 11             P3       Wednesday 2024-06-19                      14 2024-06-23
# # 12             P3        Thursday 2024-06-20                      11 2024-06-24
# # 13             P2          Friday 2024-06-21                       2 2024-06-24
# # 14             P1        Saturday 2024-06-22                       0 2024-06-24
# # 15             P3          Friday 2024-06-21                       0 2024-06-25
# # 16             P2        Saturday 2024-06-22                       0 2024-06-25
# # 17             P1          Sunday 2024-06-23                       1 2024-06-25
# # 18             P3        Saturday 2024-06-22                       0 2024-06-26
# # 19             P2          Sunday 2024-06-23                       1 2024-06-26
# # 20             P3          Sunday 2024-06-23                       0 2024-06-27
# # press any key to continue
    
# # These are the predicted calls for week 1 with first valid date for an appointment per call.
# #    Classification Day of the week  ... limit date Appointment date
# #                                    ...
# # 0              P1          Monday  ... 2024-06-19       2024-06-18
# # 1              P2          Monday  ... 2024-06-20       2024-06-18
# # 2              P1         Tuesday  ... 2024-06-20       2024-06-19
# # 3              P3          Monday  ... 2024-06-21       2024-06-18
# # 4              P2         Tuesday  ... 2024-06-21       2024-06-19
# # 5              P1       Wednesday  ... 2024-06-21       2024-06-20
# # 6              P3         Tuesday  ... 2024-06-22       2024-06-19
# # 7              P2       Wednesday  ... 2024-06-22       2024-06-20
# # 8              P1        Thursday  ... 2024-06-22       2024-06-21
# # 9              P1          Friday  ... 2024-06-23       2024-06-22
# # 10             P2        Thursday  ... 2024-06-23       2024-06-21
# # 11             P3       Wednesday  ... 2024-06-23       2024-06-20
# # 12             P3        Thursday  ... 2024-06-24       2024-06-21
# # 13             P2          Friday  ... 2024-06-24       2024-06-22
# # 14             P1        Saturday  ... 2024-06-24       2024-06-23
# # 15             P3          Friday  ... 2024-06-25       2024-06-22
# # 16             P2        Saturday  ... 2024-06-25       2024-06-23
# # 17             P1          Sunday  ... 2024-06-25       2024-06-24
# # 18             P3        Saturday  ... 2024-06-26       2024-06-23
# # 19             P2          Sunday  ... 2024-06-26       2024-06-24
# # 20             P3          Sunday  ... 2024-06-27       2024-06-24

# # [21 rows x 6 columns]
# # press any key to continue
    
# # This is the schedule of reserved slots and available slots for the month
# #             P1  P2  P3  Slots available
# # Date
# # 2024-06-17   0   0   0               30
# # 2024-06-18   9   6  14                1
# # 2024-06-19   0   0   5               25
# # 2024-06-20  13  17   0                0
# # 2024-06-21   5   0  11               14
# # 2024-06-22   8   2   0               20
# # 2024-06-23   0   0   0               30
# # 2024-06-24   1   1   0               28
# # 2024-06-25   1  12   0               17
# # 2024-06-26   0   9  11               10
# # 2024-06-27   5   3   3               19
# # 2024-06-28   1   0   3               26
# # 2024-06-29   6   8   8                8
# # 2024-06-30   1   1   1               27
# # 2024-07-01   1   3   2               24
# # 2024-07-02   5   8   9                8
# # 2024-07-03   7   9   5                9
# # 2024-07-04   3  12   0               15
# # 2024-07-05   5   4  14                7
# # 2024-07-06   0   0   8               22
# # 2024-07-07   1   1   0               28
# # 2024-07-08   1   1   0               28
# # 2024-07-09   0   8   0               22
# # 2024-07-10   4   0  12               14
# # 2024-07-11   7   6   9                8
# # 2024-07-12  25   5   0                0
# # 2024-07-13   5   0   0               25
# # 2024-07-14   1   1   2               26
# # 2024-07-15   1   1   4               24
# # 2024-07-16   0   0   0               30
# # press any key to continue
    
# # Output of Phase 4 (monthly schedule - filled agenda)  (starting Monday :  2024-06-17
# # This dataframe shows the scheduled calls per day and the slots that ramain available.
# #             P1  P2  P3  Slots available
# # Date
# # 2024-06-17   0   0   0               30
# # 2024-06-18   3   2   6                1
# # 2024-06-19  12   9   9                0
# # 2024-06-20   8   9   0                0
# # 2024-06-21   7   9  14                0
# # 2024-06-22   7   7   8                7
# # 2024-06-23   3   2   2               23
# # 2024-06-24   2   0   2               25
# # 2024-06-25  10  10   3                5
# # 2024-06-26   9   9  12                0
# # 2024-06-27   2   3   4               18
# # 2024-06-28   0   0   1               26
# # 2024-06-29   4   1   0                8
# # 2024-06-30   2   3   0               24
# # 2024-07-01   1   0   1               24
# # 2024-07-02   9  11  10                0
# # 2024-07-03   4  11   8                4
# # 2024-07-04   7  11   8                3
# # 2024-07-05  10   6  11                0
# # 2024-07-06   5   9   5                8
# # 2024-07-07   1   6   0               23
# # 2024-07-08   0   1   1               27
# # 2024-07-09   2   4   5               15
# # 2024-07-10  10   8  12                0
# # 2024-07-11  12   9   9                0
# # 2024-07-12  17   5   0                0
# # 2024-07-13   4  13  12                0
# # 2024-07-14   3  14   8                5
# # 2024-07-15   4   0   1               21
# # 2024-07-16   0   0   0               30

# # These are the penalties incurred for this period:  3

# # press any key to close