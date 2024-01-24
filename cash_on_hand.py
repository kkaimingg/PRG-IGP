from pathlib import Path
import csv


def cash_on_hand_calculator():
    # create a file path to csv file
    fp = Path.cwd()/"Cash-on-Hand.csv"

    # read the csv file
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

    # create an empty list for cash on hand
        cash_on_hand=[]
    # append cash on hand into the cash_on_hand list
        for row in reader:
            #get the day and cash on hand for each day
            #and append to the cash_on_hand list
            cash_on_hand.append([int(row[0]), int(row[1])])
    

    #create list for cash deficit 
    cash_deficit = []

  

    # create list for highest cash surplus, putting day 11 values in first as the base
    highest_surplus = [cash_on_hand[0][0], 0]
    for i in range(1, len(cash_on_hand)):
        # calculate the surplus current day - previous day
        surplus = cash_on_hand[i][1] - cash_on_hand[i - 1][1]
        
        if surplus > 0:
            # check if surplus is higher than the set highest surplus
            if surplus > highest_surplus[1]:
                highest_surplus[0] = cash_on_hand[i][0]
                highest_surplus[1] = surplus
        else:
            # append cash deficit to cash deficit list
            cash_deficit.append([cash_on_hand[i][0], -surplus])
    print(cash_deficit)
    print(sorted(cash_deficit))
            
    # code to print results for scenario 1
    output = ""
    if not cash_deficit:
        output += "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"
        output += f"[HIGHEST CASH SURPLUS] DAY: {highest_surplus[0]}, AMOUNT: USD{highest_surplus[1]}\n"
    else:
        # swapping second element and first element place in the list to use .sort function row[0] -> row[1],  row[1] ->row[0]
        cash_deficit_swapped = [[item[1],item[0]] for item in cash_deficit]
        # sorting by highest amount to lowest amount
        cash_deficit_swapped.sort(reverse=True)

        # code to print results for scenario 2
        if not surplus:
            output += "[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY\n"
            output += f"[HIGHEST CASH DEFICIT] DAY :{cash_deficit_swapped[0][1]}, AMOUNT: USD{cash_deficit_swapped[0][0]}\n"

        # code to print results for scenario 3
        else:
            for deficit in cash_deficit:
                output += f"[CASH DEFICIT] DAY: {deficit[0]}, AMOUNT: USD{deficit[1]}\n"

            # print results for top 3 highest cash deficit
            output += f"[HIGHEST CASH DEFICIT] DAY :{cash_deficit_swapped[0][1]}, AMOUNT: USD{cash_deficit_swapped[0][0]}\n"
            output += f"[2ND HIGHEST CASH DEFICIT] DAY:{cash_deficit_swapped[1][1]}, AMOUNT: USD{cash_deficit_swapped[1][0]}\n"
            output += f"[3RD HIGHEST CASH DEFICIT] DAY: {cash_deficit_swapped[2][1]}, AMOUNT: USD{cash_deficit_swapped[2][0]}\n"
    
    
    return output
print(cash_on_hand_calculator())



        







