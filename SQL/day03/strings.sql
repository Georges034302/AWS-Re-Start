/*
 * Generate a student username (alias the column) composed of:
 * name first letter
 * followed by a -
 * followed by the student ID
 * Username format: <Letter>-<ID>
 */
 
 select name,
 concat(substring(name,1,1),'-',ID) 'Username'
 from testdb.students;