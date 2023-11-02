-- adding a column to an existing table
alter table testdb.students
add phone integer;

-- removing a column from table
alter table testdb.students
drop column phone;

-- modify column data type
alter table testdb.students
modify phone varchar(20);

-- rename a column in a table
alter table testdb.students
rename column phone to mobile;