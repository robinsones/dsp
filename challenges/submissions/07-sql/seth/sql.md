### SQL Challenges

The core SQL challenges consist of the activities at the end of the SQL lab.  
http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all  

You can run the queries in W3 schools and include your work in a markdown file (exercise number, question, SQL query, result of query)

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
SELECT ContactName FROM Customers WHERE Country='UK';
```

>Thomas Hardy
Victoria Ashworth
Elizabeth Brown
Ann Devon
Helen Bennett
Simon Crowther
Hari Kumar

**Challenge 2**

What is the name of the customer who has the most orders?

```sql
select customername, count(customername) from orders 
    join customers on customers.customerid=orders.customerid 
    group by orders.customerid 
    order BY count(customername) desc;
```

>Ernst Handel 10

**Challenge 3**

What supplier has the highest average product price?

```sql
select suppliername,avg(price) from [suppliers] 
join products 
on suppliers.supplierID = products.SupplierID 
group by suppliername
order by avg(price)
desc;
```
>Aux joyeux ecclésiastiques  140.75

**Challenge 4**

How many different countries are their customers from? (Hint: Consider DISTINCT.)

```sql
select count(distinct(country)) from customers order by count(country) desc;
```

>count(distinct(country))
21


**Challenge 5**

What category appears the most in order details?

```sql
select categoryname, count(categoryname)  from orderdetails
join products  on products.productid = orderdetails.productid
join categories on categories.categoryid = products.categoryid
group by categories.categoryid 
order by count(categoryname) desc;
```

>CategoryName count(categoryname)
Dairy Products 100

**Challenge 6**

What was the total cost for each order?

```sql
select orderid, sum(quantity*price) FROM orderdetails 
join products on products.productid = orderdetails.productid
group by orderid
order by quantity*sum(price) desc;
```
>OrderID sum(quantity*price)
10372 15353.6
10440 7246.01
10353 13427
10360 9244.250000000002

**Challenge 7**

What employee made the most sales (by total cost)?

```sql
select firstname, lastname, sum(price*quantity) as total from orderdetails
join orders on orders.orderid=orderdetails.orderid
join employees on orders.employeeid = employees.employeeid
join products on products.productid = orderdetails.productid
group by orders.employeeid
order by total desc;
```

>FirstName LastName total
Margaret Peacock 105696.49999999999
Nancy Davolio 57690.38999999999
Janet Leverling 42838.350000000006
Robert King 39772.3
Laura Callahan 39309.380000000005


**Challenge 8**

What employees have BS degrees? (Hint: Look at the LIKE operator.)

```sql
select firstname, lastname, notes FROM Employees
where notes like '%bs%';
```
>FirstName LastName
Janet Leverling
Steven Buchanan

**Challenge 9**

What supplier of three or more products has the highest average product price? (Hint: Look at the HAVING operator.)

```sql
select suppliername, avg(price) from products 
join suppliers on suppliers.supplierid=products.supplierid
group by suppliername
having count(productname)>=3
order by avg(price) desc;
```

>SupplierName avg(price)
Tokyo Traders 46
Plutzer Lebensmittelgroßmärkte AG 44.678000000000004
Pavlova, Ltd. 35.57
Grandma Kelly's Homestead 31.666666666666668
G'day, Mate 30.933333333333334











---

If you like, you can also do [more](more.md).

