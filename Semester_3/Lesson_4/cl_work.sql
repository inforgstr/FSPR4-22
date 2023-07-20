-- Queries
-- 1
select DISTINCT(Name) as 'Name of Country' from Country;

-- 2
select Name from Country
where Continent = 'Asia';

-- 3
select Name, Continent, IndepYear from Country
where IndepYear > 1990 or IndepYear = 1990
ORDER by IndepYear desc;
-- 
-- 4
select IndepYear from Country
where (IndepYear not NULL) and
(IndepYear BETWEEN 15000 and 24318000) 
LIMIT 10;

-- 5
select Name, HeadOfState,
	CASE 
		WHEN GovernmentForm = 'Republic' THEN 'Республика'
		WHEN GovernmentForm = 'Monarchy' THEN 'Монархия'
		WHEN GovernmentForm = 'Federal Republic' THEN 'Федерация'
		ELSE 'Иные виды правления'
	END as 'Форма управления'
from Country;


-- Aggregate functions
-- 1
select sum(Population) 
from Country;



-- 2 
select avg(LifeExpectancy) from Country;


-- 3
select Continent, max(LifeExpectancy) from Country
GROUP by 1;


-- 4
select Name, sum(Population) as 'Population sum'
from Country
GROUP by Name
ORDER by Population desc;