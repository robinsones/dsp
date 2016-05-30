# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

> Tuples and lists are similar because both are sequences of values indexed by integers. The big difference between lists and tuples is that tuples are immutable. This means that you can't modify elements of a tuple. Only tuples will work as keys in dictionaries, because lists are mutable. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

> Both sets and lists are collections of elements, but sets cannot contain duplicate elements and are unordered, while lists can have duplicates are ordered. 

``` 
S_NYC16_Metis_Staff = set(['Julia', 'Michael', 'Reshama', 'Megan', 'Jennifer', 'Leah'])
'Jason' not in  S_NYC16_Metis_Staff
S_NYC16_Metis_Students = ['Emily', 'Adam', 'Michelle']
S_NYC16_Metis_Students.append('Max')
print S_NYC16_Metis_Students
```

> Checking for the existence of an item is significantly faster in sets than lists. This is because the whole list needs to be searched for the item, so as the list size increases so does the serach time. On the other hand, for checking if an item is in a set, because sets are implemented using hash tables, the operation checks if the object is in the position determined by its hash, and thus does not depend on the size of the set. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

> `lambda` generates a (temporary) anonymous function, meaning a function without a name. It's useful for creating simple functions that we only need to use once, as it makes the code more readable. It's very helpful used in combination with `map`, `reduce`, and `filter`, which all take a list and a function. For example: 

```
li = [2, 4, 5, 10, 25, 60]
print filter(lambda x: x % 2 == 0, li) 
``` 

will print [2, 4, 10, 60], all the elements of the list divisable by 2. 

Another example, where I sort a list of fast food places and their menu items and price:

```
fast_food_tuples = [('Chick-Fil-A', 'Chicken Sandwich', 3.3), ('McDonalds', 'Fries', 1.4), ('Dairy Queen', 'Blizzard', 3.7),]
sorted(fast_food_tuples, key = lambda fast_food: fast_food[2]) # sort by price
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





