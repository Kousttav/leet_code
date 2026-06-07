1# Write your MySQL query statement below
2select name as "Customers" from Customers where id not in (select customerid from Orders);