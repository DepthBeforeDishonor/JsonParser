import numpy
import matplotlib
import json



def main():
    with open('data.txt', 'r') as file:
       lines=file.readlines();
    json_array=[]
    for line in lines:
        event=json.loads(line)
        json_array.append(event)
    print(json_array)
main()
