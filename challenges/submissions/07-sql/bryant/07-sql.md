# Challenge 1
* What customers are from the UK?

```sql
SELECT CustomerName
FROM Customers
WHERE Country = 'UK';
```

|Answer|
|---------------------|
|Around the Horn|
|B's Beverages|
|Consolidated Holdings|
|Eastern Connection|
|Island Trading|
|North/South|
|Seven Seas Imports|

# Challenge 2
* What is the name of the customer who has the most orders?
```sql
SELECT c.CustomerName
FROM Orders as o, Customers as c 
WHERE c.CustomerID = o.CustomerID 
GROUP BY o.CustomerID 
ORDER BY count(o.CustomerID)
DESC LIMIT 1;
```
|Answer|
|---------------------|
|Ernst Handel|

# Challenge 3
* What supplier has the highest average product price?

# Challenge 4
* How many different countries are their customers from? (Hint: Consider DISTINCT.)

# Challenge 5
* What category appears the most in order details?

# Challenge 6
* What was the total cost for each order?

# Challenge 7
* What employee made the most sales (by total cost)?

# Challenge 8
* What employees have BS degrees? (Hint: Look at the LIKE operator.)

# Challenge 9
* What supplier of three or more products has the highest average product price? (Hint: Look at the HAVING operator.)
