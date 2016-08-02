# Challenge 7 SQL

Name: Michelle Gill  
Date: 2016/07/19  
Worked with: Emily on Quesiton 7

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
SELECT Customers.CustomerID |Customers.CustomerName |Orders.CustomerID |COUNT(Orders.CustomerID) AS 'NumOrders'
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
SELECT Suppliers.SupplierID | Suppliers.SupplierName | Products.SupplierID | AVG(Products.Price) as 'AveragePrice'
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
SELECT Products.ProductID | Products.SupplierID | OrderDetails.ProductID | OrderDetails.OrderID | Orders.OrderID | Orders.CustomerID | Customers.CustomerID | Customers.Country
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
WITH _table2 AS
(
WITH _table AS
(
SELECT OrderDetails.OrderID, Products.ProductID, Products.CategoryID, Categories.CategoryID, Categories.CategoryName
FROM OrderDetails 
JOIN Products ON OrderDetails.ProductID = Products.ProductID
JOIN Categories ON Categories.CategoryID = Products.CategoryID
)
SELECT OrderID, CategoryName FROM _table
GROUP BY OrderID, CategoryName
)
SELECT CategoryName, COUNT(*) as TotalOrders FROM _table2
GROUP BY CategoryName
ORDER BY TotalOrders DESC;
```


| CategoryName  |   TotalOrders | 
| :-----------: | :------------: |
| Beverages  |  80 |
| Confections | 78 |
| Dairy Products  | 76 |
| Seafood | 60  |
| Meat/Poultry    | 48 |
| Condiments  | 41 |
| Grains/Cereals  | 38 |
| Produce | 32 |

## Question 6

What was the total cost for each order?

```sql
WITH _table AS
(
SELECT OrderDetails.OrderID | OrderDetails.ProductID | Products.ProductID | Products.Price * OrderDetails.Quantity as Cost
FROM OrderDetails
INNER JOIN Products
ON OrderDetails.ProductID==Products.ProductID
)
SELECT OrderID | SUM(Cost) FROM _table
GROUP BY OrderID;
```

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
SELECT OrderDetails.OrderID | OrderDetails.ProductID | Products.ProductID | Orders.OrderID | Orders.EmployeeID | Employees.EmployeeID | Employees.FirstName | Employees.LastName | OrderDetails.Quantity * Products.Price as Cost
FROM OrderDetails
LEFT JOIN Products
ON Products.ProductID==OrderDetails.ProductID
LEFT JOIN Orders
ON OrderDetails.OrderID==Orders.OrderID
LEFT JOIN Employees
ON Orders.EmployeeID==Employees.EmployeeID
)
SELECT FirstName | LastName | SUM(Cost) as Total FROM _table
GROUP BY FirstName |LastName
ORDER BY Total DESC;
```

| FirstName  | LastName  |  Total |
| :--------: | :-----------: | :--------: |
| Margaret  |  Peacock | 105696.5 |
| Nancy |  Davolio  | 57690.39 |
| Janet |  Leverling  | 42838.35 |
| Robert  | King  |  39772.3 |
| Laura  | Callahan  |  39309.38 |
| Andrew  | Fuller |  32503.16 |
| Steven | Buchanan  |  27480.8 |
| Michael  | Suyama | 25399.25 |
| Anne  |  Dodsworth  | 15734.1 |

## Question 8

What employees have BS degrees? (Hint: Look at the LIKE operator.)

```sql
SELECT FirstName | LastName | Notes
FROM Employees
WHERE Notes LIKE '% BS %';
```

| FirstName |  LastName  |  Notes |
| :--------: | :-----------: | :--------: |
| Janet |  Leverling  | Janet has a BS degree in chemistry from Boston College). She has also completed a certificate program in food retailing management. Janet was hired as a sales associate and was promoted to sales representative. |

## Question 9

What supplier of three or more products has the highest average product price? (Hint: Look at the HAVING operator.)

```sql
SELECT Products.SupplierID | Suppliers.SupplierID | Suppliers.SupplierName | AVG(Products.Price) as MeanPrice
FROM Products
LEFT JOIN Suppliers
WHERE Products.SupplierID==Suppliers.SupplierID
GROUP BY Products.SupplierID
HAVING COUNT(Products.SupplierID) >= 3
ORDER BY MeanPrice DESC;
```

| SupplierID | SupplierName   | MeanPrice |
| :--------: | :-----------: | :--------: |
| 4  | Tokyo Traders  | 46 |
| 12 | Plutzer Lebensmittelgroßmärkte AG |  44.678000000000004 |
| 7  | Pavlova Ltd. |  35.57 |
| 3  | Grandma Kelly's Homestead |  31.666666666666668 |
| 24 | G'day Mate | 30.933333333333334 |
| 11 | Heli Süßwaren GmbH & Co. KG | 29.709999999999997 |
| 8  | Specialty Biscuits Ltd.  |  28.175 |
| 20 | Leka Trading  |  26.483333333333334 |
| 14 | Formaggi Fortini s.r.l. | 26.433333333333334 |
| 2  | New Orleans Cajun Delights | 20.35 |
| 15 | Norske Meierier | 20 |
| 17 | Svensk Sjöföda AB  | 20 |
| 23 | Karkki Oy  | 18.083333333333332 |
| 1  | Exotic Liquid  | 15.666666666666666 |
| 16 | Bigfoot Breweries  | 15.333333333333334 |
| 6  | Mayumi's  |  14.916666666666666 |
