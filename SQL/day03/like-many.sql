/*
 * Find all the names (starting with Da) and their grades
 * sorted by mark descending order
 */
 select name, grade
 from testdb.students
 where name like 'Da%'
 order by mark desc;
 