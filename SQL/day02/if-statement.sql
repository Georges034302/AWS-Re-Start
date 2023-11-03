/*
 * Give all students with marks between 40 and 49, bonus marks to pass
 */
select name, mark, 
if(mark >=40 and mark <= 49,mark+(50-mark),mark) 'New Marks'
from testdb.students;