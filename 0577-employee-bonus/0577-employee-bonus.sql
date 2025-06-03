# Write your MySQL query statement below
select name,bonus from Employee
left join Bonus 
on employee.empid = Bonus.empid
where Bonus<1000 OR Bonus is Null