## Challenge Set 7
Topic: SQL Challenges  
Date: 07/30/2016  
Name: Kevin Cole  

## Challenge 1  

What customers are from the UK?

SELECT CustomerName  
FROM customers  
WHERE Country = "UK";

CustomerName  
Around the Horn  
B's Beverages  
Consolidated Holdings  
Eastern Connection  
Island Trading  
North/South  
Seven Seas Imports

## Challenge 2

What is the name of the customer who has the most orders?

SELECT CustomerName, COUNT(*)  
FROM Orders  
INNER JOIN Customers  
ON Orders.CustomerID = Customers.CustomerID  
GROUP BY Orders.CustomerID  
ORDER BY COUNT(*) DESC  
LIMIT 1;

CustomerName	COUNT(*)  
Ernst Handel	10

## Challenge 3  

What supplier has the highest average product price?

SELECT SupplierName, AVG(PRICE)  
FROM Products  
INNER JOIN Suppliers  
ON Products.SupplierID = Suppliers.SupplierID  
GROUP BY Products.SupplierID  
ORDER BY AVG(Price) DESC  
LIMIT 1;

SupplierName	            AVG(PRICE)  
Aux joyeux ecclésiastiques	140.75

## Challenge 4

How many different countries are their customers from? (Hint: Consider DISTINCT.)

SELECT COUNT(DISTINCT(Country))  
FROM Customers;

COUNT(DISTINCT(Country))  
21

## Challenge 5

What category appears the most in order details?

SELECT CategoryName, COUNT(CategoryName)  
FROM OrderDetails  
INNER JOIN Products  
ON OrderDetails.ProductID = Products.ProductID  
INNER JOIN Categories  
ON Products.CategoryID = Categories.CategoryID  
ORDER BY COUNT(CategoryName) DESC  
LIMIT 1;


CategoryName	COUNT(CategoryName)  
Produce	        518

## Challenge 6

What was the total cost for each order?

SELECT OrderID, Quantity*Price  
FROM OrderDetails  
INNER JOIN Products  
ON OrderDetails.ProductID = Products.ProductID

OrderID	Quantity*Price  
10248	252  
10248	140  
10248	174  
10249	209.25  

## Challenge 7

What employee made the most sales (by total cost)?

SELECT LastName, FirstName, SUM(Quantity*Price)  
FROM Employees  
INNER JOIN Orders  
ON Employees.EmployeeID = Orders.EmployeeID  
INNER JOIN OrderDetails  
ON Orders.OrderID = OrderDetails.OrderID  
INNER JOIN Products  
ON OrderDetails.ProductID = Products.ProductID  
GROUP BY Employees.EmployeeID  
ORDER BY SUM(Quantity*Price) DESC  
LIMIT 1;

LastName	FirstName	SUM(Quantity*Price)  
Peacock	    Margaret	105696.49999999999

## Challenge 8

What employees have BS degrees? (Hint: Look at the LIKE operator.)

SELECT LastName, FirstName  
FROM Employees  
WHERE Notes LIKE '%BS%';


LastName	FirstName  
Leverling	Janet  
Buchanan	Steven

## Challenge 9

What supplier of three or more products has the highest average product price? (Hint: Look at the HAVING operator.)

SELECT SupplierName, AVG(PRICE)   
FROM Products  
INNER JOIN Suppliers  
ON Products.SupplierID = Suppliers.SupplierID  
GROUP BY Products.SupplierID HAVING COUNT(*) > 3  
ORDER BY AVG(Price) DESC  
LIMIT 1;

SupplierName	                    AVG(PRICE)  
Plutzer Lebensmittelgroßmärkte AG	44.678000000000004

