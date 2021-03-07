import random
import string
import os
import time
from multiprocessing import Process, Value



def RandomText(letters,fd):

    while fd.tell()<10000000:
        random_len = random.randint(5,15)
        randomtext = ''.join(random.choice(letters) for i in range(random_len))
        fd.write(' '+str(randomtext)+',')
       

def RandomInteger(number,fd):

    while fd.tell()<10000000:
        randomint = random.randint(1,100000000)
        fd.write(' '+str(randomint)+',')
        

def RandomAlfanum(alfanum,fd):
    
    while fd.tell()<10000000:
        random_len = random.randint(5,15)
        head = random.randint(1,5)*' '
        tail = random.randint(1,5)*' '
        randomalfa = ''.join(random.choice(alfanum) for i in range(random_len))
        randomalfa += str(random_len)
        randomalfa = head + randomalfa + tail
        fd.write(' '+str(randomalfa)+',')   

def RandomRealnumber(fd):

    while fd.tell()<10000000:
        randomint = random.randint(1,100000)
        rand_real = random.random()
        real_number = rand_real * randomint
        fd.write(' '+str(real_number)+',')
        

if __name__=='__main__':
    start_time = time.time()
    
    file_path = 'generated_file.txt'
    if os.path.exists(file_path):
        os.remove(file_path)
    
    letters = string.ascii_letters
    number = string.digits
    alfanum = string.ascii_letters+string.digits


    fd = open('generated_file.txt','a')
    proc1 = Process(target=RandomText,args=(letters,fd))
    proc2 = Process(target=RandomInteger,args=(number,fd))
    proc3 = Process(target=RandomAlfanum,args=(alfanum,fd))
    proc4 = Process(target=RandomRealnumber,args=(fd,))

    proc1.start()
    proc2.start()
    proc3.start()
    proc4.start()

    proc1.join()
    proc2.join()
    proc3.join()
    proc4.join()
    fd.close()
    end_time = int (time.time() - start_time)
    print(f'Processing time : {end_time} seconds')
