##### PHASE 4: PATIENT CALL SIMULATION
## We are generating lists of simulated patient calls using the call history to randomly simulate calls per type of patient and day of the week
## Look at min and max n of calls for a given weekday (e.g. Monday) and randomly calculate number of calls for Mondays (Xi= random n between min and max)
## Generate a list of lenght Xi and randomly assigne type of client to each of that elemnts in list -> will be the simulated calls

import numpy as np
import datetime

class Simulation:
    """Class used to generate a simulation of the calls per type of patient and day of the 
    week for each week, fill in the agenda according to the simulation and calculate number of penalties"""    

    weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']  # class attribute
    
    def __init__(self):
        """class constructor"""
        
        ##self.weekdays = weekdays # instance variable
        
    def call_history_counter(self, a, b, call_history_dict):
        """From a dataframe, fills in a dictionary of weekdays with dates of calls as keys of a nested dict and number of calls
        as values"""
        
        for d in Simulation.weekdays:
            if a == d:
                if b not in call_history_dict[d].keys():
                    call_history_dict[d][b] = 1
                else:
                    call_history_dict[d][b] += 1
                    
    def generate_weekly_simulation(self, call_history_dict, weekday_calls, dic_weekdays_simulated_call):
        """Fills in a dict with day of week as keys and simulated number of calls per type of client as values,
        taking into account the min and max n call for that day of week in call history."""
        
        for d in Simulation.weekdays:
            for day in call_history_dict:
                if day == d:
                    for date in call_history_dict[d].keys():
                        weekday_calls[d].append(call_history_dict[d][date]) # populate list with numbers of calls received that day of the week over the call history ()
            simulated_n_calls = np.random.randint(min(weekday_calls[d]),max(weekday_calls[d]))
            dic_weekdays_simulated_call[d] = np.random.choice(['P1','P2','P3'],simulated_n_calls) # generate n random repeats between values 'P1','P2','
        return dic_weekdays_simulated_call
    
    ## ADD PENALTIES
    
    def add_penalty(self, ele, first_app_date, call_date, penalties):
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
    
    ## FILL IN AGENDA

    def agenda_filler(self, call, idx, call_day_idx, reserved_slots_dict, agenda, avail_slots):
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
                            if reserved_slots_dict[first_app_date][ele] > 0: # if there are still reserved slots for that type of client for that day
                                reserved_slots_dict[first_app_date][ele] -=1
                                agenda[first_app_date][ele] +=1
                                penalties = self.add_penalty(ele, first_app_date, call_date, penalties)
                                return penalties
                            else:
                                if avail_slots[first_app_date] > 0: # if there are still avail slots for that day (not reserved)
                                    agenda[first_app_date][ele] +=1
                                    avail_slots[first_app_date] -= 1
                                    penalties = self.add_penalty(ele, first_app_date, call_date, penalties)
                                    return penalties
                                else:
                                    #There are no available slots for the day right after the call, the call will be scheduled after that date.
                                    idx += 1 # the loop is repeated for new element of the enumerate (index, item) and tries to set appointment for current call on this new date
        else:
            print("An appointment could not be scheduled for this call. Wait for next month's schedule to be released.")
        return penalties

    ## AGENDA FILLING PER WEEK

    def agenda_filler_per_week(self, week, idx_initial_call_sch, reserved_slots_dict, agenda, avail_slots):
        """Fills the agenda for a given week and returns penalties for that week"""
        
        week_penalties = 0
                    
        for d in week:
            for call in week[d]:
                idx = idx_initial_call_sch[d] 
                call_day_idx = idx_initial_call_sch[d] -1
                penalties_for_this_call = Simulation.agenda_filler(self, call, idx, call_day_idx, reserved_slots_dict, agenda, avail_slots)
                week_penalties = week_penalties + penalties_for_this_call   
        return week_penalties  