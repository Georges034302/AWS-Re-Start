/*
 * Hash all names from the 3rd character in a new column 'Hashed Names'
 */
select name,
insert(name,3,length(name),'#') 'Hashed Names'
from testdb.students;