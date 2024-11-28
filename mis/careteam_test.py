# this script is used to test the careteam types update  
# Giving a init number which is 1000 keep generating the random number between 1 - 100  and reduce it . Until 1000 meets 0 the process stopped 

import random  
import time  

init_row_count = 1000
new_init_row_count = 0 


while init_row_count != new_init_row_count :
    print(f"start to update table with {init_row_count} records")
    time.sleep(1)
    new_init_row_count = random.randint(0,init_row_count)
    print(f"updated {new_init_row_count} records")
    init_row_count -= new_init_row_count
    print(f"after updating {init_row_count} rows remined")
    
       
       
print(f'update finished result are :{init_row_count}, {new_init_row_count}')
    
    