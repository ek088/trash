import time


count = 0


while True:

    with open('inf.txt', 'a') as file:

        file.write(f'{count}\n')
    
    count += 1
    

    time.sleep(10)