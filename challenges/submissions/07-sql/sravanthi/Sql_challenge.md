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

![1](/challenges/submissions/07-sql/sravanthi/images/1.png)

**Challenge 2**

What is the name of the customer who has the most orders?
>> SELECT c.CustomerName, count(*) as Number_Of_Orders from Orders o ,Customers c where c.CustomerID = o.CustomerID group by o.CustomerID order by Number_Of_Orders DESC LIMIT 1

![2](/challenges/submissions/07-sql/sravanthi/images/2.png)

**Challenge 3**

What supplier has the highest average product price?

>> SELECT s.SupplierName,Avg(p.Price) as Avg_Price FROM Suppliers s, Products p where s.SupplierID = p.SupplierID group by s.SupplierName order by Avg_Price Desc LIMIT 1

![3](/challenges/submissions/07-sql/sravanthi/images/3.png)

**Challenge 4**

How many different countries are their customers from? (Hint: Consider DISTINCT.)

>> SELECT count(distinct(Country)) as Num_of_Countries FROM [Customers]

![4](/challenges/submissions/07-sql/sravanthi/images/4.png)

**Challenge 5**

What category appears in the most orders?

>> SELECT c.CategoryName,count(c.CategoryID) as Most_Sold_category FROM OrderDetails o, Categories c, Products p where c.CategoryID = p.CategoryID and o.ProductID = p.ProductID group by c.CategoryID order by c.CategoryID Desc LIMIT 1 

![5](/challenges/submissions/07-sql/sravanthi/images/5.png)

**Challenge 6**

What was the total cost for each order?

>> SELECT o.OrderID,sum(od.Quantity*p.Price) as Total_cost FROM Orders o,OrderDetails od,Products p where o.OrderID = od.OrderID and od.ProductID = p.ProductID group by o.OrderID

![6](/challenges/submissions/07-sql/sravanthi/images/6.png)


**Challenge 7**

What employee made the most sales (by total cost)?

>> SELECT e.EmployeeID,e.LastName,e.FirstName,sum(od.Quantity*p.Price) as Order_Total FROM Orders o,OrderDetails od,Products p,Employees e where o.OrderID = od.OrderID and od.ProductID = p.ProductID and e.EmployeeID = o.EmployeeID group by e.EmployeeID order by Order_Total desc LIMIT 1

![7](/challenges/submissions/07-sql/sravanthi/images/7.png)


**Challenge 8**

What employees have BS degrees? (Hint: Look at the LIKE operator.)

>> SELECT EmployeeID,LastName,FirstName FROM [Employees] where Notes like '%BS%'

![8](/challenges/submissions/07-sql/sravanthi/images/8.png)

**Challenge 9**

What supplier of three or more products has the highest average product price? (Hint: Look at the HAVING operator.)

>> SELECT s.SupplierName,Avg(Price) as Average_Price FROM Products p, Suppliers s where p.SupplierID = s.SupplierID group by p.SupplierID having count(*) >= 3 order by Average_Price Desc LIMIT 1

![9](/challenges/submissions/07-sql/sravanthi/images/9.png)













---

If you like, you can also do [more](more.md).