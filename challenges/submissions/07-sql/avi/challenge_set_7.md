Challenge Set 7  
Topic:        SQL  
Date:         07/31/2016  
Name:         Avi Grunwald  
Worked with:  

**Challenge 1**

What customers are from the UK?  

```sql
SELECT * FROM Customers WHERE Country='UK';
```

>4	Around the Horn	Thomas Hardy	120 Hanover Sq.	London	WA1 1DP	UK  
11	B's Beverages	Victoria Ashworth	Fauntleroy Circus	London	EC2 5NT	UK  
16	Consolidated Holdings	Elizabeth Brown	Berkeley Gardens 12 Brewery	London	WX1 6LT	UK  
19	Eastern Connection	Ann Devon	35 King George	London	WX3 6FW	UK  
38	Island Trading	Helen Bennett	Garden House Crowther Way	Cowes	PO31 7PJ	UK  
53	North/South	Simon Crowther	South House 300 Queensbridge	London	SW7 1RZ	UK  
72	Seven Seas Imports	Hari Kumar	90 Wadhurst Rd.	London	OX15 4NB	UK  

---

**Challenge 2**

What is the name of the customer who has the most orders?

```sql
SELECT CustomerName, o.customerID, count(*) as cnt FROM Customers as c
  JOIN Orders as o ON (c.CustomerID=o.CustomerID)
  GROUP BY o.CustomerID ORDER BY cnt DESC LIMIT 1;
```

>Ernst Handel	20	10  

---

**Challenge 3**

What supplier has the highest average product price?

```sql
SELECT SupplierName, p.supplierID, AVG(Price) as avgp FROM Suppliers as s
  JOIN Products as p ON (s.SupplierID=p.SupplierID)
  GROUP BY p.SupplierID ORDER BY avgp DESC LIMIT 1;
```

>Aux joyeux ecclésiastiques	18	140.75

---
**Challenge 4**

How many different countries are their customers from?

```sql
SELECT COUNT(DISTINCT(country)) FROM Customers;
```

>21

---

**Challenge 5**

What category appears the most in order details?

```sql
SELECT CategoryName, c.CategoryID, count(*) as cnt FROM OrderDetails as od
  JOIN Products as p ON (od.ProductID=p.ProductID)
  JOIN Categories as c ON (p.CategoryID=c.CategoryID)
  GROUP BY c.CategoryID ORDER BY cnt DESC LIMIT 1;
```

>Dairy Products	4	100

---

**Challenge 6**

What was the total cost for each order?

```sql
SELECT od.OrderID, SUM(od.Quantity * p.Price) FROM OrderDetails as od
  JOIN Products as p ON (od.ProductID=p.ProductID)
  GROUP BY od.OrderID LIMIT 5;
```

>10248	566  
10249	2329.25  
10250	2267.25  
10251	839.5  
10252	4662.5  

---

**Challenge 7**

What employee made the most sales (by total cost)?

```sql
SELECT e.LastName, e.FirstName, o.EmployeeID, SUM(od.Quantity * p.Price) as tc
  FROM OrderDetails as od
  JOIN Products as p ON (od.ProductID=p.ProductID)
  JOIN Orders as o ON (o.OrderID=od.OrderID)
  JOIN Employees as e ON (o.EmployeeID=e.EmployeeID)
  GROUP BY o.EmployeeID ORDER BY tc DESC LIMIT 1;
```

>Peacock	Margaret	4	105696.49999999999

---

**Challenge 8**

What employees have BS degrees?

```sql
SELECT * FROM Employees WHERE Notes LIKE '%BS%'
```

>3	Leverling	Janet	1963-08-30	EmpID3.pic	Janet has a BS degree in chemistry from Boston College). She has also completed a certificate program in food retailing management. Janet was hired as a sales associate and was promoted to sales representative.  
5	Buchanan	Steven	1955-03-04	EmpID5.pic	Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree. Upon joining the company as a sales representative, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London, where he was promoted to sales manager. Mr. Buchanan has completed the courses 'Successful Telemarketing' and 'International Sales Management'. He is fluent in French.

---

**Challenge 9**

What supplier of three or more prodcuts has the highest average product price?

```sql
SELECT SupplierName, AVG(p.Price) as avgp FROM Suppliers as s
  JOIN Products as p ON (p.SupplierID=s.SupplierID)
  GROUP BY SupplierName
  HAVING COUNT(p.ProductID) > 2
  ORDER BY avgp DESC LIMIT 1;
```

>Tokyo Traders	46
