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

SELECT Products.SupplierID, Suppliers.SupplierName, AVG(Price) as AveragePrice FROM Products   
JOIN Suppliers ON Suppliers.SupplierID = Products.SupplierID  
GROUP BY Products.SupplierID   
ORDER BY AveragePrice DESC  
LIMIT 1  

**Answer**

Aux joyeux ecclésiastiques	

**Challenge 4**

How many different countries are their customers from? (Hint: Consider DISTINCT.)

**SQL Query**
SELECT COUNT(DISTINCT Country) FROM  [Customers]  

**Answer**
21

**Challenge 5**

What category appears in the most orders?

**SQL Query**


**Answer**


**Challenge 6**

What was the total cost for each order?

**SQL Query**
SELECT SUM(ProductID * Quantity) as OrderCost, OrderID FROM [OrderDetails]
GROUP BY OrderID;

**Answer**
A long table

**Challenge 7**

What employee made the most sales (by total cost)?

**SQL Query**

SELECT SUM(Price * Quantity) as TotalSales, Employees.EmployeeID, FirstName FROM Orders  
JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID  
JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID  
JOIN Products ON Products.ProductID = OrderDetails.ProductID  
GROUP BY Employees.EmployeeID  
ORDER BY TotalSales DESC  
LIMIT 1; 

**Answer**
Margaret Peacock

**Challenge 8**

What employees have BS degrees? (Hint: Look at the LIKE operator.)

**SQL Query**

SELECT * FROM Employees  
WHERE Notes LIKE "%BS%";

**Answer**
Janet Leverling and Steven Buchanan

**Challenge 9**

What supplier of three or more products has the highest average product price? (Hint: Look at the HAVING operator.)

**SQL Query**

SELECT AVG(Price) as AveragePrice, Products.SupplierID, SupplierName, COUNT(*) as NumProducts FROM Products  
JOIN Suppliers ON Products.SupplierID = Suppliers.SupplierID  
GROUP BY Products.SupplierID  
HAVING 3 <= NumProducts  
ORDER By AveragePrice DESC  
LIMIT 1;

**Answer**
Tokyo Traders

