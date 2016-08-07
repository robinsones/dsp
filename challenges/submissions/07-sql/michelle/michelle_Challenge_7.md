# Challenge 7 SQL

Name: Michelle Gill  
Date: 2016/07/19  
Worked with: Emily on Question 7

## Question 1

What customers are from the UK?

```sql
SELECT * FROM Customers WHERE Country=='UK';
```

| CustomerID |  CustomerName |    ContactName | Address | City |    PostalCode |  Country |
| :--------:  | :-----------:  | :----------: | :-----: | :--: | :-----------: | :------: |
| 4 |   Around the Horn | Thomas Hardy |    120 Hanover Sq. | London |  WA1 1DP | UK |
| 11 |  B's Beverages |   Victoria Ashworth |   Fauntleroy Circus |   London |  EC2 5NT | UK |
| 16 | Consolidated Holdings |   Elizabeth Brown | Berkeley Gardens 12 Brewery | London |  WX1 6LT | UK |
| 19 |  Eastern Connection |  Ann Devon |   35 King George |  London |  WX3 6FW | UK |
| 38 |  Island Trading |  Helen Bennett |   Garden House Crowther Way |   Cowes |   PO31 7PJ |    UK |
| 53 |  North/South Simon Crowther |  South House | 300 Queensbridge |   London |  SW7 1RZ | UK |
| 72 |  Seven Seas Imports |  Hari Kumar |  90 Wadhurst Rd. | London |  OX15 4NB |    UK |

## Question 2

What is the name of the customer who has the most orders?

```sql
SELECT Customers.CustomerID, Customers.CustomerName, Orders.CustomerID, COUNT(Orders.CustomerID) AS 'NumOrders'
FROM Orders
INNER JOIN Customers 
ON Orders.CustomerID=Customers.CustomerID
GROUP BY Orders.CustomerID
ORDER BY NumOrders DESC;
```

| CustomerID | CustomerName  |  NumOrders |
| :--------: | :-----------: | :--------: |
| 20 | Ernst Handel  |  10

## Question 3

What supplier has the highest average product price?


```sql
SELECT Suppliers.SupplierID, Suppliers.SupplierName, Products.SupplierID, AVG(Products.Price) as 'AveragePrice'
FROM Suppliers
INNER JOIN Products
ON Suppliers.SupplierID=Products.SupplierID
GROUP BY Suppliers.SupplierID
ORDER BY AveragePrice DESC;
```

| SupplierID | SupplierName  |  AveragePrice |
| :--------: | :-----------: | :--------: |
| 18 | Aux joyeux ecclésiastiques | 140.75 |

## Question 4

How many different countries are their customers from? (Hint: Consider DISTINCT.)

```sql
WITH _table AS
(
SELECT Products.ProductID, Products.SupplierID, OrderDetails.ProductID, OrderDetails.OrderID, Orders.OrderID, Orders.CustomerID, Customers.CustomerID, Customers.Country
FROM Products
INNER JOIN OrderDetails
ON Products.ProductID==OrderDetails.ProductID
INNER JOIN Orders
ON OrderDetails.OrderID==Orders.OrderID
INNER JOIN Customers
ON Orders.CustomerID==Customers.CustomerID
WHERE Products.SupplierID==18
)
SELECT DISTINCT(Country) FROM _table;
```

Answer: Nine Countries

Brazil
Venezuela
France
USA
Germany
Austria
UK
Denmark
Canada


## Question 5

What category appears in the most orders?

```sql
SELECT Categories.CategoryName, COUNT(Categories.CategoryID) as Count
FROM OrderDetails
JOIN Products
JOIN Categories
ON OrderDetails.ProductID = Products.ProductID
AND Products.CategoryID = Categories.CategoryID
GROUP BY Categories.CategoryID
ORDER BY Count DESC
LIMIT 1;
```

| CategoryName  |   TotalOrders | 
| :-----------: | :------------: |
| Dairy Products  | 100 |


## Question 6

What was the total cost for each order?

```sql
WITH _table AS
(
SELECT OrderDetails.OrderID, OrderDetails.ProductID, Products.ProductID, Products.Price * OrderDetails.Quantity as Cost
FROM OrderDetails
INNER JOIN Products
ON OrderDetails.ProductID==Products.ProductID
)
SELECT OrderID, SUM(Cost) FROM _table
GROUP BY OrderID;
```

Top for orders are shown.  

| OrderID  |  SUM(Cost) |
| :------: | :--------: |
| 10248 |   566 |
| 10249 |  2329.25 |
| 10250 |   2267.25 |
| 10251 |   839.5 |

## Question 7

What employee made the most sales (by total cost)?

```sql
WITH _table AS
(
SELECT OrderDetails.OrderID, OrderDetails.ProductID, Products.ProductID, Orders.OrderID, Orders.EmployeeID, Employees.EmployeeID, Employees.FirstName, Employees.LastName, OrderDetails.Quantity * Products.Price as Cost
FROM OrderDetails
LEFT JOIN Products
ON Products.ProductID==OrderDetails.ProductID
LEFT JOIN Orders
ON OrderDetails.OrderID==Orders.OrderID
LEFT JOIN Employees
ON Orders.EmployeeID==Employees.EmployeeID
)
SELECT FirstName, LastName, SUM(Cost) as Total FROM _table
GROUP BY FirstName, LastName
ORDER BY Total DESC
LIMIT 1;
```

| FirstName  | LastName  |  Total |
| :--------: | :-----------: | :--------: |
| Margaret  |  Peacock | 105696.5 |


## Question 8

What employees have BS degrees? (Hint: Look at the LIKE operator.)

```sql
SELECT FirstName, LastName, Notes
FROM Employees
WHERE Notes LIKE '%bs%';
```

| FirstName |  LastName  |  Notes |
| :--------: | :-----------: | :--------: |
| Janet |  Leverling  | Janet has a BS degree in chemistry from Boston College). She has also completed a certificate program in food retailing management. Janet was hired as a sales associate and was promoted to sales representative. |
| Steven | Buchanan | Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree. Upon joining the company as a sales representative, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London, where he was promoted to sales manager. Mr. Buchanan has completed the courses 'Successful Telemarketing' and 'International Sales Management'. He is fluent in French. |

## Question 9

What supplier of three or more products has the highest average product price? (Hint: Look at the HAVING operator.)

```sql
SELECT Products.SupplierID, Suppliers.SupplierID, Suppliers.SupplierName, AVG(Products.Price) as MeanPrice
FROM Products
LEFT JOIN Suppliers
WHERE Products.SupplierID==Suppliers.SupplierID
GROUP BY Products.SupplierID
HAVING COUNT(Products.SupplierID) >= 3
ORDER BY MeanPrice DESC
LIMIT 1;
```

| SupplierID | SupplierName   | MeanPrice |
| :--------: | :-----------: | :--------: |
| 4  | Tokyo Traders  | 46 |
