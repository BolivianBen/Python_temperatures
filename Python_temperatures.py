#Benjamin Holman, SPC ID 2371353
'''
Since program requires two functions, make
the converter function first. import random.
define a function that converts celsius to Fahren.
use random to obtain range of 50 ints between -40 and 40.
use built in function to dermine high and low temps and
display them for the user.
determine if 0c is found in teh list, if it is, display
which index, if not display its not found.
create a second list of 10 temps that are then sorted
create a loop to convert each temp into farhenheit.
create headers for the Celsius and Fahrenheit.
set variables at 0 to determine the average
add up the 10 temperatures and then determine
average.
Display all information for user.

'''

import random as ran

def CtoF(celsius):
    fahren = []
    for i in celsius:
        x = (i * 1.8) + 32
        fahren.append(x)
    return fahren

def main():

    temps = [ran.randint(-40,40) for i in range(50)]

    low = min (temps)
    hi = max(temps)
    print(f'Lowest temp is {low} and highest is {hi}')
    
    if 0 in temps:
        loc = temps.index(0)
        print(f'Found 0c at index {loc}')
    else:
        print('0C is not in the list')

    cel = []
    x = ran.randint(-40,40)
    for i in range(10):
        while x in cel:
            x = ran.randint(-40,40)
        cel.append(x)
    cel.sort()
    print('Sorted sample of ten equivalent temperatures')

    fahrenheit = CtoF(cel)
    print("CELSIUS\t  FAHRENHEIT")
    sum1 = 0
    sum2 = 0
    for i in range(10):
        sum1 = sum1 + cel[i]
        sum2 = sum2 + fahrenheit[i]
        convert = fahrenheit[i]
        print(f'{cel[i]} \t  {convert:.1f}')
    print()
    print(f'{sum1/10:.1f} \t  {sum2/10:.1f} \t <--- averages')

main()
