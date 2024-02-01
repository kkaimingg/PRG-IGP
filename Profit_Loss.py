from pathlib import Path
import csv

# create a file path to csv file.


def list_of_netprofit_deficit (): 

    fp = Path.cwd()/"csv_reports" / "profit-and-loss-sgd.csv"

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

    return(deficit_days_and_amount)
# call the function to get the deficit_days_and_amount list
list_of_netprofit_deficit()

def write_profit_loss(deficit_days_and_amount, file):
    for day, amount in deficit_days_and_amount: 
                file.write(f"[NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{amount}\n")

    for sequence in range(1, len(deficit_days_and_amount)):
    #to ensure the inner loop iterates over the remaining part of the list
        for sequence2 in range(len(deficit_days_and_amount)-sequence):
            # check if the current amount is larger than the previous amount in the net profit deficit list
            if deficit_days_and_amount [sequence2][1] < deficit_days_and_amount [sequence2+1][1]:
                # the positions of the sublist will be swapped if it is true
                deficit_days_and_amount[sequence2], deficit_days_and_amount[sequence2+1] = deficit_days_and_amount [sequence2+1], deficit_days_and_amount[sequence2]

    for rank, (day, amount) in enumerate (deficit_days_and_amount[:3]): 
        if rank == 0:
            file.write(f"[HIGHEST NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{amount}\n")
        elif rank == 1 :
            file.write(f"[2ND HIGHEST NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{amount}\n")
        elif rank == 2:
            file.write(f"[3RD HIGHEST NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{amount}\n")   

def profit_loss_append_file(deficit_days_and_amount):

    file_path = Path.cwd() / "summary_report.txt"

    # Check if the file exists
    if file_path.exists():
        # If the file exists, open it in append mode
        with file_path.open(mode="a", encoding="UTF-8") as file:
            write_profit_loss(deficit_days_and_amount, file)
    else:
        # If the file does not exist, create it using touch() and write the results
        file_path.touch()
        with file_path.open(mode="w", encoding="UTF-8") as file:
           write_profit_loss(deficit_days_and_amount, file)
        


# print out the days and amount for each deficit for checking purposes
    # for day, amount in deficit_days_and_amount: 
    #     print(f"[NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{amount}")

    # # iterate from 1 and to iterate over the indices of deficit_days_and_amount sequence
    # for sequence in range(1, len(deficit_days_and_amount)):
    #     # to ensure the inner loop iterates over the remaining part of the list
    #     for sequence2 in range(len(deficit_days_and_amount)-sequence):
    #         # check if the current amount is larger than the previous amount in the net profit deficit list
    #         if deficit_days_and_amount [sequence2][1] < deficit_days_and_amount [sequence2+1][1]:
    #             # the positions of the sublist will be swapped if it is true
    #             deficit_days_and_amount[sequence2], deficit_days_and_amount[sequence2+1] = deficit_days_and_amount [sequence2+1], deficit_days_and_amount[sequence2]

    # for rank, (day, amount) in enumerate (deficit_days_and_amount[:3]): 
    #     if rank == 0:
    #         print(f"[HIGHEST NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{amount}")
    #     elif rank == 1 :
    #         print (f"[2ND HIGHEST NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{amount}")
    #     elif rank == 2:
    #         print (f"[3RD HIGHEST NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{amount}")
