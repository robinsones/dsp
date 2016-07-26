**Challenge 1**

**Question**: What customers are from the UK?

**SQL Query**
 
SELECT CustomerName FROM Customers  
WHERE Country = "UK";

**Answer**

Around the Horn  
B's Beverages  
Consolidated Holdings  
Eastern Connection  
Island Trading  
North/South  
Seven Seas Imports  

**Challenge 2**

**Question**: What is the name of the customer who has the most orders?

**SQL Query**

SELECT Orders.CustomerID, Customers.CustomerName, COUNT(*) as OrderTotal  
FROM Orders  
JOIN Customers ON Customers.CustomerID = Orders.CustomerID  
GROUP BY Orders.CustomerID  
ORDER BY OrderTotal DESC  
LIMIT 1;   

**Answer**
Ernst Handel	

**Challenge 3**

What supplier has the highest average product price?

**SQL Query**

**Answer**

**Challenge 4**

How many different countries are their customers from? (Hint: Consider DISTINCT.)
**SQL Query**

**Answer**

**Challenge 5**

What category appears in the most orders?
**SQL Query**

**Answer**

**Challenge 6**

What was the total cost for each order?

**SQL Query**

**Answer**

**Challenge 7**

What employee made the most sales (by total cost)?

**SQL Query**

**Answer**

**Challenge 8**

What employees have BS degrees? (Hint: Look at the LIKE operator.)

**SQL Query**

**Answer**

**Challenge 9**

What supplier of three or more products has the highest average product price? (Hint: Look at the HAVING operator.)

**SQL Query**

**Answer**

