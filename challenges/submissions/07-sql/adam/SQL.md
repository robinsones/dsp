**Challenge 1**  
What customers are from the UK?

```sql
SELECT 
    CustomerName
FROM 
    Customers
WHERE
    Country='UK';
```

Around the Horn
B's Beverages
Consolidated Holdings
Eastern Connection
Island Trading
North/South
Seven Seas Imports

**Challenge 2**  
What is the name of the customer who has the most orders?

```sql
SELECT 
    CustomerName, num_orders
FROM
    (
    SELECT
        CustomerID, Count(*) as num_orders
    FROM
        Orders
    GROUP BY
        CustomerID
    ORDER BY
        num_orders DESC
    LIMIT 
        1
    ) a
JOIN
    Customers
ON
    a.CustomerID=Customers.CustomerID;
```

Ernst Handel    10

**Challenge 3**  
What supplier has the highest average product price?

```sql
SELECT
    SupplierName,
    AVG(Price) AS avg
FROM
    Products
JOIN
    Suppliers
ON
    Products.SupplierID=Suppliers.SupplierID
GROUP BY
    Suppliers.SupplierID
ORDER BY
    avg DESC
LIMIT
    1;
```

Aux joyeux ecclésiastiques  140.75

**Challenge 4**  
How many different countries are their customers from? (Hint: Consider DISTINCT.)

```sql
SELECT
    Count(*)
FROM
    (
    SELECT
        DISTINCT(Country)
    FROM 
        Customers
    GROUP BY
        Country
    );
```

21

**Challenge 5**  
What category appears the most in order details?

```sql
SELECT
    CategoryName,
    Count(*) AS count
FROM
    OrderDetails
JOIN
    Products
ON
    OrderDetails.ProductID=Products.ProductID
JOIN
    Categories
ON
    Categories.CategoryID=Products.CategoryID
GROUP BY
    CategoryName
ORDER BY
    count DESC
LIMIT
    1;
```

Dairy Products  100

**Challenge 6**  
What was the total cost for each order?

```sql
SELECT
   OrderID,
   SUM(totalprice) as totalprice
FROM
    (SELECT
        Price*Quantity as totalprice,
        OrderID
    FROM
        OrderDetails
    JOIN
        Products
    ON
        OrderDetails.ProductID=Products.ProductID)
GROUP BY
    OrderID
ORDER BY
    totalprice DESC
LIMIT
    5;

    OrderID totalprice
    10372   15353.6
    10424   14366.5
    10417   14104
    10353   13427
    10360   9244.250000000002

**Challenge 7**  
What employee made the most sales (by total cost)?

```sql
SELECT
    FirstName, LastName, totalsales
FROM
    (SELECT
        EmployeeID,
        SUM(totalprice) as totalsales
    FROM
        (SELECT
            EmployeeID,
            totalprice
        FROM
            (SELECT
                SUM(totalprice) as totalprice,
                OrderID
            FROM
                (SELECT
                    Price*Quantity as totalprice,
                    OrderID
                FROM
                    OrderDetails
                JOIN
                    Products
                ON
                    OrderDetails.ProductID=Products.ProductID)
            GROUP BY
                OrderID) a
        JOIN
            Orders
        ON
            a.OrderID = Orders.OrderID)
    GROUP BY
        EmployeeID
    ORDER BY
        totalsales DESC
    LIMIT 1) b
JOIN
    Employees
ON
    b.EmployeeID=Employees.EmployeeID;
```

Margaret    Peacock 105696.49999999999

**Challenge 8**  
What employees have BS degrees? (Hint: Look at the LIKE operator.)

``sql
SELECT
    FirstName,
    LastName
FROM
    Employees
WHERE 
    Notes LIKE '%BS%';
```

Janet   Leverling
Steven  Buchanan

**Challenge 9**  
What supplier of three or more products has the highest average product price? (Hint: Look at the HAVING operator.)

```sql
SELECT
    SupplierName
FROM
    (SELECT
        AVG(Price) as aveprice,
        SupplierID,
        COUNT(*) as count
    FROM
        Products
    GROUP BY
        SupplierID
    HAVING
        count > 2) a
JOIN
    Suppliers
ON
    Suppliers.SupplierID=a.SupplierID
ORDER BY
    aveprice DESC
LIMIT 1;
```

Tokyo Traders
