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

### Q2

# make a list of all titles
titles = faculty[' title'].tolist()
Counter(titles)
# there's a typo, so there's only three types, icluding additional assistant

### Q3
# make a list of all titles
emails = faculty[' email'].tolist()
print emails

### Q4 

# retrieve domain for each email
domains = []
for email in emails: 
    match = re.search('([\w.-]+)@([\w.-]+)', email)
    domains.append(match.group(2) ) 

# print list of unique emails
print list(set(domains))


