
---

**Challenge 0 - Practice Example**

What customers are from Sweden?

```sql
SELECT * FROM Customers WHERE Country='Sweden';
```

>Berglunds snabbköp  	Christina Berglund  
Folk och fä HB  	Maria Larsson   

---

**Challenge 1**

What customers are from the UK?

```sql
SELECT * 
FROM Customers
WHERE Country='UK';
```

>CustomerID	CustomerName	ContactName	Address	City	PostalCode	Country
4	Around the Horn	Thomas Hardy	120 Hanover Sq.	London	WA1 1DP	UK
11	B's Beverages	Victoria Ashworth	Fauntleroy Circus	London	EC2 5NT	UK
16	Consolidated Holdings	Elizabeth Brown	Berkeley Gardens 12 Brewery	London	WX1 6LT	UK
19	Eastern Connection	Ann Devon	35 King George	London	WX3 6FW	UK
38	Island Trading	Helen Bennett	Garden House Crowther Way	Cowes	PO31 7PJ	UK
53	North/South	Simon Crowther	South House 300 Queensbridge	London	SW7 1RZ	UK
72	Seven Seas Imports	Hari Kumar	90 Wadhurst Rd.	London	OX15 4NB	UK

**Challenge 2**

What is the name of the customer who has the most orders?

```sql
SELECT CustomerID, 
count(CustomerID) as count 
FROM [Orders] 
GROUP BY CustomerID 
ORDER BY count DESC;
```

>CustomerID	count
20	10

```sql
SELECT CustomerID, 
CustomerName 
FROM [Customers] 
WHERE CustomerID=20;
```

>CustomerID	CustomerName
20	Ernst Handel

answer-Ernst Handel


**Challenge 3**

What supplier has the highest average product price?

```sql
SELECT SupplierID,
avg(Price) as avg 
FROM [Products]
GROUP BY SupplierID
ORDER BY avg DESC;
```

>SupplierID	avg
18	140.75

```sql
SELECT SupplierID,SupplierName FROM [Suppliers] WHERE SupplierID=18;
```

>SupplierID	SupplierName
18	Aux joyeux ecclésiastiques

answer-Aux joyeux ecclésiastiques


**Challenge 4**

How many different countries are their customers from? (Hint: Consider DISTINCT.)

```sql
SELECT count(DISTINCT Country) FROM [Customers]
```

>count(DISTINCT Country)
21


**Challenge 5**

What category appears the most in order details?

```sql
SELECT OrderDetails.ProductID, Products.CategoryID, count(Products.CategoryID) as count, CategoryName 
FROM [OrderDetails],Products, Categories 
WHERE OrderDetails.ProductID=Products.ProductID 
AND Products.CategoryID=Categories.CategoryID 
GROUP BY Products.CategoryID 
ORDER BY count DESC
```

>ProductID	CategoryID	count	CategoryName
11	4	100	Dairy Products

answer- Dairy Products


**Challenge 6**

What was the total cost for each order?

```sql
SELECT OrderID ,sum(Quantity*Price) as sum 
FROM [OrderDetails],Products 
WHERE OrderDetails.ProductID=Products.ProductID 
GROUP BY OrderId 
```

>OrderID	sum
10248	566
10249	2329.25
10250	2267.25
10251	839.5
10252	4662.5
10253	1806


**Challenge 7**

What employee made the most sales (by total cost)?

```sql
SELECT sum(Quantity*Price) as sum, Orders.EmployeeID,LastName,FirstName 
FROM [OrderDetails],Products, Orders,Employees
WHERE OrderDetails.ProductID=Products.ProductID AND Orders.EmployeeID=Employees.EmployeeID
GROUP BY Orders.EmployeeID
ORDER BY sum DESC
```
>sum	EmployeeID	LastName	FirstName
15456969.200000014	4	Peacock	Margaret

answer-Margaret Peacock


**Challenge 8**

What employees have BS degrees? (Hint: Look at the LIKE operator.)

```sql
SELECT count(EmployeeID) FROM [Employees] WHERE Notes LIKE '%BS%'
```
>2



**Challenge 9**

What supplier of three or more products has the highest average product price? (Hint: Look at the HAVING operator.)

```sql
SELECT SupplierName, avg(Price) 
FROM [Products],Suppliers 
WHERE Suppliers.SupplierID=Products.SupplierID
GROUP BY Products.SupplierID 
HAVING count(ProductID) >= 3
ORDER BY avg(Price) DESC
```

>SupplierName	avg(Price)
Tokyo Traders	46

answer-TokyoTraders

