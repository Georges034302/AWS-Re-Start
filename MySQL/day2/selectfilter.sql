-- return the frequency of each grade
select grade, count(*) 'Grade Frequency'
from testdb.students
where mark >= 75
group by grade
having grade = 'D' -- specify which group to select from the categories
order by grade desc;