load data infile '[path-to-file]\\students.csv'
into table testdb.students
fields terminated by ',' enclosed by '"'
lines terminated by '\n' ignore 1 rows;