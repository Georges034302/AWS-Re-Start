create table if not exists testdb.students(
	ID integer primary key auto_increment,
    name varchar(50) unique not null,
    mark integer not null
)auto_increment=100000;

alter table testdb.students
add grade varchar(10) as (case
							when mark >= 85 then 'HD'
							when mark >= 75 then 'D'
                            when mark >= 65 then 'C'
                            when mark >= 50 then 'P'
							else 'Z'
						end);