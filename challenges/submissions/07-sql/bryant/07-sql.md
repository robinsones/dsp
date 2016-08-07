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
```sql
Select SupplierName
FROM Suppliers
WHERE SupplierID =
  (SELECT SupplierID
  FROM Products
  GROUP BY SupplierID
  ORDER BY AVG(Price) DESC);
```
|Answer|
|---------------------|
|Aux joyeux ecclésiastiques|

# Challenge 4
* How many different countries are there customers from? (Hint: Consider DISTINCT.)
```sql
SELECT COUNT(DISTINCT Country)
FROM Customers;
```
|Answer|
|---------------------|
|21|

# Challenge 5
* What category appears the most in order details?
```sql
SELECT CategoryName
FROM Categories
WHERE CategoryID = 
  (SELECT CategoryID
  FROM Products
  WHERE ProductID = 
    (SELECT ProductID
    FROM OrderDetails
    GROUP BY ProductID 
    ORDER BY COUNT(ProductID) DESC
    LIMIT 1))
```
|Answer|
|---------------------|
|Dairy Products|

# Challenge 6
* What was the total cost for each order?
```sql
SELECT OrderID, SUM(Total) as Total
FROM (SELECT od.OrderID, (p.Price * od.Quantity) as Total
FROM OrderDetails as od
INNER JOIN Products as p
ON od.ProductID=p.ProductID)
GROUP BY OrderID
```
|Answer|
|---------------------|
|WAY TO LONG TO POST! Just trust me!|

# Challenge 7
* What employee made the most sales (by total cost)?
```sql
SELECT FirstName, LastName
FROM Employees
WHERE EmployeeID = 
  (SELECT o.EmployeeID
  FROM OrderDetails as od
  INNER JOIN Orders as o
  ON od.OrderID=o.OrderID
  INNER JOIN Products as p
  ON od.ProductID=p.ProductID
  GROUP BY EmployeeID
  ORDER BY SUM(od.Quantity * p.Price)
  LIMIT 1)
```
|Answer|
|---------------------|
|Anne Dodsworth|

# Challenge 8
* What employees have BS degrees? (Hint: Look at the LIKE operator.)
```sql
SELECT FirstName, LastName
FROM Employees
WHERE Notes LIKE '%BS%'
```
|Answer|
|---------------------|
|Janet Leverling|
|Steven Buchanan|


# Challenge 9
* What supplier of three or more products has the highest average product price? (Hint: Look at the HAVING operator.)
```sql
SELECT s.SupplierName
FROM Products as p, Suppliers as s 
WHERE p.SupplierID=s.SupplierID 
GROUP BY p.SupplierID HAVING COUNT(*) >= 3 
ORDER BY Avg(Price)  DESC 
LIMIT 1;
```
|Answer|
|---------------------|
|Tokyo Traders|
