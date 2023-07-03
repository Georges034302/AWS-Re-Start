select name, grade, mark, mark+10 'Adjusted Mark'
from testdb.students
where name like 'Da%'
order by mark asc;