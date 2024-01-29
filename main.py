import cash_on_hand , overheads , Profit_Loss  

def main(): 

    cash_on_hand.cash_on_hand_calculator()


# from pathlib import Path
# # create a path object for my text file
# file_path = Path.cwd()/"paymentSummary.txt" 

# with file_path.open(mode = "w" , encoding="UTF-8") as file: 
#  file.write("PowerLeopard payment summary\n====================================\nDriver ID, Total Sales, Total Earnings, Sales to earning ratio\n")

# # define the file path for my payment summary 
# file_path = Path.cwd()/"paymentSummary.txt" 
 
# # create the file if it doesn't exist 
# file_path.touch() 
 
# # open the file in write mode and set encoding to UTF-8 
# with file_path.open(mode = "w" , encoding="UTF-8") as file: 
#     file.write("PowerLeopard Payment Summary\n============================\nDriver ID,Total Sales,Total Earning,Sales to Earning Ratio\n") 

# # iterate through each DriverID and use .write function to write information into the file by using f strings. 
#     for DriverID, data in driverData.items():
#         earnings = data["Earnings"]
#         sales = data["Sales"]
#         ratio = sales / earnings
#         file.write(f"{DriverID},{sales:.2f},{earnings:.2f},{ratio:.2f}\n")