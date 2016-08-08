
# Challenge set 7


Name: Marc Gameroff  
Topic: SQL  
Date: August 7 2016

## Challenge 1

What customers are from the UK?

```SQL
SELECT * 
FROM [Customers]
WHERE Country = 'UK';
```

Answer:    
**Around the Horn  Thomas Hardy  120 Hanover Sq.  London  WA1 1DP  UK  
B's Beverages  Victoria Ashworth  Fauntleroy Circus  London  EC2 5NT  UK  
Consolidated Holdings  Elizabeth Brown  Berkeley Gardens 12 Brewery  London  WX1 6LT  UK  
Eastern Connection  Ann Devon  35 King George  London  WX3 6FW  UK  
Island Trading  Helen Bennett  Garden House Crowther Way  Cowes  PO31 7PJ  UK  
North/South  Simon Crowther  South House 300 Queensbridge  London  SW7 1RZ  UK  
Seven Seas Imports  Hari Kumar  90 Wadhurst Rd.  London  OX15 4NB  UK**


---

## Challenge 2

What is the name of the customer who has the most orders?

```SQL
SELECT CustomerName count(o.CustomerID) AS num_orders
FROM Orders as o
JOIN Customers as c
ON o.CustomerID = c.CustomerID
GROUP BY CustomerName
ORDER BY num_orders DESC LIMIT 1
```

Answer:    
**Ernst Handel**

---

## Challenge 3

What supplier has the highest average product price?

```SQL
SELECT s.SupplierName AVG(p.Price) AS avg_price
FROM Products as p
JOIN Suppliers as s
ON p.SupplierID = s.SupplierID
GROUP BY SupplierName
ORDER BY avg_price DESC LIMIT 1
```

Answer:   
**Aux joyeux ecclésiastiques**

---

## Challenge 4

How many different countries are their customers from? (Hint: Consider DISTINCT.)

```SQL
SELECT count(DISTINCT(Country)) 
FROM Customers
```

Answer:    
**21**

---

## Challenge 5

What category appears the most in order details?

```SQL
SELECT categoryname COUNT(categoryname) AS count
FROM Products AS p
JOIN OrderDetails AS o
ON o.ProductID=p.productID
JOIN Categories AS c
ON c.CategoryID = p.CategoryID
GROUP BY categoryname
ORDER BY COUNT(categoryname) DESC LIMIT 1
```

Answer:   
**Dairy Products**

---

## Challenge 6

What was the total cost for each order?


```SQL
SELECT o.OrderID sum(quantity*price) AS TOT_PRICE 
FROM [Orders] AS O
JOIN ORDERDETAILS AS OD
ON O.ORDERID = OD.ORDERID
JOIN PRODUCTS AS P
ON P.PRODUCTID = OD.PRODUCTID
group by o.orderid
order by tot_price desc
```


Beginning of output:

Number of Records: 196  
OrderID TOT_PRICE  
10372 **15353.6**  
10424 **14366.5**  
10417 **14104**  
10353 **13427**  

---

## Challenge 7

What employee made the most sales (by total cost)?


```SQL
SELECT e.lastname e.firstname  sum(quantity*price) AS TOT_PRICE
FROM [Orders] AS O
JOIN ORDERDETAILS AS OD
ON O.ORDERID = OD.ORDERID
JOIN PRODUCTS AS P
ON P.PRODUCTID = OD.PRODUCTID
JOIN employees AS e
ON e.employeeid = o.employeeid
GROUP BY o.employeeid
ORDER BY tot_price DESC limit 1
```


Answer:  
**Margaret Peacock**

---


## Challenge 8

What employees have BS degrees? (Hint: Look at the LIKE operator.)


```SQL
SELECT lastname firstname 
FROM [Employees]
WHERE notes LIKE \%BS%\
```


Answer:  
**Janet Leverling  
Steven Buchanan** 

---


## Challenge 9

What supplier of three or more products has the highest average product price? (Hint: Look at the HAVING operator.)


```SQL
SELECT s.SupplierName AVG(p.Price) AS avg_price COUNT(DISTINCT(p.productid)) AS num_prods
FROM Products AS p
left JOIN Suppliers AS s
ON p.SupplierID = s.SupplierID
GROUP BY SupplierName
HAVING num_prods > 2
ORDER BY avg_price DESC LIMIT 1
```

Answer:  
**Tokyo Traders**

