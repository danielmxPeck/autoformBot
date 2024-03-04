import openpyxl
import time
import string

workbook = openpyxl.load_workbook('/Users/dpmx/Desktop/testSelenium/DummyData.xlsx' )
worksheet = workbook['Sheet1']

cell_alpabet = 'A'
cell_num=2

#CHECKING IF CELL IS EMPTY AND COUNT IT WITH CELL_NUM
# while True:
#     cell_value = worksheet['A' + str(cell_num)].value
#     if cell_value is not None:
#         cell_num +=1
#         time.sleep(1)
#         print(cell_value)
#     else:
#         break
# print(cell_num) 


#Reading cell 



# Iterate through columns



# # Close the workbook
# workbook.close()

