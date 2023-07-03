select grade, count(*) as Frequency,
concat(round(count(*)*100/sum(count(*)) over(),2),' %') 'Precentage'
from testdb.students
group by grade;

/*
	Percentage:
    total_count * 100 / total_sum
*/