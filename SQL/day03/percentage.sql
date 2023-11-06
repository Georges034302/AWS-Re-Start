/*
 * Determine the grades frequency and percentage
 */
 select grade, count(*) 'Frequency',
 concat(round(count(*)*100/sum(count(*)) over(),2),' %') 'Percentage'
 from testdb.students 
 group by grade;