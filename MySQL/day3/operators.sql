select name, grade, mark 
from testdb.students
where mark >= 50 
and grade in ('D', 'HD')
order by mark desc limit 10;