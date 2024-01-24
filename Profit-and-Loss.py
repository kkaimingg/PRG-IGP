from pathlib import Path
import csv

# create a file path to csv file.
fp = Path.cwd()/"profit-and-loss-sgd.csv"

# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list for profit and loss
    ProfitAndLoss =[] 

    # append profit-and-loss-sgd into the Profit_and_Loss list
    for row in reader:
        #get the day and net profit
        #and append to the Profit_and_Loss list
        row [0]= int (row[0])
        row [4]= int (row[4])
        ProfitAndLoss.append([row[0], row[4]])

def list_of_netprofit_deficit (ProfitAndLoss): 
    '''
    - the function takes in the list of the profit and loss 
    - the function returns the list of the days where there were the net profit deficit and the amount 
    '''
    deficit_days_and_amount = []

    for Current_Day , (day, net_profit) in enumerate (ProfitAndLoss):
        # to skip the first iteration of the loop which is day 0
        if Current_Day > 0:
            prev_day, prev_net_profit = ProfitAndLoss[Current_Day - 1] # to substract from the previous sublist

            # check if there was a net profit deficit 
            if prev_net_profit > net_profit: 
                deficit_days_and_amount.append([day, prev_net_profit - net_profit])
   
    # print out the days and amount for each deficit
        for day, amount in sorted(deficit_days_and_amount): 
            print(f"[NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{amount}")

    # iterate from 1 and to iterate through the list of deficit days and amounts
    for sequence in range(1, len(deficit_days_and_amount)): 
        # inner loop to compare the 2 adjacent elements in each iteration
        for sequence2 in range(len(deficit_days_and_amount)-sequence):
            # check if the current amount is less than the previous amount in the net profit deficit list
            if deficit_days_and_amount [sequence2][1] < deficit_days_and_amount [sequence2+1][1]:
                # the positions of the sublist will be swapped if it is true
                deficit_days_and_amount[sequence2], deficit_days_and_amount[sequence2+1] = deficit_days_and_amount [sequence2+1], deficit_days_and_amount[sequence2]

    # rank variable keeps track of which iteration we are on, starting from 0 
    for rank, (day, amount) in enumerate (deficit_days_and_amount): 
        if rank == 0:
            print(f"[HIGHEST NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{amount}")
        elif rank == 1 :
            print (f"[2ND HIGHEST NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{amount}")
        elif rank == 2:
            print (f"[3RD HIGHEST NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{amount}")

# call the function to get the deficit_days_and_amount list
list_of_netprofit_deficit(ProfitAndLoss)