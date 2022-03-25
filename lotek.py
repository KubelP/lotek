'''
Import random module to generate six random numbers
'''
import random
import time


my_numbers = []
while len(my_numbers) < 6:
  my_number = int(input('Podaj szczesliwe liczby '))
  my_numbers.append(my_number)

my_numbers_set = set(my_numbers) 
print(my_numbers_set)

random_numbers = set()

time1 = time.time()

if __name__ == '__main__':
    def rand_int():
        '''writing the loop which generates six random numbers'''
        while len(random_numbers) < 6:
            i = random.randint(1, 50)
            random_numbers.add(i)
        return random_numbers

    COUNTER = 0 # count of draws
    while random_numbers !=  my_numbers_set:
        random_numbers = set() # clear generated set
        random_numbers = rand_int()
        COUNTER +=1
        
    time2 = time.time()

    elapsed_time = time2 - time1
    
    print('YOU WIN on ', COUNTER, 'time which cost you', 3*COUNTER, ' and took '
        , int(COUNTER/54), 'years', 'elapsed time of drawings: ', round(elapsed_time/60, 2))
