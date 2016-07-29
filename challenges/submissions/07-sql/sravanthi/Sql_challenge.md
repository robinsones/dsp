### SQL Challenges



---

**Challenge 0 - Practice Example**

What customers are from Sweden?

```sql
SELECT * FROM Customers WHERE Country='Sweden';
```

>Berglunds snabbköp  	Christina Berglund  
Folk och fä HB  	Maria Larsson   

---

**Challenge 1**

What customers are from the UK?

>> SELECT * FROM [Customers] where Country = 'UK'
Number of Records: 7
CustomerID
CustomerName
ContactName
Address
City
PostalCode
Country
4
Around the Horn
Thomas Hardy
120 Hanover Sq.
London
WA1 1DP
UK
11
B's Beverages
Victoria Ashworth
Fauntleroy Circus
London
EC2 5NT
UK
16
Consolidated Holdings
Elizabeth Brown
Berkeley Gardens 12 Brewery
London
WX1 6LT
UK
19
Eastern Connection
Ann Devon
35 King George
London
WX3 6FW
UK
38
Island Trading
Helen Bennett
Garden House Crowther Way
Cowes
PO31 7PJ
UK
53
North/South
Simon Crowther
South House 300 Queensbridge
London
SW7 1RZ
UK
72
Seven Seas Imports
Hari Kumar
90 Wadhurst Rd.
London
OX15 4NB
UK



**Challenge 2**

What is the name of the customer who has the most orders?


**Challenge 3**

What supplier has the highest average product price?


**Challenge 4**

How many different countries are their customers from? (Hint: Consider DISTINCT.)


**Challenge 5**

What category appears in the most orders?


**Challenge 6**

What was the total cost for each order?


**Challenge 7**

What employee made the most sales (by total cost)?


**Challenge 8**

What employees have BS degrees? (Hint: Look at the LIKE operator.)


**Challenge 9**

What supplier of three or more products has the highest average product price? (Hint: Look at the HAVING operator.)














---

If you like, you can also do [more](more.md).
