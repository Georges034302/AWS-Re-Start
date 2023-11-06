select name, grade,
curdate() 'Current Date',
dayname(curdate()) 'Today',
monthname(curdate()) 'Month',
day(curdate()) 'Day'
from testdb.students;