### Challenge 1:

```sql
SELECT CustomerName,
Country 
FROM Customers
WHERE Country = 'UK'
```

```text
CustomerName            Country
Around the Horn         UK
B's Beverages           UK
Consolidated Holdings	UK
Eastern Connection      UK
Island Trading          UK
North/South             UK
Seven Seas Imports      UK
```

### Challenge 2:

```sql
SELECT C.CustomerName, O.CustomerID, count(O.OrderID) AS Counts
FROM Orders O
INNER JOIN Customers C
ON O.CustomerID=C.CustomerID
GROUP BY C.CustomerName
ORDER BY -Counts;
```

```text
CustomerName	CustomerID	Counts
Ernst Handel	20          10
```

### Challenge 3:

```sql
SELECT SupplierName, round(Avg(Price)) as AveragePrice
FROM Products P
LEFT OUTER JOIN Suppliers S
ON P.SupplierID = S.SupplierID
GROUP BY SupplierName
ORDER BY -AveragePrice;
```

```text
SupplierName                AveragePrice
Aux joyeux ecclésiastiques	  140.75
```

### Challenge 4:

```sql
SELECT COUNT(DISTINCT Country) as Num_Countries 
FROM Customers;
```

```
Num_Countries
21
```

### Challenge 5:

```sql
SELECT CategoryName, Count(OrderID) as Counts
FROM Categories Ca
LEFT OUTER JOIN Products Pr 
ON Ca.CategoryID = Pr.CategoryID
LEFT OUTER JOIN OrderDetails OD
on OD.ProductID = Pr.ProductID
GROUP BY CategoryName
ORDER BY -Counts; 
```

```text
CategoryName        Counts
Dairy Products       100
```

### Challenge 6:

```sql
SELECT OrderID, (Quantity * Price) as TotAmt
FROM OrderDetails OD
LEFT OUTER JOIN Products PR
on PR.ProductID = OD.ProductID
GROUP BY OrderID
ORDER BY -TotAmt;
```

```text
OrderID	  TotAmt
10353	    13175
```

### Challenge 7:

```sql
SELECT FirstName, LastName, round(sum(Quantity * Price),0) as TotAmt
FROM OrderDetails OD
LEFT OUTER JOIN Products PR
on PR.ProductID = OD.ProductID
LEFT OUTER JOIN Orders O 
on O.OrderID = OD.OrderID
LEFT OUTER JOIN Employees E
on E.EmployeeID = O.EmployeeID
GROUP BY FirstName
ORDER BY -TotAmt;
```

```text
FirstName	LastName	TotAmt
Margaret	Peacock	  105696
```

### Challenge 8:

```sql
SELECT *
FROM Employees
WHERE Notes like '%BS Degree%';
```

```text
1, Janet Leverling
```

### Challenge 9:

```sql
SELECT  SN.SupplierName, Count(ProductName) as Count_of_Products, avg(Price) as Average_Price
FROM Suppliers SN
LEFT OUTER JOIN Products P
ON SN.SupplierID = P.SupplierID
GROUP BY SupplierName
HAVING Count_of_Products >= 3
Order by -Average_Price;
```

```text
SupplierName	Count_of_Products	Average_Price
Tokyo Traders           3                 46
```
