
start transaction;
insert into testdb.students(name,mark) value('Jay Creel',55);
update testdb.students set name='Mal Sinus' where ID = 100003;
select * from testdb.students;
rollback; -- revert the table to previous state if any operation fails