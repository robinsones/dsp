#### Q1

# import faculty file
import pandas as pd
import numpy
# read file as dataframe
faculty = pd.read_csv('/users/emilyrobinson/Dropbox/metis/prework/dsp/python/faculty.csv')
faculty
# column "degree" has all degrees. Sometimes there are different notations for same degree (e.g. Ph.D. versus PhD). Some people have multiple degrees
# make a list of all degrees
degrees = faculty[' degree'].tolist()
# remove "." to fix formatting  
degrees_nodots = [i.replace(".", "") for i in degrees]
# split strings where a space (to separate multiple degrees) and make one list again
degrees_split = [i.split() for i in degrees_nodots]
degrees_onelist = [item for sublist in degrees_split for item in sublist] 
# Count occurances of each type of degree
from collections import Counter
Counter(degrees_onelist)


