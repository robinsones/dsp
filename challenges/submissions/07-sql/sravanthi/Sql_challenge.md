### SQL Challenges



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

>> SELECT * FROM [Customers] where Country = 'UK'

**Challenge 2**

What is the name of the customer who has the most orders?
>> SELECT c.CustomerName, count(*) as Number_Of_Orders from Orders o ,Customers c where c.CustomerID = o.CustomerID group by o.CustomerID order by Number_Of_Orders DESC LIMIT 1

**Challenge 3**

What supplier has the highest average product price?

>> SELECT s.SupplierName,Avg(p.Price) as Avg_Price FROM Suppliers s, Products p where s.SupplierID = p.SupplierID order by Avg_Price Desc LIMIT 1

**Challenge 4**

How many different countries are their customers from? (Hint: Consider DISTINCT.)

>> SELECT count(distinct(Country)) as Num_of_Countries FROM [Customers]

**Challenge 5**

What category appears in the most orders?

>> SELECT c.CategoryName,count(c.CategoryID) as Most_Sold_category FROM OrderDetails o, Categories c, Products p where c.CategoryID = p.CategoryID and o.ProductID = p.ProductID group by c.CategoryID order by c.CategoryID Desc LIMIT 1 

**Challenge 6**

What was the total cost for each order?

>> select OrderID,sum(total_price) as Total_Order_Price from (select  o.OrderID,(o.Quantity*p.Price) as total_price from OrderDetails o, Products p where o.ProductID = p.ProductID group by o.OrderID,o.ProductID) group by OrderID


**Challenge 7**

What employee made the most sales (by total cost)?

>> SELECT e.EmployeeID,e.LastName,e.FirstName,sum(int_res.Total_cost) as Total_Sales FROM Employees e , (SELECT *,(od.Quantity*p.Price) as Total_cost FROM OrderDetails od, Orders o,Products p where od.OrderID=o.OrderID and p.ProductID = od.ProductID group by od.orderID,od.ProductID order by o.orderID) as int_res order by e.EmployeeID


**Challenge 8**

What employees have BS degrees? (Hint: Look at the LIKE operator.)

>> SELECT EmployeeID,LastName,FirstName FROM [Employees] where Notes like '%BS%'

**Challenge 9**

What supplier of three or more products has the highest average product price? (Hint: Look at the HAVING operator.)

>> SELECT s.SupplierName,Avg(Price) as Average_Price FROM Products p, Suppliers s where p.SupplierID = s.SupplierID group by p.SupplierID having count(*) >= 3 order by Average_Price Desc LIMIT 1













---

If you like, you can also do [more](more.md).
