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
            reasn_as_string="Band Bonds"

        case 2:
            reason_as_string="Changing Tips"

        case 3:
            reason_as_string="Chanigng Reel"

        case 4:
            reason_as_string="Changing Crystals"

        case 5:
            reason_as_string=""

        case 6:
            reason_as_string=''

        case 7:
            reason_as_string=''

        case 8:
            reason_as_string=''


        case 9:
            reasn_as_string=''

        case 10:
            reason_as_string=''

        case 11:
            reason_as_string=''

        case 12:
            reason_as_string=''

        case 13:
            reasn_as_string=''

        case 14:
            reason_as_string=''

        case 15:
            reason_as_string=''

        case 16:
            reason_as_string=''

        case 17:
            reason_as_string=''

        case 18:
            reason_as_string=''

        case 21:
            reason_as_string="Time Spent in Manual Mode"

    return reason_as_string






def timeDecoder(string):
    

    #string=string[11:]
    #hour=string[0:2]
    #hour=int(hour)
    #minute=string[3:5]
    #minute=int(minute)
    #second=string[-2:]
    #second=int(second)
    #time=dt.time(hour,minute,second)
    time=dt.datetime.fromisoformat(string)
    #time=tt.strptime(string,"%H:%M:%S")
    #time=dt.strptime(string,"%H:%M:%S")
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
        
    file_path_csv=file_path.replace(".txt", ".csv",1)


    with open(file_path_csv, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(csv_list)

    

main()
