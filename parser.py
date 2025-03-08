import numpy as np
import matplotlib
import json
import tkinter as tk
import tkinter.filedialog
import datetime as dt
import time as tt
import csv






def reason_code_decoder(code):
    #just need a list of reason codes and I can finish this, get from repository tomorrow
    reason_as_string=code
    code=int(code)
    #reason_as_string="default"
    match code:
        case 1:
            reason_as_string="Band Bonds"

        case 2:
            reason_as_string="Changing Tips"

        case 3:
            reason_as_string="Chanigng Reel"

        case 4:
            reason_as_string="Changing Crystals"

        case 5:
            reason_as_string="Missing Material"

        case 6:
            reason_as_string='Punch Problem'

        case 7:
            reason_as_string='Tray Problem'

        case 8:
            reason_as_string='Software Bug'

        case 9:
            reason_as_string='WIre Break'

        case 10:
            reason_as_string='Engineering'

        case 11:
            reason_as_string='Operator Break'

        case 12:
            reason_as_string='Double Modules'

        case 13:
            reason_as_string="Gantry Problem"

        case 14:
            reason_as_string='Welding Problem'

        case 15:
            reason_as_string='Picking Problem'

        case 16:
            reason_as_string='Microstop'

        case 17:
            reason_as_string='Operator Meeting'

        case 18:
            reason_as_string='Machine Start'

        case 21:
            reason_as_string="Manual Mode"

    return reason_as_string






def timeDecoder(string):
    
    time=dt.datetime.fromisoformat(string)
    return time

def main():

    root =tk.Tk()
    root.withdraw()
    file_path = tk.filedialog.askopenfilename()
    #file_path="data.txt"

    #with open(file_path, 'w', newline='') as csvfile:
        #csvwriter = csv.writer(csvfile)

    with open (file_path, 'r') as file:
        lines=file.readlines();
    json_obj_array=[]
    for line in lines:
        event=json.loads(line)
        json_obj_array.append(event)
    json_string_array=[]
    for obj_string in json_string_array:
        un_proc_event=json.loads(obj_string)
        json_obj_array.append(un_proc_event)
    csv_list=[]
    totalized_list=[]
    #with open(file_path, 'w', newline='') as csvfile:
        #csvwriter = csv.writer(csvfile)
    for event in json_obj_array:
        start_time=timeDecoder(event["Start Time"])
        end_time=timeDecoder(event["End Time"])
        duration=end_time-start_time
        duration=int(duration.total_seconds())
        reason=reason_code_decoder(event["Event Type"])
        csvEvent=(reason,duration)
        csv_list.append(csvEvent)
        #i want to totalize the amount of time spent in each event type
        #what if we had a totalzied list that we searched for by reason, then +=duration to.
        

    file_path_csv=file_path.replace(".txt", ".csv",1)

    with open(file_path_csv, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(csv_list)

main()
