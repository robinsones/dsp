Challenge 1

What customers are from the UK?


> Query:  
> SELECT CustomerName FROM [Customers] where Country='UK'  

> Answer:  
> Around the Horn, B's Beverages, Consolidated Holdings, Eastern Connection, Island Trading, North/South, Seven Seas Imports  

Challenge 2  

What is the name of the customer who has the most orders?
> Query:  
> SELECT Orders.CustomerID, count(OrderID) as count, CustomerName FROM [Orders] JOIN Customers ON Orders.CustomerID=Customers.CustomerID GROUP BY Orders.CustomerID ORDER BY count DESC LIMIT 1;  

> Answer:  
> Ernst Handel


Challenge 3

What supplier has the highest average product price?
> Query:  
> SELECT avg(Price) as avg, Products.SupplierID, Suppliers.SupplierName FROM Products JOIN Suppliers on Products.SupplierID=Suppliers.SupplierID GROUP BY Products.SupplierID ORDER BY avg DESC LIMIT 1  

> Answer:  
> Aux joyeux ecclesiastiques

Challenge 4

How many different countries are their customers from? (Hint: Consider DISTINCT.)
> Query:  
> Select count(DISTINCT(Country)) FROM Orders JOIN OrderDetails ON Orders.OrderID=OrderDetails.OrderID JOIN Customers ON Orders.CustomerId = Customers.CustomerID WHERE ProductID=38 or ProductID=39  

> Answer: 
> 9

Challenge 5

What category appears the most in order details?**
> Query:  
> Select count(Products.CategoryID) as ct, CategoryName from OrderDetails JOIN Products on OrderDetails.ProductID=Products.ProductID Join Categories on Products.CategoryID=Categories.CategoryID Group By Products.CategoryID ORDER BY ct DESC LIMIT 1

> Answer:  
> Dairy products

Challenge 6

What was the total cost for each order?
> Query:  
> SELECT Quantity*Price, Orders.OrderID from Orders Join OrderDetails on Orders.OrderID=OrderDetails.OrderID Join Products on OrderDetails.ProductID=Products.ProductID GROUP BY Orders.OrderID

Challenge 7

What employee made the most sales (by total cost)?
> Query:  
> SELECT Orders.EmployeeID, FirstName, LastName, Quantity*Price as cost FROM  Orders JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID JOIN Products ON OrderDetails.ProductID=Products.ProductID JOIN Employees on Orders.EmployeeID=Employees.EmployeeID GROUP BY Orders.EmployeeID ORDER BY cost DESC

> Answer: 
> Margaret Peacock

Challenge 8

What employees have BS degrees? (Hint: Look at the LIKE operator.)
> Query:  
> SELECT FirstName, LastName FROM [Employees] WHERE Notes like '%BS%'

> Answer: 
> Janet Leverling, Steven Buchanan

Challenge 9

What supplier of three or more products has the highest average product price? (Hint: Look at the HAVING operator.)
> Query:  
> SELECT avg(Price) as avg, Products.SupplierID, SupplierName FROM Products JOIN Suppliers ON Products.SupplierID=Suppliers.SupplierID GROUP BY Products.SupplierID having count(ProductID) > 3 ORDER BY avg DESC LIMIT 1

>Answer:  
> Plutzer Lebensmittelgrobmarkte AG
