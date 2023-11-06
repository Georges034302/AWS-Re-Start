/*
 * Determine the min, max, average mark at 2-decimal points  (alias all columns)
 */
select
min(mark) 'Min',
max(mark) 'Max',
round(avg(mark),2) 'AVG'
from testdb.students;