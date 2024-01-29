import cash_on_hand 
import overheads
import Profit_Loss


max_overhead_category , max_overheads = overheads.overheads_finder()
deficit_days_and_amount = Profit_Loss.list_of_netprofit_deficit()
cash_deficit , surplus , highest_surplus = cash_on_hand.cash_on_hand_calculator()

from pathlib import Path
# create a path object for my text file
file_path = Path.cwd()/"summary_report.txt" 

# create the file if it doesn't exist 
file_path.touch() 

with file_path.open(mode = "w" , encoding="UTF-8") as file: 
    
    # write results to summary_report.txt 
    with open('summary_report.txt', 'w') as file: 

        file.write(f"[HIGHEST OVERHEAD] {max_overhead_category}: {max_overheads}%\n")
    
        output = ""
        if not cash_deficit:
            file.write ("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
            file.write (f"[HIGHEST CASH SURPLUS] DAY: {highest_surplus[0]}, AMOUNT: SGD{highest_surplus[1]}\n")
        else:
            # swapping second element and first element place in the list to use .sort function row[0] -> row[1],  row[1] ->row[0]
            cash_deficit_swapped = [[item[1],item[0]] for item in cash_deficit]
            # sorting by highest amount to lowest amount
            cash_deficit_swapped.sort(reverse=True)

            # code to print results for scenario 2 so we can check
            if not surplus:
                file.write ("[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY\n")
                file.write (f"[HIGHEST CASH DEFICIT] DAY :{cash_deficit_swapped[0][1]}, AMOUNT: SGD{cash_deficit_swapped[0][0]}\n")

            # code to print results for scenario 3 so we can check
            else:
                for deficit in cash_deficit:
                    file.write (f"[CASH DEFICIT] DAY: {deficit[0]}, AMOUNT: SGD{deficit[1]}\n")

                # print results for top 3 highest cash deficit
                file.write (f"[HIGHEST CASH DEFICIT] DAY :{cash_deficit_swapped[0][1]}, AMOUNT: SGD{cash_deficit_swapped[0][0]}\n")
                file.write (f"[2ND HIGHEST CASH DEFICIT] DAY:{cash_deficit_swapped[1][1]}, AMOUNT: SGD{cash_deficit_swapped[1][0]}\n")
                file.write (f"[3RD HIGHEST CASH DEFICIT] DAY: {cash_deficit_swapped[2][1]}, AMOUNT: SGD{cash_deficit_swapped[2][0]}\n")
        
        for day, amount in deficit_days_and_amount: 
            file.write(f"[NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{amount}\n")

        for rank, (day, amount) in enumerate (deficit_days_and_amount[:3]): 
            if rank == 0:
                file.write(f"[HIGHEST NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{amount}\n")
            elif rank == 1 :
                file.write(f"[2ND HIGHEST NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{amount}\n")
            elif rank == 2:
                file.write(f"[3RD HIGHEST NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{amount}\n")   
            