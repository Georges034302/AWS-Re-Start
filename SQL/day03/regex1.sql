/*
 * Find all students grades and marks where the student names
 * start with upper-case A and ending with lower-case r
 */
select name, grade, mark
from testdb.students
where name regexp '^A.*r$'; 
