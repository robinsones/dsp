### Excercise 1.


```
SELECT * FROM Customers WHERE Country='UK';
```

|CustomerID|CustomerName|ContactName|Address| City|PostalCode|Country|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|4|	Around the Horn|	Thomas Hardy|	120 Hanover Sq.|	London|	WA1 1DP|	UK|
|11|	B's Beverages|	Victoria Ashworth|	Fauntleroy Circus|	London|	EC2 5NT	|UK|
|16|	Consolidated Holdings|	Elizabeth Brown|	Berkeley Gardens 12 Brewery|	London|	WX1 6LT|UK|
|19|	Eastern Connection|	Ann Devon|	35 King George|	London|	WX3 6FW|	UK|
|38|	Island Trading|	Helen Bennett|	Garden House Crowther Way|	Cowes|	PO31 7PJ|	UK|

### Excercise 2.

```
SELECT CustomerName, ContactName, COUNT(c.CustomerID) as counts
FROM Customers as c
JOIN Orders as o
ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID
ORDER BY counts DESC
```

|CustomerName|					ContactName|		  counts|
| :--- | :--- | :---: |
|Ernst Handel|					Roland Mendel|		10|
|QUICK-Stop|					Horst Kloss|			7|
|Rattlesnake Canyon Grocery|		Paula Wilson|		7|
|Wartian Herkku|					Pirkko Koskitalo|	7|
|Hungry Owl All-Night Grocers|	Patricia McKenna|	6|
|Split Rail Beer & Ale|			Art Braunschweiger|	6|


### Exercise 3.


```
SELECT s.SupplierName, AVG(p.Price) as mean
FROM Products as p
JOIN Suppliers as s
ON p.SupplierID = s.SupplierID
GROUP BY p.SupplierID
ORDER BY mean DESC
```


|SupplierName|						mean|
| :--- | :----|
|Aux joyeux ecclésiastiques|			140.75|
|Tokyo Traders|						46|
|Plutzer Lebensmittelgroßmärkte AG|	44.678|
|Gai pâturage|						44.5|
|Forêts d'érables|					38.9|


### Excercise 4.


```
SELECT COUNT(DISTINCT Country)
FROM Customers

```

21


### Excersise 5.


```
SELECT c.CategoryName, COUNT(c.CategoryID) as count
FROM Categories as c
JOIN Products as p
ON c.CategoryID = p.CategoryID
JOIN OrderDetails as od
ON p.ProductID = od.ProductID
GROUP BY c.CategoryID
ORDER BY count DESC
```


|CategoryName|			count|
| :--- | :--- |
|Dairy Products|		100|
|Beverages|				93|
|Confections|				84|
|Seafood|					67|
|Meat/Poultry|			50|
|Condiments|				49|
|Grains/Cereals|			42|
|Produce|					33|



### Excercise 6.


```
SELECT od.OrderID, OrderDate, SUM(p.Price *od.Quantity) as cost
FROM  OrderDetails as od
JOIN Orders as o
ON od.OrderID = o.OrderID
JOIN Products as p
ON od.ProductID = p.ProductID
GROUP BY od.OrderID
ORDER BY cost DESC
```


|OrderID|	OrderDate|	cost|
| :--- | :--- | :--- |
|10372|	1996-12-04|	15353.6|
|10424|	1997-01-23|	14366.5|
|10417|	1997-01-16|	14104|
|10353|	1996-11-13|	13427|
|10360|	1996-11-22|	9244.25|


### Excercise 7.


```
SELECT e.LastName, e.FirstName, SUM(p.Price * od.Quantity) as sales
FROM Employees as e
JOIN Orders as o
ON e.EmployeeID = o.EmployeeID
JOIN OrderDetails as od
ON o.OrderID = od.OrderID
JOIN Products as p
ON od.ProductID = p.ProductID
GROUP BY e.EmployeeID
ORDER BY sales DESC
```


|LastName|	 FirstName|			sales|
| :--- | :--- | :---|
|Peacock|		Margaret|		105696.5|
|Davolio|		Nancy|			57690.39|
|Leverling|	Janet|			42838.35|
|King|		Robert|			39772.3|
|Callahan|	Laura|			39309.38|


### Excercise 8.


```
SELECT LastName,FirstName,Notes
FROM Employees
WHERE Notes
LIKE '%BS%'
```


|LastName|	FirstName|	Notes|
| :--- | :--- | :--- |
|Leverling|	Janet|	Janet has a BS degree in chemistry from Boston College). She has also completed a certificate program in food retailing 		management. Janet was hired as a sales associate and was promoted to sales representative.|
|Buchanan|	Steven|	Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree. Upon joining the company as a sales representative, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London, where he was promoted to sales manager. Mr. Buchanan has completed the courses 'Successful Telemarketing' and 'International Sales Management'. He is fluent in French.|


### Excercise 9.


```
SELECT p.SupplierID, s.SupplierName, COUNT(p.ProductName) as numprod, AVG(p.Price) as mean
FROM Products as p
JOIN Suppliers as s
ON p.SupplierID = s.SupplierID
GROUP BY p.SupplierID
HAVING numprod>2
ORDER BY mean DESC
```


|SupplierID|		SupplierName|						numprod|		mean|
| :--- | :--- | :--- | :--- |
|4|			Tokyo Traders|						3|			46|
|12|			Plutzer Lebensmittelgroßmärkte AG|	5|			44.678|
|7|			Pavlova, Ltd.|						5|			35.57|
|3|			Grandma Kelly's Homestead|			3|			31.667|
|24|			G'day, Mate|					3|			30.933|

