select grade, count(*) 'Frequency'
from testdb.students
group by grade
having grade = 'HD' or grade = 'D';