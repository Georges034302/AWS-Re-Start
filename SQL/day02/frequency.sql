select grade,count(*) 'Frequency' from testdb.students
group by grade;