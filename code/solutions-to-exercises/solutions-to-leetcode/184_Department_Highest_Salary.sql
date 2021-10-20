-- 看了题解才写出来where条件，关键在于in操作，两个列同时in，以前没这样写过

select department.name Department, employee.name Employee , employee.salary Salary 
from employee join department
on employee.DepartmentId  = department.id
where (departmentid, salary) in(
    select e.departmentid, max(salary)
    from employee e
    group by departmentid
)
