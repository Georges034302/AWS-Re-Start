select
min(mark) 'Min',
max(mark) 'Max',
round(avg(mark),2) 'AVG'
from testdb.students;