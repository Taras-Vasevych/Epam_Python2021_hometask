"""
Task 2_3

You are given n bars of gold with weights: w1, w2, ..., wn and bag with capacity W.
There is only one instance of each bar and for each bar you can either take it or not
(hence you cannot take a fraction of a bar). Write a function that returns the maximum weight of gold that fits
into a knapsack's capacity.

The first parameter contains 'capacity' - integer describing the capacity of a knapsack
The next parameter contains 'weights' - list of weights of each gold bar
The last parameter contains 'bars_number' - integer describing the number of gold bars
Output : Maximum weight of gold that fits into a knapsack with capacity of W.

Note:
Use the argparse module to parse command line arguments. You don't need to enter names of parameters (i. e. -capacity)
Raise ValueError in case of false parameter inputs
Example of how the task should be called:
python3 task3_1.py -W 56 -w 3 4 5 6 -n 4
"""
"""
Created by Taras Vasevych
"""



import argparse

def bounded_knapsack(max_weight, bars, num_of_bars):
    """
    Checks if data has physical meaning, sorts list of bars for convinient calculation
    and returns max weight what is equal or less then backpack capacity
    """
    bars.sort()
    
    if bars[0] <= 0 or \
    len(bars) != num_of_bars or \
    num_of_bars == 0 or \
    max_weight <=0 : 
        raise ValueError
    
    pos_weight = [False] * (max_weight + 1)
    pos_weight[0] = True
    
    for bar in bars:
        temp_list = pos_weight.copy()
        for i in range(bar, max_weight+1):
            if pos_weight[i-bar] == True:
                temp_list[i] = True
        pos_weight = temp_list
        
    for i in range(max_weight, -1, -1):
        if pos_weight[i]: return i
    


def main():
    """
    Takes arguments from a command line for task, 
    call bounded_knapsack and print result 
    """
    
    parser = argparse.ArgumentParser(description='Knapsack arguments')
    parser.add_argument('-W', type=int, help='Weight capacity')
    parser.add_argument('-w', nargs='*', type=int, help='Space-separated list of weights of bars')
    parser.add_argument('-n', type=int, help='Number of bars')
    args = parser.parse_args()
    max_weight = args.W
    bars = args.w
    num_of_bars = args.n
    
    print(bounded_knapsack(max_weight, bars, num_of_bars))


if __name__ == '__main__':
    main()
