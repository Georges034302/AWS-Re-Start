/*
 * find all students with marks 90 and above (not including 100)
 */
select name, mark
from testdb.students
where mark like '9_';
--  where mark between 90 and 99;
-- where mark >= 90 and mark < 100;