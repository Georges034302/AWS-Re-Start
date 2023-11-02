/*
 * Create a students table, with the following specifications:
 * column ID integer as primary key, auto_incremented from 100000
 * column name string of size 50, unique and not null (not allowed to be empty)
 * mark is an integer, not null
 */
 create table if not exists testdb.students(
	ID integer primary key auto_increment,
    name varchar(50) unique not null,
    mark integer not null
)auto_increment=100000;

-- provides information about the table columns
describe testdb.students;

/*
 * add a grade column auto-caculated based on mark
 */
 alter table testdb.students
 add grade varchar(10) as (
	case 
		when mark >= 85 then 'HD'
        when mark >= 75 then 'D'
        when mark >= 65 then 'C'
        when mark >= 50 then 'P'
        else 'Z'
	end);
 
 -- provides information about the table columns
describe testdb.students;
 
 
 
 
 
 
 
 
 