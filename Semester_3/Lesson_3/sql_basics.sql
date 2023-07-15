-- extract data first_name, last_name and city columns from people table
-- where quiz_points are between (interval) 100 points and 120 points.
select first_name, last_name, city 
from people
where quiz_points between 100 and 120;


-- extract data from first_name, last_name, city columns from people TABLE
select first_name, last_name, city 
from people
-- where first_name starts with any character(s) and exactly ends with 'a'
where first_name like '%a';
-- where first_name starts with one character (required) and ends with any character(s).
-- '_' for exactly one character and '%' for any count of character(s).
where first_name like '_a%';


-- Operators:
-- 		< - less than
--		> - greater than
-- 		<= - less or equal
-- 		>= - greater or equal
-- 		!=, <> - not equal
--		(column) IN '' - if column in '' 
select * from people
where quiz_points != 100;

-- ordering items
-- with ORDER BY
-- structure
-- select (columns) from (table) ORDER BY (column(s)) (default is asc) asc or desc;

select * from people
ORDER BY first_name desc;


-- CASE clause
select first_name, last_name, age,
	CASE
		WHEN age > 40 THEN 'Adults content :1'
		WHEN age > 18 THEN 'You can drive now!'
		ELSE 'You are still child :D'
	END as 'RESPONSE'
from people;
