select e.name
from Employee as e
join employee as emp 
on e.id=emp.managerId 
GROUP BY e.Id ,e.name
having Count(e.Id)>=5
;