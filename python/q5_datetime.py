# Hint:  use Google to find python function

from datetime import datetime

# I define a function to get the difference between two dates when given the format of the dates
def date_dif(date_start, date_stop, date_format):
    # this function returns the difference between two dates
    a = datetime.strptime(date_start, date_format)
    b = datetime.strptime(date_stop, date_format)
    delta = b - a
    return delta.days

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   
date_format = "%m-%d-%Y"
date_dif(date_start, date_stop, date_format)
# 937

####b)  
date_start = '12312013'  
date_stop = '05282015'  
date_format = "%m%d%Y"
date_dif(date_start, date_stop, date_format)
# 513

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
date_format = "%d-%b-%Y"
date_dif(date_start, date_stop, date_format)
# 7850
