/*
	Start a transaction as follows:
    - insert a new student to the table
    - update the name by ID
    - show all students
    - commit the transaction
*/
start transaction;
insert into testdb.students(name,mark) value('Jay Creel',55);
update testdb.students set name='Ronaldo Danus' where ID = 100003;
select * from testdb.students;
commit; -- saves the changes permenantly to the table