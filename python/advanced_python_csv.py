# Create csv file from emails
import pandas as pd
import numpy
# read file as dataframe
faculty = pd.read_csv('/users/emilyrobinson/Dropbox/metis/prework/dsp/python/faculty.csv')

# get emails
emails = faculty[' email'].tolist()

# create csv file from emails

import csv
resultFile = open("emails.csv",'wb')
wr = csv.writer(resultFile, dialect='excel')
for item in emails:
     wr.writerow([item, ])
