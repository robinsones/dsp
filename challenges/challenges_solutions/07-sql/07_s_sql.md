## Challenge Set 7
## SQL Lab Solutions

### Challenges / Practice

--

**Challenge 1**

What customers are from the UK?

```sql
SELECT * FROM Customers WHERE Country='UK';
```

>Around the Horn  
B's Beverages  
Consolidated Holdings  
Eastern Connection  
Island Trading  
North/South  
Seven Seas Imports  

--


**Challenge 2**

What is the name of the customer who has the most orders?

```sql
SELECT
    CustomerName,
    COUNT(*) as OrderCount
FROM
    Customers AS c
  JOIN
    Orders AS o
  ON c.CustomerID = o.CustomerID
GROUP BY o.CustomerID
ORDER BY OrderCount DESC
LIMIT 1;
```

> **Ernst Handel** with 10 orders

--

**Challenge 3**

What supplier has the highest average product price?

```sql
SELECT
    SupplierName,
    AVG(p.Price) as MeanPrice
FROM
    Suppliers AS s
  JOIN
    Products AS p
  ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID
ORDER BY MeanPrice DESC
LIMIT 1;
```

> **Aux joyeux ecclésiastiques** with average of 140.75

--

**Challenge 4**

How many different countries are their customers from? (Hint: Consider [DISTINCT](http://www.w3schools.com/sql/sql_distinct.asp).)

```sql
SELECT COUNT(DISTINCT(Country)) AS NumCountries FROM Customers;
```

> **21** different countries

--

**Challenge 5**

What category appears in the most orders?

```sql
SELECT
    c.CategoryName
FROM
    OrderDetails as o
  JOIN
    Products as p
  JOIN
    Categories AS c
  ON
      o.ProductID = p.ProductID
    AND
      p.CategoryID = c.CategoryID
GROUP BY c.CategoryID
ORDER BY COUNT(*) DESC
LIMIT 1;
```

> **Dairy Products** on 2601 orders

--

**Challenge 6**

What was the total cost for each order?

```sql
SELECT
    o.OrderID,
    SUM(o.Quantity * p.Price) as Total
FROM
    OrderDetails as o
  JOIN
    Products as p
  ON
    o.ProductID = p.ProductID
GROUP BY o.OrderID
ORDER BY Total DESC;
```

>Here are first 5:  
ID   Total  
10248  566  
10249  2329.25  
10250  2267.25  
10251  839.5  
10252  4662.5

--

**Challenge 7**

What employee made the most sales (by total price)?

```sql
SELECT
    e.FirstName,
    e.LastName,
    SUM(op.Quantity * p.Price) as Total
FROM
    Employees as e
  JOIN
    Orders as o
  JOIN
    OrderDetails as op
  JOIN
    Products as p
  ON
      e.EmployeeID = o.EmployeeID
    AND
      o.OrderID = op.OrderID
    AND
      op.ProductID = p.ProductID
GROUP BY e.EmployeeID
ORDER BY Total DESC;
```

>Margaret Peacock

--

**Challenge 8**

What employees have BS degrees? (Hint: Look at the [LIKE](http://www.w3schools.com/sql/sql_like.asp) operator.)

```sql
SELECT * FROM Employees WHERE Notes LIKE '%BS%';
```

>Janet Leverling  
Steven Buchanan

--

**Challenge 9**

What supplier of three or more products has the highest average product price? (Hint: Look at the [HAVING](http://www.w3schools.com/sql/sql_having.asp) operator.)

```sql
SELECT
    SupplierName,
    COUNT(*) as NumProducts,
    AVG(p.Price) as MeanPrice
FROM
    Suppliers AS s
  JOIN
    Products AS p
  ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID
HAVING 3 <= NumProducts
ORDER BY MeanPrice DESC;
```

>Tokyo Traders