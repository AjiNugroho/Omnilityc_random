import re
import time
from multiprocessing import Pool

def check_data(str_input):
    str_process = str_input.strip()

    if re.match('^\d+([^.,])?$',str_process):
        print(f'{str_process} - integer')
    elif re.match('^\d*\.?\d*$',str_process):
        print(f'{str_process} - real numbers')
    elif re.match('^[a-zA-Z]+$',str_process):
        print(f'{str_process} - alphabetical strings')
    else:
        print(f'{str_process} - alphanumeric')

if __name__=='__main__':
    start_time = time.time()
    p = Pool()
    data_str = ''
    rf = open("generated_file.txt", "r")
    for line in rf:
        data_str = line
    
    list_data = data_str.split(",")
    
    p.map(check_data,list_data)
    
    p.close
    p.join
    end_time = int(time.time() - start_time)
    print(f'Time processing : {end_time} seconds')
    
    rf.close()
