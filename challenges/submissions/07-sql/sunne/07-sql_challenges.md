Challenge 1:

SELECT CustomerName,
Country 
FROM Customers
WHERE Country = 'UK'

CustomerName            Country
Around the Horn         UK
B's Beverages           UK
Consolidated Holdings	UK
Eastern Connection      UK
Island Trading          UK
North/South             UK
Seven Seas Imports      UK

Challenge 2:

SELECT C.CustomerName, O.CustomerID, count(O.OrderID) AS Counts
FROM Orders O
INNER JOIN Customers C
ON O.CustomerID=C.CustomerID
GROUP BY C.CustomerName
ORDER BY -Counts;

CustomerName	CustomerID	Counts
Ernst Handel	20          10

Challenge 3:

SELECT SupplierName, round(Avg(Price)) as AveragePrice
FROM Products P
LEFT OUTER JOIN Suppliers S
ON P.SupplierID = S.SupplierID
GROUP BY SupplierName
ORDER BY -AveragePrice;

SupplierName                AveragePrice
Aux joyeux ecclésiastiques	  140.75

Challenge 4:

SELECT COUNT(DISTINCT Country) as Num_Countries 
FROM Customers;

Num_Countries
    21

Challenge 5:

SELECT CategoryName, Count(OrderID) as Counts
FROM Categories Ca
LEFT OUTER JOIN Products Pr 
ON Ca.CategoryID = Pr.CategoryID
LEFT OUTER JOIN OrderDetails OD
on OD.ProductID = Pr.ProductID
GROUP BY CategoryName
ORDER BY -Counts; 

CategoryName        Counts
Dairy Products       100

Challenge 6:

SELECT OrderID, (Quantity * Price) as TotAmt
FROM OrderDetails OD
LEFT OUTER JOIN Products PR
on PR.ProductID = OD.ProductID
GROUP BY OrderID
ORDER BY -TotAmt;

Challenge 7:

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

Challenge 8:

SELECT *
FROM Employees
WHERE Notes like '%BS Degree%';

1, Janet Leverling

Challenge 9:

SELECT  SN.SupplierName, Count(ProductName) as Count_of_Products, avg(Price) as Average_Price
FROM Suppliers SN
LEFT OUTER JOIN Products P
ON SN.SupplierID = P.SupplierID
GROUP BY SupplierName
HAVING Count_of_Products >= 3
Order by -Average_Price;


SupplierName	Count_of_Products	Average_Price
Tokyo Traders           3                 46

