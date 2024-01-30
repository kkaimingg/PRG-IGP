import cash_on_hand 
import overheads_module
import Profit_Loss

max_overhead_category , max_overheads = overheads_module.overheads_finder()
deficit_days_and_amount = Profit_Loss.list_of_netprofit_deficit()
cash_deficit , surplus , highest_surplus = cash_on_hand.cash_on_hand_calculator()

def main():
    
    overheads_module.overheads_append_file(max_overhead_category,max_overheads)
    cash_on_hand.cash_on_hand_append_file(cash_deficit, surplus, highest_surplus)
    Profit_Loss.profit_loss_append_file(deficit_days_and_amount)

main()

           