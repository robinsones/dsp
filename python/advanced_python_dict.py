### Q6

import pandas as pd
# read file as dataframe
faculty = pd.read_csv('/users/emilyrobinson/Dropbox/metis/prework/dsp/python/faculty.csv')

# create faculty dictionary where key is last name, values are list with degree, title, and email

# first we make name column only last name
names = faculty['name'].tolist()
lastnames = [name.rsplit(None, 1)[-1] for name in names]

# then we make lists for degrees, titles, and emails and combine into one list
degrees = faculty[' degree'].tolist()
titles = faculty[' title'].tolist()
emails = faculty[' email'].tolist()
values = []
for i in range(0, len(emails)):
    values.append([degrees[i], titles[i], emails[i]])

# I can't just zip a dictionary because of duplicte keys. So I do a workaround
faculty_dict = {}
for i, j in zip(lastnames, values):
    faculty_dict.setdefault(i, []).append(j)

print faculty_dict

### Q7

# drop initials
no_initials = []
for name in names: 
    no_initials.append(' '.join(word for word in name.split() if len(word)>1 and '.' not in word))
    
# create name tuples of first and last name.
name_tuples = [(name.split(' ', 1)[0], name.rsplit(None, 1)[-1]) for name in no_initials]
# values is the same
# Won't have problem of duplicate

professor_dict = dict(zip(name_tuples, values))
professor_dict

### Q8 

# print based on alphabetical order last name of professor
for key in sorted(professor_dict, key = lambda x: x[1]):
    print "%s: %s" % (key ,professor_dict[key])
