select name, mark, grade,
row_number() over(partition by grade order by mark) 'Row Number'
from testdb.students;
-- row_number() gives each row a number
-- each duplicate has a unique number
-- there are no skipping for duplicate values
-- ranking is reset when category changes
