
|Challenge Set 7|
|---------------|
|Topic: |SQL|
|Date: |08/01/2016|
|Name: |Jessica Cox|

Q1.  What customers are from the UK?

```sql
SELECT CustomerName FROM Customers WHERE Country='UK';
```

|CustomerName|
|------------|
|Around the Horn|
|B's Beverages|
|Consolidated Holdings|
|Eastern Connection|
|Island Trading|
|North/South|
|Seven Seas Imports|

Q2.    What is the name of the customer who has the most orders?
```sql
SELECT CustomerID, COUNT(CustomerID) AS MOST_FREQUENT
FROM Orders
GROUP BY CustomerID
ORDER BY COUNT(CustomerID) DESC LIMIT 1;
```
|CustomerID	 |MOST_FREQUENT|
|--------------------------|
|20|	10|

Q3. What supplier has the highest average product price?
```sql
SELECT SupplierID, AVG(Price) FROM Products GROUP BY SupplierID ORDER BY AVG(Price) DESC LIMIT 1;
```
|SupplierID|	AVG(Price)|
|-------------------------|
|18|	140.75|


Q4. How many different countries are their customers from? (Hint: Consider DISTINCT.)

```sql
SELECT COUNT(DISTINCT(Country)) FROM Customers;
COUNT(DISTINCT(Country))
21
```

Q5.  What category appears the most in order details?
```sql
SELECT C.CategoryName,count(C.CategoryID) as most_sold 
FROM OrderDetails O, Categories C, Products P 
WHERE C.CategoryID = P.CategoryID and O.ProductID = O.ProductID 
GROUP BY C.CategoryID 
ORDER BY C.CategoryID DESC LIMIT 1
```
|CategoryName|most_sold|
|----------------------|
|Seafood|6216|

Q6.  What was the total cost for each order?
```sql
SELECT O.OrderID, sum(OD.Quantity*P.Price) 
AS t_cost 
FROM Orders O,OrderDetails OD,Products P, Categories C
WHERE C.CategoryName = 'Seafood'
AND O.OrderID = OD.OrderID and OD.ProductID = P.ProductID 
GROUP BY C.CategoryName
```
|OrderID|t_cost|
|--------------|
|10443|386424.23|

Q7.  What employee made the most sales (by total cost)?
```sql
SELECT E.EmployeeID,E.LastName,E.FirstName,sum(OD.Quantity*P.Price) AS Most_sales 
FROM Orders O,OrderDetails OD,Products P,Employees E 
WHERE O.OrderID = OD.OrderID AND OD.ProductID = P.ProductID 
AND E.EmployeeID = O.EmployeeID 
GROUP BY E.EmployeeID ORDER BY Most_sales DESC LIMIT 1
```
|EmployeeID|LastName|FirstName|Most_sales|
|----------------------------------------|
|4|Peacock|Margaret|105696.49999999999|

Q8. What employees have BS degrees? (Hint: Look at the LIKE operator.)
```sql
SELECT E.EmployeeID, E.LastName, E.FirstName
FROM Employees E
WHERE E.Notes LIKE '%BS%'
```
|EmployeeID|LastName|FirstName|
|-----------------------------|
|3|Leverling|Janet|
|5|Buchanan|Steven|


Q9.  What supplier of three or more products has the highest average product price? (Hint: Look at the HAVING operator.)
```sql
SELECT S.SupplierID, S.SupplierName, AVG(P.Price)
FROM Suppliers S, Products P, Orders O
WHERE S.SupplierID = P.SupplierID
GROUP BY S.SupplierID
HAVING COUNT(P.ProductID) >= 3
ORDER BY AVG(P.Price)
DESC LIMIT 1
```
|SupplierID|SupplierName|AVG(P.Price)|
|------------------------------------|
|18|Aux joyeux ecclésiastiques|140.75|
