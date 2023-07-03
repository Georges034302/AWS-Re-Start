/*
	Start a transaction as follows:
    - insert a new student in the table
    - update student name and mark by ID
    - delete student by ID
    - show all students
    Enable rollback the transaction
*/
start transaction;
insert into testdb.students(name,mark) value('Alen Roberts',78);
update testdb.students set name='Rony' where ID=100003;
delete from testdb.students where ID=100046;
select * from testdb.students;
rollback; -- revert to previous table state if any operation fails