# Write your MySQL query statement below
select Product_name,year,price 
from Sales inner join Product
on Sales.product_id=product.product_id