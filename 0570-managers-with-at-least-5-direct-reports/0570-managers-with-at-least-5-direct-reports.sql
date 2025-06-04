select  e2.name as name from Employee e1 
join Employee e2 
on e1.managerId  = e2.id
group by e1.managerId
having count(distinct e1.id)>=5